__version__ = '0.0.1'
__author__ = 'Fabricio Roberto Reinert'
__email__ = 'Fabricio Reinert <fabricio.reinert@live.com>'

from fastapi import FastAPI
from account_api.api import user
import os

app = FastAPI()
app.include_router(user.router)
