import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
all_movies = soup.select('span:has(h2 > strong)')

movies = list(all_movies)
movies.reverse()


with open("top_movies.txt","a") as file:
    for movie in movies:
        file.write(movie.getText())

