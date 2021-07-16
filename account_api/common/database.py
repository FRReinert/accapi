import os
from typing import Any

import firebase_admin
from firebase_admin import credentials, firestore

from account_api.models.base import IModel

# Initialize credentials
cred = credentials.Certificate(os.environ.get('ACCAPI_G_CERTIFICATE'))
firebase_admin.initialize_app(
    cred, {'projectId': os.environ.get('ACCAPI_G_PROJECT_ID'), })


class ModelManager:
    '''User Manager'''

    def __init__(self, model: Any, collection: str) -> None:
        self.model_class = model
        self.collection = collection + '_test' if os.environ.get('ACCAPI_DEBUG') == 'true' else collection

        # Firestore initializer
        self.db = firestore.client()

    def get(self, id: str) -> Any:
        '''Get a single User document'''

        user_ref = self.db.collection(self.collection).document(id)
        doc = user_ref.get()

        if doc.exists:
            data = doc.to_dict()
            data['id'] = id
            print(data)
            return self.model_class.from_dict(**data)

        raise ValueError('Documento nao existe')

    def filter(self, *args):
        '''Apply filters to collection retrieving one or more documents'''
        doc_ref = self.db.collection(self.collection).where(*args)

        return doc_ref

    def create(self, model_fields: dict) -> str:
        '''Create new User document'''

        try:
            _, ref = self.db.collection(self.collection).add(model_fields)
        except Exception as e:
            raise ValueError('Nao foi possivel criar o documento: %s' % str(e))
        
        return ref

    def update(self, id: int, **kwargs) -> None:
        '''Update User document'''
        pass

    def delete(self, id: int) -> None:
        '''Delete User'''

        return self.db.collection(self.collection).document(id).delete()
