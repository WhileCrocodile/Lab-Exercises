from bs4 import BeautifulSoup
import requests
import html5lib
import csv

# Isolate the title, the date of release, and one other element of your choosing. (3pts)
# Put the data into a csv. (2pts)

imbd = requests.get("https://www.imdb.com/list/ls055592025/").text
soup = BeautifulSoup(imbd, "lxml")

csv_file = open("imbd_movies.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["title", "year of release", "rating"])

for movie in soup.find_all("div", class_="lister-item mode-detail"):
    title = movie.find("h3", class_="lister-item-header").a.text
    released = movie.find("span", class_="lister-item-year text-muted unbold").text[1:5] #gets rid of parentheses
    rating = movie.find("span", class_="ipl-rating-star__rating").text
    csv_writer.writerow([title, released, rating])