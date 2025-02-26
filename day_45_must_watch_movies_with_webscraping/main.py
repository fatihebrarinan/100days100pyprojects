from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
top_100 = [item.getText() for item in soup.select("h2 strong")]
top_100.reverse()
with open("movies.txt", "w") as file:
    for movie in top_100:
        file.write(movie + "\n")

