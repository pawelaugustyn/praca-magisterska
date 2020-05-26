from abc import ABCMeta, abstractmethod

class AbstractImageAction(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        """name property specifies action name"""

    @property
    @abstractmethod
    def params(self):
        """params property specifies needed input parameters"""

    @abstractmethod
    def execute(self, image, params):
        """Execute performs specific operation on input image"""

    @staticmethod
    def validate(params, needed_params):
        for param, validator in needed_params:
            if param not in params.keys() or not params[param]:
                raise ValueError(f"{param} parameter missing in input")
            if not validator(params[param]):
                raise ValueError(f"{param} has wrong type or value")
