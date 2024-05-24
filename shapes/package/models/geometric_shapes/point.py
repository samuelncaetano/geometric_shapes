from shapes.package.models.geometric_shape import GeometricShape


class Point(GeometricShape):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def calculate_area(self):
        return 0
