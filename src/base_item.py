from abc import ABC, abstractmethod


class BaseItem(ABC):

    @abstractmethod
    def __str__(self):
        pass
