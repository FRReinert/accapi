import unittest
import datetime

from account_api.common.validators import *
from account_api.common.database import ModelManager
from account_api.models.user import User


class TestValidators(unittest.TestCase):
    
    def test_valid_document(self):
        '''Test Valid documents'''
        assert is_document_valid('81816793000') == True
        assert is_document_valid('58242129029') == True
        assert is_document_valid('94207979026') == True

    def test_invalid_documents(self):
        '''Test invalid documents'''

        with self.assertRaises(InvalidDocument):
            is_document_valid('1111111111')  # 10 chars
            is_document_valid('111111111112') # 12 chars
            is_document_valid('11111111111') # same number
            is_document_valid('02924960000')  # wrong digit 1
            is_document_valid('02924960011')  # wrong digit 2
    
    def test_valid_birthday_majority(self):
        '''Valid Majority dates'''
        assert is_user_older_then_eighteen('01/01/1970')
        assert is_user_older_then_eighteen('31/12/1986')
        assert is_user_older_then_eighteen('24/01/1990')

    def test_invalidbirthday_majority(self):
        '''Test invalid majority from birth day input'''

        eighteen_from_now = datetime.datetime.today() - datetime.timedelta(days=(365.24 * 18))

        # The date conversion based in days is not very accurate
        # So test will be run with 3 days after birthday at minimum
        date_1 = datetime.date.strftime(eighteen_from_now + datetime.timedelta(days=(3)), '%d/%m/%Y')
        date_2 = datetime.date.strftime(eighteen_from_now + datetime.timedelta(days=(30)), '%d/%m/%Y')
        date_3 = datetime.date.strftime(eighteen_from_now + datetime.timedelta(days=(300)), '%d/%m/%Y')

        with self.assertRaises(InvalidBirthday):
            is_user_older_then_eighteen(date_1)
            is_user_older_then_eighteen(date_2)
            is_user_older_then_eighteen(date_3)

    def test_valid_email(self):
        '''Test valid emails'''

        assert is_email_valid('test.surname@domain.com') == True
        assert is_email_valid('test@domain.com') == True

    def test_invalid_email(self):
        '''Test nvalid email'''

        with self.assertRaises(InvalidEmail):
            is_email_valid('@domain.com')
            is_email_valid('test@domain')
            is_email_valid('domainonly')
            is_email_valid('domain.com')

    def test_valid_phone(self):
        '''Test Valid phone numbers'''

        assert is_phone_valid('55544433332222') == True
        assert is_phone_valid('554433332222') == True

    def test_invalid_phone(self):
        '''Test Invalid phones'''

        with self.assertRaises(InvalidPhone):
            is_phone_valid('A554433332222')
            is_phone_valid('55554433332222')
            is_phone_valid('33332222')
            is_phone_valid('+554733332222')
            is_phone_valid('55 47 3333 2222')
            is_phone_valid('3333 2222')

    def test_valid_unifque_email(self):
        '''Test valid unique emails'''

        manager = ModelManager('users', test_mode=True)
        
        manager.create(User(full_name="Nome Teste", email="teste.01@domain.com", phone="554733820000", birth_day="01/01/1990", document="78496584003"))
        manager.create(User(full_name="Nome Teste", email="teste.02@domain.com", phone="554733820000", birth_day="01/01/1990", document="23747232086"))
        manager.create(User(full_name="Nome Teste", email="teste.03@domain.com", phone="554733820000", birth_day="01/01/1990", document="37481755078"))

        assert unique_field_valid(manager, 'email', 'teste.04@domain.com') == True

    def test_invalid_unique_email(self):
        '''Test invalid unique emails'''
        
        manager = ModelManager('users', test_mode=True)

        manager.create(User(full_name="Nome Teste", email="teste.05@domain.com", phone="554733820000", birth_day="01/01/1990", document="25067960027"))
        manager.create(User(full_name="Nome Teste", email="teste.06@domain.com", phone="554733820000", birth_day="01/01/1990", document="35971618040"))
        manager.create(User(full_name="Nome Teste", email="teste.07@domain.com", phone="554733820000", birth_day="01/01/1990", document="34981501030"))

        with self.assertRaises(DuplicatedValue):
            unique_field_valid(manager, 'email', 'teste.05@domain.com')
            unique_field_valid(manager, 'email', 'teste.06@domain.com')
            unique_field_valid(manager, 'email', 'teste.07@domain.com')
