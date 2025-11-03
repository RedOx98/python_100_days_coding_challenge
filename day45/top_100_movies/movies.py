import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
article_wp =response.text

movies_article = BeautifulSoup(article_wp, "html.parser")
# movies = []
movie_names = [movies.getText() for movies in movies_article.find_all(name="h3", class_="title")]

# Reverse order because the list is in reverse (100 → 1)
movie_names.reverse()

try:
    with open("movies.txt", "w", encoding="utf-8") as file:
        for movie in movie_names:
            file.write(f"{movie}\n")
            # file.write("\\n")
except UnicodeEncodeError as e:
    print(e)

print("✅ Movies successfully written to movies.txt")