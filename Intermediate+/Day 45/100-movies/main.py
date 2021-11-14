import requests
from bs4 import BeautifulSoup
from random import choice

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def scrape_top_movies():
    response = requests.get(url=URL)
    movies_web_page = response.text

    soup = BeautifulSoup(movies_web_page, 'html.parser')
    movies = soup.find_all(name="h3", class_="title")
    top_100_movies = [movie_tag.getText() for movie_tag in movies[::-1]]
    with open("movies.txt", mode="w") as movies_file:
        for i, movie in enumerate(top_100_movies):
            line = f"{movie}\n" if i < len(top_100_movies) - 1 else movie
            movies_file.write(line)


def generate_movie_suggestion():
    with open("movies.txt") as movies_file:
        movies = movies_file.readlines()
        while True:
            suggestion = choice(movies)
            print(f"We recommend that you try out...\n{suggestion}")
            if input("Have you seen this movie ('Y' or 'N')? ").upper() != 'Y':
                print("Great! Enjoy the movie!")
                break


if __name__ == "__main__":
    generate_movie_suggestion()
