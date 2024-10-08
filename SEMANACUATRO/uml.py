class Director:
    def __init__(self, name: str, nationality: str):
        self.name = name
        self.nationality = nationality
        self.movies = []

    def agregar_movie(self, movie):
        self.movies.append(movie)

    def mostrar_informacion(self):
        print(f"Director: {self.name}, Nacionalidad: {self.nationality}")
        print("Películas dirigidas:")
        for movie in self.movies:
            print(f"- {movie.title}")

class Movie:
    def __init__(self, title: str, genre: str, duration: int, director: Director):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.director = director
        director.agregar_movie(self)

    def mostrar_informacion(self):
        print(f"Título: {self.title}, Género: {self.genre}, Duración: {self.duration} minutos")
        print(f"Director: {self.director.name}")

class Cinema:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.billboard = []

    def agregar_movie(self, movie: Movie):
        self.billboard.append(movie)

    def mostrar_informacion(self):
        print(f"Cine: {self.name}, Dirección: {self.address}")
        print("Cartelera:")
        for movie in self.billboard:
            movie.mostrar_informacion()

# EJ:
director1 = Director("Mel Gibson", "Australiano")
movie1 = Movie("Braveheart", "Drama Histórico", 178, director1)
movie2 = Movie("Hacksaw Ridge", "Bélico", 139, director1)

director2 = Director("Quentin Tarantino", "Estadounidense")
movie3 = Movie("Pulp Fiction", "Crimen", 154, director2)
movie4 = Movie("Inglourious Basterds", "Bélico", 153, director2)

cine1 = Cinema("Cinemark", "limonar")
cine1.agregar_movie(movie1)
cine1.agregar_movie(movie2)
cine1.agregar_movie(movie3)
cine1.agregar_movie(movie4)

cine1.mostrar_informacion()
director1.mostrar_informacion()
director2.mostrar_informacion()
