import os
import secrets
from fastapi.security import HTTPBasicCredentials

class NotAuthorized(Exception):
    pass

def is_authorized(cred: HTTPBasicCredentials) -> bool:
    '''Check authorization'''

    try:
        assert secrets.compare_digest(cred.username, os.environ.get('ACCAPI_USERNAME'))
        assert secrets.compare_digest(cred.password, os.environ.get('ACCAPI_PASSWORD'))
        return True

    except:
        raise NotAuthorized()
