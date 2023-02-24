from bs4 import BeautifulSoup
import requests
import html5lib
import csv

csv_file = open("congress_cats.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["title", "item description", "hyperlink", "contributor", "date"])

pages = 5

for page_num in range (1, pages+1):
    congress = requests.get(f"https://www.loc.gov/search/?q=cats&sp={page_num}").text
    soup = BeautifulSoup(congress, "lxml")
    
    for item in soup.find_all("li", class_="item"):
        # These are the two straightforward elements to find
        title = item.find("span", class_="item-description-title").a.text.strip()
        hyperlink = item.find("span", class_="item-description-title").a["href"].strip()
        
        # These elements may or may not exist
        try:
            description = item.find("span", class_="item-description-abstract").text.strip()
        except AttributeError:
            description = "N/A"
        
        try:
            date = item.find("li", class_="date").span.text.strip(": ")
        except AttributeError:
            date = "N/A"
        
        try:
            contributor = item.find("li", class_="contributor").span.text.strip()
        except AttributeError:
            contributor = "N/A"
        
        
        csv_writer.writerow([title, description, hyperlink, contributor, date])
        print(title, description, hyperlink)

csv_file.close()