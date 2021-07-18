import os
import secrets
from fastapi.security import HTTPBasicCredentials
from account_api.common.database import ModelManager

class NotAuthorized(Exception):
    pass

def is_authorized(cred: HTTPBasicCredentials) -> bool:
    '''Check authorization'''

    try:
        if os.environ.get('ACCAPI_G_DEBUG') == 'true':
            assert secrets.compare_digest(cred.username, os.environ.get('ACCAPI_USERNAME'))
            assert secrets.compare_digest(cred.password, os.environ.get('ACCAPI_PASSWORD'))

        else:
            model = ModelManager('settings', test_mode=False)
            auth = model.get('auth')
            assert secrets.compare_digest(cred.username, auth['user'])
            assert secrets.compare_digest(cred.password, auth['password'])

        return True

    except:
        raise NotAuthorized()
