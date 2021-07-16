'''
TODO
    [ ] Não permitir o cadastro de CPF ou e-mail duplicado;
    [X] Validar se CPF, e-mail, telefone são dados válidos;
    [X] Validar se a data de nascimento é maior ou igual que 18 anos;
    [X] O id do objeto User é o ID gerado pelo banco de dados;
'''
from typing import Optional
from account_api.common.validators import *
from account_api.models.base import IModel
from pydantic import BaseModel, Field, validator


class User(IModel, BaseModel):
    '''User Base Model'''

    id: Optional[str] = Field(title="id", description="Id do usuário")
    full_name: str = Field(title="fullName", description="Nome completo do usuario", max_length=30) 
    email: str = Field(title="email", description="E-mail do usuario", max_length=200) 
    phone: str = Field(title="phone", description="Telefone do usuario (DDI + DDD + NUMERO)", max_length=25) 
    birth_day: str = Field(title="birthDay", description="Timestamp da data de nascimento do usuario", max_length=10) 
    document: str = Field(title="document", description="Numero do documento do usuario", max_length=20)

    @validator('email')
    @is_email_valid
    def validate_email(cls, value: str) -> str:
        return value

    @validator('phone')
    @is_phone_valid
    def validate_phone(cls, value: str) -> str:
        return value

    @validator('document')
    @validate_personal_id
    def validate_id(cls, value):
        return value

    @validator('birth_day')
    @is_user_older_then_eighteen
    def validate_birthday(cls, value: str) -> str:
        return value

    def to_dict(self) -> dict:
        '''Return dictionary representing User document'''

        return {
            'id': self.id,
            'fullName': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'birthDay': self.birth_day,
            'document': self.document,
        }

    @staticmethod
    def from_dict(**kwargs) -> object:
        '''Instantiate class from dictionary of data'''
        try:
            data = {
                'id': kwargs['id'],
                'full_name': kwargs['fullName'],
                'email': kwargs['email'],
                'phone': kwargs['phone'],
                'birth_day': kwargs['birthDay'],
                'document': kwargs['document']
            }
            return User(**data)
        
        except ValueError as e:
            print(e)
