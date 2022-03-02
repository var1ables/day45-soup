from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies = response.text

soup = BeautifulSoup(movies, "html.parser")

all_movies = soup.find_all(name='img', class_="jsx-952983560")
films = []
for i in all_movies:
    film = i.get('alt')
    films.append(film)

cut_films = films[12:]
films = cut_films[::-1]

with open(file='movies.txt', mode='w') as file:
    for film in films:
        number = films.index(film)+1
        file.write(f'{number}) {film}\n')

