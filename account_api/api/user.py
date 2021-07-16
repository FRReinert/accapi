'''
TODO:
    [ ] POST ​/account Abre uma conta ATAR e retorna o objeto com o ID gerado
    [ ] GET ​/account​/{id} Retorna os dados do titular da conta
    [ ] PUT ​/account​/{id} Atualiza os dados do titular da conta
'''

from account_api.common.database import ModelManager
from account_api.common.permissions import is_authorized
from account_api.models.user import User
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import ValidationError

router = APIRouter()
security = HTTPBasic()

@router.get('/account/{id}')
async def get_user(id: str, credentials: HTTPBasicCredentials = Depends(security)):
    '''Retrieve a user account'''
   
    try:
        manager = ModelManager(User, 'users')
        user = manager.get(id)
        return JSONResponse(user.to_dict())

    except ValidationError as e:
        err = e.errors()[0]
        if err['type'] == 'value_error.invaliddocument':
            raise HTTPException(status_code=404, detail=f"Erro ao validar Documento")
    
    except Exception as e:
        raise HTTPException(404, f"Não encontrado: {type(e)}")

@router.post('/account')
async def create_user(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    '''Create user account'''
   
    try:
        user_dict = await request.json()
        manager = ModelManager(User, 'users')
        user = User.from_dict(**manager.create(user_dict))
    
    except ValidationError as e:
        err = e.errors()
        raise HTTPException(400, f"Erro ao criar documento {err.loc}: {err.msg}")
    
    return user.id

@router.put('/account/{id}')
async def update_user(id: int):
    '''Update user account'''

    manager = ModelManager(User, 'users')
    manager.update(User, id, **{})

    return
