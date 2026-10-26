# ии подсказал что надо добавить return 0
class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print("Баллы начисляются только первым 100 участникам")
            return 0
        elif place < 1:
            print("Спортсмен не может занять нулевое или отрицательное место")
            return 0
        else:
            points = 101 - place
            return points               
class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print("Количество метров не может быть отрицательным")
            return 0
        else:
            points = meters*0.5
            return points   
class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self,meters,place):   
            points_for_meters = self.get_points_for_meters(meters)
            points_for_place = self.get_points_for_place(place)
            return points_for_meters + points_for_place
print(PointsForPlace.get_points_for_place(10))
print(PointsForMeters.get_points_for_meters(10))
total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 