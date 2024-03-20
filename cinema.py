# Cinema project

class Movie:
    def __init__(self, title, genre, duration):
        self.title = title
        self.genre = genre
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.genre}, {self.duration} min)"

class Cinema:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def show_movies(self):
        print(f"Movies currently playing at {self.name}:")
        for movie in self.movies:
            print(movie)

# Create some movies
avengers = Movie("Avengers: Endgame", "Action", 181)
joker = Movie("Joker", "Drama", 122)
harry_potter = Movie("Harry Potter and the Philosopher's Stone", "Fantasy", 152)

# Create a cinema
cinema = Cinema("City Cinema", "New York")

# Add movies to the cinema
cinema.add_movie(avengers)
cinema.add_movie(joker)
cinema.add_movie(harry_potter)

# Show the movies playing at the cinema
cinema.show_movies()
