from abc import ABCMeta, abstractclassmethod
from typing import Any, Dict

from injector import inject


class ICache(metaclass=ABCMeta):

    @abstractclassmethod
    def get(self, key: str):
        pass

    @abstractclassmethod
    def set(self, key: str, value: Any):
        pass


class DictCache(ICache):

    def __init__(self):
        self.content = {'key': 'value'}
    
    def get(self, key: str) -> Any:
        return self.content.get(key, None)
    
    def set(self, key: str, value: Any) -> None:
        self.content[key] = value
