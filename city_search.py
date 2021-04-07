from math import sin, cos, sqrt, atan2, radians

R = 6373.0


class CityDistance():
    def __init__(self, cord1, cord2):
        self.lat1 = radians(float(cord1[0].split(" ")[0]))
        self.long1 = radians(float(cord1[1].lstrip().split(" ")[0]))
        self.lat2 = radians(float(cord2[0].split(" ")[0]))
        self.long2 = radians(float(cord2[1].lstrip().split(" ")[0]))

    def get_distance(self):
        dlon = self.long2 - self.long1
        dlat = self.lat2 - self.lat1
        a = sin(dlat / 2)**2 + cos(self.lat1) * cos(self.lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return round(distance, 3)


if __name__ == "__main__":
    cord1 = input("City 1:")
    cord2 = input("City 2:")
    city_obj = CityDistance(cord1.split(","), cord2.split(","))
    print("City 1 and City 2 are {} km apart".format(city_obj.get_distance()))
