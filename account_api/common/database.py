import os
from typing import Any

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(os.environ.get('GOOGLE_CERTIFICATE'))
firebase_admin.initialize_app(
    cred, {'projectId': os.environ.get('GOOGLE_PROJECT_ID'), })


class ModelManager:
    '''User Manager'''

    def __init__(self, model: Any, collection: str) -> None:
        self.model_class = model
        self.collection = collection

        # Firestore initializer
        self.db = firestore.client()

    def get(self, id: str) -> Any:
        '''Get User document'''

        user_ref = self.db.collection(self.collection).document(id)
        doc = user_ref.get()

        if doc.exists:
            data = doc.to_dict()
            data['id'] = id
            return self.model_class.from_dict(**data)

        raise ValueError('Document does not exist')

    def filter(self, *args):
        '''Apply filters to collection'''
        doc_ref = self.db.collection(self.collection).where(*args)

        return doc_ref

    def create(self, obj: object) -> str:
        '''Create new User document'''

        if hasattr(obj, 'to_dict'):
            _, ref = self.db.collection(self.collection).add(obj.to_dict())
        else:
            raise ValueError('Object is not serializable')

        return ref

    def update(self, id: int, **kwargs) -> None:
        '''Update User document'''
        pass

    def delete(self, id: int) -> None:
        '''Delete User'''

        raise NotImplementedError
