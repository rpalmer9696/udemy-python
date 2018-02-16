import requests
from bs4 import BeautifulSoup

data = requests.get("https://pythonhow.com/example.html")
c = data.content

soup = BeautifulSoup(c, "html.parser")
all_divs = soup.find_all("div", {"class": "cities"})

cities = [x.text for i in all_divs for x in (i.find_all("h2"))]
print(cities)
