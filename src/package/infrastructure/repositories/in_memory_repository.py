from src.package.domain import IRepository


class InMemoryRepository(IRepository):
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def list_all(self):
        return self.__items

    def get(self, index):
        if 0 <= index < len(self.__items):
            return self.__items[index]
        return None

    def remove(self, index):
        if 0 <= index < len(self.__items):
            return self.__items.pop(index)
        return None
