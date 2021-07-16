from abc import ABC, abstractmethod, abstractstaticmethod

class IModel(ABC):
    
    @abstractstaticmethod
    def from_dict(**kwargs) -> object:
        '''Instantiate a model from a dictionary'''
        pass

    @abstractmethod
    def to_dict() -> dict:
        '''Cast the model as dictionary'''
        pass
