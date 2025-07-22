
from abc import ABC, abstractmethod

class BaseSecurityModule(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def run_analysis(self):
        pass

if __name__ == '__main__':
    pass
