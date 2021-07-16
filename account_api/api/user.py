'''
TODO:
    [ ] POST ​/account Abre uma conta ATAR e retorna o objeto com o ID gerado
    [ ] GET ​/account​/{id} Retorna os dados do titular da conta
    [ ] PUT ​/account​/{id} Atualiza os dados do titular da conta
'''

from account_api.common.database import ModelManager
from account_api.models.user import User
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError

router = APIRouter()


@router.get('/account/{id}')
def get_user(id: str):
    '''Retrieve a user account'''

    try:
        manager = ModelManager(User, 'users')
        user = manager.get(id)

        return JSONResponse(user.to_dict())

    except ValidationError as e:
        err = e.errors()[0]
        if err['type'] == 'value_error.invaliddocument':
            raise HTTPException(400, f"Error on {err['loc'][0]}: {err['msg']}")


@router.put('/account/{id}')
def update_user(id: int):
    '''Update user account'''

    manager = ModelManager(User, 'users')
    manager.update(User, id, **{})

    return


@router.post('/account')
def create_user():
    '''Create user account'''

    manager = ModelManager(User, 'users')
    user = User({})
    manager.create()

    return