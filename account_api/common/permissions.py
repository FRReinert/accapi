import os
import base64
import secrets
from fastapi.security import HTTPBasicCredentials

def is_authorized(cred: HTTPBasicCredentials) -> bool:
    '''Check authorization'''
    assert secrets.compare_digest(cred.username, os.environ.get('ACCAPI_USERNAME'))
    assert secrets.compare_digest(cred.password, os.environ.get('ACCAPI_PASSWORD'))

    return True
