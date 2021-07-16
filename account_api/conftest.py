import pytest 

import base64
import os

from account_api.common.database import ModelManager
from account_api.models.user import User


def make_valid_credential() -> str:
    credential = f"{os.environ.get('ACCAPI_USERNAME')}:{os.environ.get('ACCAPI_PASSWORD')}"
    credential_byte = credential.encode('ascii')
    b64_credential = base64.b64encode(credential_byte)
    
    return fr"Basic {b64_credential.decode('ascii')}"

#  Fixture for users_test collection
@pytest.fixture(scope="function")
def clear_users_test_collection(id: str):
    yield
    user_manager = ModelManager(User, 'users_test')
    user_manager.delete(id)
