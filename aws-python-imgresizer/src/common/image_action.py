from abc import ABCMeta, abstractmethod

class AbstractImageAction(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, image, params):
        """Execute performs specific operation on input image"""
