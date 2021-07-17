from account_api.models.user import User
from account_api.common.database import ModelManager
from account_api.main import app
from account_api.conftest import *
from fastapi.testclient import TestClient

class TestCreateUser():

    client = TestClient(app)
    user_manager = ModelManager(User, 'users', test_mode=True)

    def test_valid_user(self):
        valid_data = {
            "fullName": "mock_teste_01", "phone": "554733820110",
            "email": "mock1@bol.com.br", "document": "86352786073",
            "birthDay": "15/07/1968"
        }
        cred = make_valid_credential()
        response = self.client.post('/account', headers={'Authorization': cred}, json=valid_data)
        assert response.status_code == 200

    def test_valid_user_with_bad_credential(self):
        valid_data = {
            "fullName": "mock_teste_02", "phone": "554733820110",
            "email": "mock2@bol.com.br", "document": "74394038006",
            "birthDay": "15/07/1968"}
        response = self.client.post('/account', headers={'Authorization': 'Basic NOWAYTORUN'}, json=valid_data)
        assert response.status_code == 401
        assert response.json() == {'detail': 'Invalid authentication credentials'}

    def test_invalid_phone_a(self):
        valid_data = {
            "fullName": "mock_teste_03", "phone": "AA4733820110",
            "email": "mock3@bol.com.br", "document": "20367828090",
            "birthDay": "15/07/1968"}
        cred = make_valid_credential()
        response = self.client.post('/account', headers={'Authorization': cred}, json=valid_data)
        assert response.status_code == 400
        assert response.json() == {'detail': 'Dados invalidos'}

    def test_invalid_phone_b(self):
        valid_data = {
            "fullName": "mock_teste_04", "phone": "55 47 33820110",
            "email": "mock4@bol.com.br", "document": "07731103056",
            "birthDay": "15/07/1968"}
        cred = make_valid_credential()
        response = self.client.post('/account', headers={'Authorization': cred}, json=valid_data)
        assert response.status_code == 400
        assert response.json() == {'detail': 'Dados invalidos'}


class TestGetUser:

    client = TestClient(app)

    def test_no_id_without_cred_account_get(self):
        '''Test /account without credentials'''

        cred = make_valid_credential()
        response = self.client.get("/account", headers={'Authorization': cred})
        assert response.status_code == 405
        assert response.json() == {"detail":"Method Not Allowed"}

    def test_no_id_with_cred_account_get(self):
        '''Test /account with valid credentials'''

        response = self.client.get("/account")
        assert response.status_code == 405
        assert response.json() == {"detail":"Method Not Allowed"}

    def test_invalid_id_with_valid_cred_account_get(self):
        '''Test /account/{id} with invalid ID and VALID credential'''

        cred = make_valid_credential()
        response = self.client.get("/account/anything", headers={'Authorization': cred})
        assert response.status_code == 404
        assert response.json() == {"detail":"Não encontrado"}

    def test_invalid_id_with_invalid_cred_account_get(self):
        '''Test /account/{id} with invalid ID and INVALID credential'''

        response = self.client.get("/account/anything", headers={'Authorization': 'Basic NOWAYTORUN'})
        assert response.status_code == 401
        assert response.json() == {'detail': 'Invalid authentication credentials'}

    def test_invalid_id_without_cred_account_get(self):
        '''Test /account/{id} with invalid ID and NO credential'''

        response = self.client.get("/account/anything")
        assert response.status_code == 401
        assert response.json() == {"detail":"Not authenticated"}

    def test_found_id_with_credential(self):
        '''Test /account/{id} with valid ID and valid credential'''

        cred = make_valid_credential()
        response = self.client.get("/account/a2d0NMnD5lUwibiv6Tix", headers={'Authorization': cred})
        assert response.status_code == 200
        assert response.json() == {"id":"a2d0NMnD5lUwibiv6Tix","fullName":"Fabricio Roberto Reinert","email":"fabricio.reinert@live.com","phone":"5547991675536","birthDay":"16/07/2003","document":"07437514931"}
