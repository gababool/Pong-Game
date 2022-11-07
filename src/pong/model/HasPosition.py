

from abc import abstractmethod, ABC


class HasPosition(ABC):
    """
        Contract for anything that can be positioned in the world.

        NOTE: This must be fulfilled by any object the GUI shall render
    """
    @abstractmethod
    def get_x(self):      # Min x and y is upper left corner (y-axis pointing down)
        raise NotImplementedError

    @abstractmethod
    def get_y(self):
        raise NotImplementedError

    @abstractmethod
    def get_width(self):
        raise NotImplementedError

    @abstractmethod
    def get_height(self):
        raise NotImplementedError
