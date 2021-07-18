from typing import Optional
from account_api.common.validators import *
from account_api.models.base import IModel
from account_api.common.database import ModelManager
from pydantic import BaseModel, Field


class User(IModel, BaseModel):
    '''User Base Model'''

    id: Optional[str] = Field(title="id", description="Id do usuário")
    full_name: str = Field(title="fullName", description="Nome completo do usuario", max_length=30) 
    email: str = Field(title="email", description="E-mail do usuario", max_length=200) 
    phone: str = Field(title="phone", description="Telefone do usuario (DDI + DDD + NUMERO)", max_length=25) 
    birth_day: str = Field(title="birthDay", description="Timestamp da data de nascimento do usuario", max_length=10) 
    document: str = Field(title="document", description="Numero do documento do usuario", max_length=20)

    def to_dict(self) -> dict:
        '''Return dictionary representing User document'''

        data = {
            'fullName': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'birthDay': self.birth_day,
            'document': self.document,
        }

        if self.id:
            data['id'] = self.id
        
        return data

    @staticmethod
    def from_dict(**kwargs) -> object:
        '''Instantiate class from dictionary of data'''

        data = {
            'full_name': kwargs['fullName'],
            'email': kwargs['email'],
            'phone': kwargs['phone'],
            'birth_day': kwargs['birthDay'],
            'document': kwargs['document']
        }

        if 'id' in kwargs.keys():
            data['id'] = kwargs['id']

        return User(**data)

    def validate_fields(self) -> None:
        '''Validate field values'''

        is_phone_valid(self.phone)
        is_document_valid(self.document)
        is_email_valid(self.email)
        is_user_older_then_eighteen(self.birth_day)

    def validate_unique(self, manager: ModelManager, consider_self_document: bool) -> None:
        '''Validate unique fields'''

        if consider_self_document:
            unique_field_valid(manager, 'email', self.email)
            unique_field_valid(manager, 'document', self.document)

        else:
            filtered_emails: list = manager.filter('email','==', self.email)
            if len([doc for doc in filtered_emails if doc.id != self.id]) > 0:
                raise DuplicatedValue('email')
            
            filtered_docs: list = manager.filter('document','==', self.document)
            if len([doc for doc in filtered_docs if doc.id != self.id]) > 0:
                raise DuplicatedValue('document')
