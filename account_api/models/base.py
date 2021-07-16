from abc import ABC, abstractstaticmethod
from typing import Any

from pydantic.main import BaseModel


class IModelManager(ABC):

    model: BaseModel

    @abstractstaticmethod
    @staticmethod
    def get() -> Any:
        '''Get Model object'''
        pass

    @abstractstaticmethod
    @staticmethod
    def filter() -> Any:
        '''Get Model object'''
        pass

    @abstractstaticmethod
    @staticmethod
    def create() -> Any:
        '''Create Model object'''
        pass

    @abstractstaticmethod
    @staticmethod
    def update() -> Any:
        '''Update Model object'''
        pass

    @abstractstaticmethod
    @staticmethod
    def delete() -> Any:
        '''Delete Model object'''
        pass