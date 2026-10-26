# Сначала сделала сам и код работал, но решила что странно выгдядит, по шагам с помощью ии поправила к нормальному виду
class Movies:
    def __init__(self):
        self.movies = []
    def add_movie(self, movie):
        self.movies.append(movie)
class Comedy(Movies):
    def add_movie(self,movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'   
class Drama(Movies):
    def add_movie(self,movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'        
comedy = Comedy()
result_comedy = comedy.add_movie('Большой куш')
print(result_comedy) 
drama = Drama()
result_drama = drama.add_movie('Оружейный барон')
print(result_drama)

