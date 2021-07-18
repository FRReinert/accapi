from account_api.common.database import ModelManager
from account_api.models.user import User
import unittest


class TestDatabase(unittest.TestCase):

    def test_manager_create(self):
        '''Test creation'''

        manager = ModelManager('users', test_mode=True)
        user_doc = manager.create(User(full_name="Nome Teste", email="teste.20@domain.com", phone="554733820000", birth_day="01/01/1990", document="47506433001"))
        assert user_doc.id
        assert user_doc.full_name == "Nome Teste"
        assert user_doc.email == "teste.20@domain.com" 
        assert user_doc.phone == "554733820000"
        assert user_doc.birth_day == "01/01/1990"
        assert user_doc.document == "47506433001"
    
    def test_manager_get(self):
        '''Test get documenet'''

        manager = ModelManager('users', test_mode=True)
        user_doc = manager.create(User(full_name="Nome Teste", email="teste.21@domain.com", phone="554733820000", birth_day="01/01/1990", document="40320277062"))
        user_get = manager.get(user_doc.id)
        assert user_doc.id == user_get['id']

    def test_manager_filter(self):
        '''Test filter documents'''

        manager = ModelManager('users', test_mode=True)
        manager.create(User(full_name="Nome Teste", email="teste.22@domain.com", phone="554733820000", birth_day="01/01/1990", document="58484958078"))
        user_filter = manager.filter('email', '==', 'teste.22@domain.com')
        assert len(user_filter) > 0

    def test_manager_update(self):
        '''Test update document'''

        manager = ModelManager('users', test_mode=True)
        user = manager.create(User(full_name="Nome Teste", email="teste.23@domain.com", phone="554733820000", birth_day="01/01/1990", document="70610161083"))
        new_user = User.from_dict(**{'fullName': "Nome Teste 2", 'email': "teste.24@domain.com", 'phone': "554733820022", 'birthDay': "01/01/1991", 'document': "27662641082"})
        user_updated = manager.update(user.id, new_user)

        assert user_updated.full_name == 'Nome Teste 2'
        assert user_updated.email == 'teste.24@domain.com'
        assert user_updated.phone == '554733820022'
        assert user_updated.birth_day == '01/01/1991'
        assert user_updated.document == '27662641082'
