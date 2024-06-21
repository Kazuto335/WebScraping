import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
conn = requests.get(url=URL)
html_content = conn.text

# print(html_content)

soup = BeautifulSoup(html_content, 'html.parser')

list_html = soup.select(selector='.entity-info-items__list ul li a')
list_html = [item.text for item in list_html]


