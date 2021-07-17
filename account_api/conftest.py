import base64
import os

def make_valid_credential() -> str:
    credential = f"{os.environ.get('ACCAPI_USERNAME')}:{os.environ.get('ACCAPI_PASSWORD')}"
    credential_byte = credential.encode('ascii')
    b64_credential = base64.b64encode(credential_byte)
    
    return fr"Basic {b64_credential.decode('ascii')}"
