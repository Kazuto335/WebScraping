from bs4 import *
import requests


conn = requests.get('https://news.ycombinator.com/news')
html_content = conn.text
# print(html_content)
soup = BeautifulSoup(html_content, 'html.parser')

links = soup.select(selector='.titleline a')
print(links)
# db = {item.getText(): {'Links': item.get('href')} for item in links}
count = 2
db = {}
for item in links:
    if links.index(item) in (0, 1) or count == 3:
        count -= 1
    else:
        db.update({item.getText(): item.get('href')})
        count += 1

print(db)





