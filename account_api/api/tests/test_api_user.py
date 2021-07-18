from account_api.models.user import User
from account_api.common.database import ModelManager
from account_api.main import app
from account_api.conftest import *
from fastapi.testclient import TestClient
import unittest


class TestUserPOST(unittest.TestCase):

    client = TestClient(app)

    def test_valid_user_with_bad_credential(self):
        valid_data = {
            "fullName": "mock_teste_02", "phone": "554733820110",
            "email": "mock2@bol.com", "document": "74394038006",
            "birthDay": "15/07/1968"}
        response = self.client.post('/account', headers={'Authorization': 'Basic NOWAYTORUN'}, json=valid_data)
        assert response.status_code == 401
        assert response.json() == {'detail': 'Invalid authentication credentials'}

    def test_invalid_phone(self):
        valid_data = {
            "fullName": "mock_teste_03", "phone": "AA4733820110",
            "email": "mock3@bol.com", "document": "20367828090",
            "birthDay": "15/07/1968"}
        cred = make_valid_credential()
        response = self.client.post('/account', headers={'Authorization': cred}, json=valid_data)
        assert response.status_code == 400
        assert response.json() == {'detail': 'Informar apenas numeros'}

    def test_invalid_email(self):
        valid_data = {
            "fullName": "mock_teste_03", "phone": "554733820110",
            "email": "mock1.invalid.com", "document": "24035987042",
            "birthDay": "15/07/1968"}
        cred = make_valid_credential()
        response = self.client.post('/account', headers={'Authorization': cred}, json=valid_data)
        assert response.status_code == 406
        assert response.json() == {'detail': 'E-mail invalido'}

    def test_used_email(self):
        valid_data = {
            "fullName": "mock_teste_03", "phone": "554733820110",
            "email": "mock1@bol.com", "document": "24035987042",
            "birthDay": "15/07/1968"}
        cred = make_valid_credential()
        response = self.client.post('/account', headers={'Authorization': cred}, json=valid_data)
        assert response.status_code == 409
        assert response.json() == {'detail': 'email ja cadastrado'}

class TestUserGET(unittest.TestCase):

    client = TestClient(app)

    def test_id_with_invalid_Credential(self):
        '''Test /account/{id} with invalid ID and VALID credential'''

        cred = make_valid_credential()
        response = self.client.get("/account/anything", headers={'Authorization': cred})
        assert response.status_code == 404
        assert response.json() == {'detail': 'Nao encontrado'}

    def test_id_without_credential(self):
        '''Test /account/{id} with invalid ID and NO credential'''

        response = self.client.get("/account/anything")
        assert response.status_code == 401
        assert response.json() == {'detail': 'Nao autorizado'}

    def test_id_with_credential(self):
        '''Test /account/{id} with valid ID and valid credential'''

        cred = make_valid_credential()

        valid_data = {"id": "GN6h5DygDDMES7bhFVFf", "fullName": "mock_teste_01", "email":"mock1@bol.com",
            "phone":"554733820110","birthDay":"15/07/1968","document":"81370006071"}

        response = self.client.get("/account/GN6h5DygDDMES7bhFVFf", headers={'Authorization': cred})

        assert response.status_code == 200
        assert response.json() == valid_data

class TestUserPUT(unittest.TestCase):

    client = TestClient(app)

    def test_user_updated(self):
        cred = make_valid_credential()

        valid_data = {"id": "GN6h5DygDDMES7bhFVFf", "fullName": "mock_teste_01", "email":"mock1@bol.com",
            "phone":"554733820110","birthDay":"15/07/1968","document":"81370006071"}

        response = self.client.put("/account/GN6h5DygDDMES7bhFVFf", headers={'Authorization': cred})

        # assert response.status_code == 204
        assert response.json() == valid_data

    def test_invalid_phone(self):
        valid_data = {
            "fullName": "mock_teste_03", "phone": "AA4733820110",
            "email": "mock3@bol.com", "document": "20367828090",
            "birthDay": "15/07/1968"}
        cred = make_valid_credential()
        response = self.client.post('/account', headers={'Authorization': cred}, json=valid_data)
        assert response.status_code == 400
        assert response.json() == {'detail': 'Informar apenas numeros'}

    def test_not_authorized(self):
        valid_data = {
            "fullName": "mock_teste_03", "phone": "554733820110",
            "email": "mock1@bol.com", "document": "24035987042",
            "birthDay": "15/07/1968"}
        response = self.client.put("/account/GN6h5DygDDMES7bhFVFf", json=valid_data)
        assert response.status_code == 401
        assert response.json() == {'detail': 'Nao autorizado'}

    def test_invalid_email(self):
        valid_data = {
            "fullName": "mock_teste_03", "phone": "554733820110",
            "email": "mock1.invalid.com", "document": "24035987042",
            "birthDay": "15/07/1968"}
        cred = make_valid_credential()
        response = self.client.put('/account/GN6h5DygDDMES7bhFVFf', headers={'Authorization': cred}, json=valid_data)
        assert response.status_code == 406
        assert response.json() == {'detail': 'E-mail invalido'}

    def test_email_used(self):
        valid_data = {
            "fullName": "mock_teste_03", "phone": "554733820110",
            "email": "mock1@bol.com", "document": "24035987042",
            "birthDay": "15/07/1968"}
        cred = make_valid_credential()
        response = self.client.put('/account/GN6h5DygDDMES7bhFVFf', headers={'Authorization': cred}, json=valid_data)
        assert response.status_code == 406
        assert response.json() == {'detail': 'E-mail invalido'}