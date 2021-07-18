import unittest

from account_api.models.user import User
from account_api.common.validators import *


class TestUserModel(unittest.TestCase):
    
    def test_create_user_methods(self):
        '''Create user model'''

        new_user = User(full_name="Nome Teste", email="teste@domain.com", phone="554733820000", birth_day="01/01/1990", document="86717126051")
        user_dict = {"fullName": "Nome Teste", "email": "teste@domain.com", "phone": "554733820000", "birthDay": "01/01/1990", "document": "86717126051"}
        assert new_user.to_dict() == user_dict

    def test_converto_to_dict(self):
        '''Create user model'''

        new_user = User(full_name="Nome Teste", email="teste@domain.com", phone="554733820000", birth_day="01/01/1990", document="86717126051")
        user_dict = {"fullName": "Nome Teste", "email": "teste@domain.com", "phone": "554733820000", "birthDay": "01/01/1990", "document": "86717126051"}
        assert new_user.to_dict() == user_dict

    def test_create_user_model_from_dict(self):
        '''Create user model from dict'''
        user_dict = {"fullName": "Nome Teste", "email": "teste@domain.com", "phone": "554733820000", "birthDay": "01/01/1990", "document": "86717126051"}
        user = User.from_dict(**user_dict)
        assert user.to_dict() == user_dict

    def test_user_field_convertion_to_db(self):
        user_dict = {"fullName": "Nome Teste", "email": "teste@domain.com", "phone": "554733820000", "birthDay": "01/01/1990", "document": "86717126051"}
        user = User.from_dict(**user_dict)
        assert user.full_name == "Nome Teste"
        assert user.email == "teste@domain.com"
        assert user.phone == "554733820000"
        assert user.birth_day == "01/01/1990"
        assert user.document == "86717126051"
