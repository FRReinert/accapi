from account_api.models.base import IModel
import os

import firebase_admin
from firebase_admin import credentials, firestore
from mockfirestore import MockFirestore

cred = credentials.Certificate(os.environ.get('ACCAPI_G_CERTIFICATE'))
firebase_admin.initialize_app(cred, {'projectId': os.environ.get('ACCAPI_G_PROJECT_ID'), })


class ModelManager:
    '''User Manager'''

    def __init__(self, collection: str, test_mode: bool = False) -> None:
        self.collection = collection
        self.test_mode = test_mode

        if self.test_mode:
            self.db = MockFirestore()
        else:
            self.db = firestore.client()

    def get(self, id: str) -> dict:
        '''Get a single User document'''

        user_doc = self.db.collection(self.collection).document(id).get()
        if user_doc.exists:
            data = user_doc.to_dict()
            data['id'] = id
            return data

        raise ValueError('Documento nao existe')

    def filter(self, *args) -> list:
        '''Filter documents and return them'''
        doc_ref = self.db.collection(self.collection).where(*args)

        return [doc for doc in doc_ref.stream()]

    def create(self, model_obj: IModel) -> str:
        '''Create new Document and return its ID'''

        try:
            _, ref = self.db.collection(self.collection).add(model_obj.to_dict())
            return ref.id

        except Exception as e:
            raise ValueError('Nao foi possivel criar o documento: %s' % str(e))

    def update(self, id: int, user: IModel) -> bool:
        '''Update User document'''

        try:
            user_ref = self.db.collection(self.collection).document(id)
            user_ref.update(user.to_dict())
            user_ref.get()
            return self.get(id)
        
        except Exception as e:
            raise ValueError('Nao foi possivel atualizar: %s' % str(e))


    def delete(self, id: int) -> None:
        '''Delete User'''

        raise NotImplementedError

    def reset(self) -> bool:
        '''Reset test database'''

        if self.test_mode:
            try:
                self.db.reset()
                return True
            except:
                return False
