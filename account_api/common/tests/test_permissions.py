import os
import unittest

from account_api.common.permissions import NotAuthorized, is_authorized


class Credential:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class TestPermissions(unittest.TestCase):
    
    def test_not_authorization(self):
        '''Test not authorized'''

        bad_cred1 = Credential('BADLOGON','BADPASWD')
        bad_cred2 = Credential('BADLOGON','')
        bad_cred3 = Credential('','BADPASWD')

        with self.assertRaises(NotAuthorized):
            is_authorized(bad_cred1)
            is_authorized(bad_cred2)
            is_authorized(bad_cred3)

    def test_authorized(self):
        '''Test authorized'''
        cred = Credential(os.environ.get('ACCAPI_USERNAME'),os.environ.get('ACCAPI_PASSWORD'))
        assert is_authorized(cred)
