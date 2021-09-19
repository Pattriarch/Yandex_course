from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
            self.longitude - other.longitude)
        return 6371 * acos(cos_d)


class City(Point):
    def __init__(self, latitude, longitude, name, population):
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")


class Mountain(Point):
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height

    def show(self):
        print(f"Высота горы {self.name} - {self.height} м.")


Moscow = City(55.751244, 37.618423, 'Moscow', 11_920_000)
Everest = Mountain(27.986065, 86.922623, 'Everest', 8849)

print(f'Расстояние от Москвы до Эвереста: {Moscow.distance(Everest)}')
