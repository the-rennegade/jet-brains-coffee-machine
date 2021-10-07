class Movie:
    all_movies = []

    def __init__(self, name, director, year):
        self.title = name
        self.director = director
        self.year = year
        Movie.all_movies.append(self)

# objects of the class Movie
titanic = Movie("Titanic", "James Cameron", 1997)
star_wars = Movie("Star Wars", "George Lucas", 1977)
fight_club = Movie("Fight Club", "David Fincher", 1999)
