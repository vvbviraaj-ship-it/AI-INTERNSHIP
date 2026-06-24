import requests
from bs4 import Beautifulsoup4

url = "https://pokemondb.net/pokedex/all"

page = requests.get(url)

soup = BeautifulSoup4(page.text, "html.parser")

print(soup.title.text)