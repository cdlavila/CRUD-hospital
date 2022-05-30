from abc import ABC, abstractmethod


class ICrud(ABC):
    @abstractmethod
    def find(self, **kwargs):
        raise NotImplementedError
