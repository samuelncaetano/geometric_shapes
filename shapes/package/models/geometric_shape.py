from abc import ABC, abstractmethod


class GeometricShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    # @abstractmethod
    # def calculate_perimeter(self):
    #     pass

    # @abstractmethod
    # def contains_point(self):
    #     pass

    # @abstractmethod
    # def to_move(self):
    #     pass
