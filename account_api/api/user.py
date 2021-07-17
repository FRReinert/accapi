from account_api.common.database import ModelManager
from account_api.common.permissions import NotAuthorized, is_authorized
from account_api.common.validators import DuplicatedValue, InvalidBirthday, InvalidDocument, InvalidEmail, InvalidPhone
from account_api.models.user import User
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter()
security = HTTPBasic(auto_error=False)

@router.get('/account/{id}')
async def get_user(id: str, credentials: HTTPBasicCredentials = Depends(security)):
    '''Retrieve a user account'''
   
    try:
        is_authorized(credentials)
        manager = ModelManager('users')
        user = User.from_dict(**manager.get(id))
        return JSONResponse(user.to_dict())
  
    except NotAuthorized as e:
        raise HTTPException(401, 'Nao autorizado', headers={"WWW-Authenticate": "Basic"})

    except Exception as e:
        raise HTTPException(404, f"Nao encontrado")

@router.post('/account')
async def create_user(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    '''Create user account'''
   
    try:
        is_authorized(credentials)
        query_data = await request.json()
        manager = ModelManager('users')
        user = User.from_dict(**query_data)
        user.validate_fields()
        user.validate_unique(manager)
        return manager.create(user)

    except InvalidPhone as e:
        raise HTTPException(400, str(e))

    except InvalidBirthday as e:
        raise HTTPException(400, str(e))

    except NotAuthorized as e:
        raise HTTPException(401, 'Nao autorizado', headers={"WWW-Authenticate": "Basic"})
    
    except InvalidDocument as e:
        raise HTTPException(406, str(e))

    except InvalidEmail as e:
        raise HTTPException(406, str(e))
    
    except DuplicatedValue as e:
        raise HTTPException(409, str(e))
    
    except Exception as e:
        raise HTTPException(400, 'Dados invalidos: %s' % str(e))

@router.put('/account/{id}')
async def update_user(id: str, request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    '''Update user account'''

    try:
        is_authorized(credentials)
        query_data = await request.json()
        manager = ModelManager('users')
        data = manager.get(id) | query_data  # Bitwise OR
        user = User.from_dict(**data)
        user.validate_fields()

        return manager.update(id, user)

    except InvalidPhone as e:
        raise HTTPException(400, str(e))

    except InvalidBirthday as e:
        raise HTTPException(400, str(e))

    except NotAuthorized as e:
        raise HTTPException(401, 'Nao autorizado', headers={"WWW-Authenticate": "Basic"})
    
    except InvalidDocument as e:
        raise HTTPException(406, str(e))

    except InvalidEmail as e:
        raise HTTPException(406, str(e))
    
    except DuplicatedValue as e:
        raise HTTPException(409, str(e))
    
    except Exception as e:
        raise HTTPException(400, 'Dados invalidos: %s' % str(e))
    