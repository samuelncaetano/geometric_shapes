# pylint: disable = W1514, R1705
import json
from pathlib import Path
from src.package import Point, LineSegment, Rectangle, Circle, Triangle, IRepository


class JsonRepository(IRepository):
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self.file_path.write_text(json.dumps([]))
        self.load()

    def load(self):
        with self.file_path.open("r") as file:
            self.items = json.load(file)

    def save(self):
        with self.file_path.open("w") as file:
            json.dump(self.items, file)

    def add(self, item):
        self.items.append(item.to_dict())
        self.save()

    def list_all(self):
        return [self.dict_to_object(obj) for obj in self.items]

    def get(self, index):
        if 0 <= index < len(self.items):
            return self.dict_to_object(self.items[index])
        return None

    def remove(self, index):
        if 0 <= index < len(self.items):
            removed_item = self.items.pop(index)
            self.save()
            return self.dict_to_object(removed_item)
        return None

    def dict_to_object(self, obj_dict):
        shape_type = obj_dict["type"]
        if shape_type == "Point":
            return Point.from_dict(obj_dict)
        elif shape_type == "LineSegment":
            return LineSegment.from_dict(obj_dict)
        elif shape_type == "Circle":
            return Circle.from_dict(obj_dict)
        elif shape_type == "Rectangle":
            return Rectangle.from_dict(obj_dict)
        elif shape_type == "Triangle":
            return Triangle.from_dict(obj_dict)
        else:
            raise ValueError(f"Tipo de forma desconhecido: {shape_type}")
