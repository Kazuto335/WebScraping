from bs4 import *
import requests
from pandas import *

conn = requests.get(url='http://www.hubertiming.com/results/2017GPTR10K')
html_content = conn.text
# print(html_content)

soup = BeautifulSoup(html_content, 'html.parser')
heading = soup.find_all('th')
list_ = [text.getText() for text in heading]
# print(list_)

values = soup.select(selector='#individualResults tbody tr')
# print(values)

db = {}
for item in values:
    each_value = item.select(selector='td')
    db.update({each_value[0].text: {
        list_[1]: each_value[1].text,
        list_[2]: each_value[2].text,
        list_[3]: each_value[3].text,
        list_[4]: each_value[4].text,
        list_[5]: each_value[5].text
        }
    })

print(DataFrame(db))


























# from bs4 import BeautifulSoup
#
# # Open and read the HTML file with the specified encoding (UTF-8)
# with open('C:\\Users\\ranah\\PycharmProjects\\WebScraping\\website.html', 'r', encoding='utf-8') as data:
#     html_content = data.read()
#
# # Parse the HTML content
# soup = BeautifulSoup(html_content, 'html.parser')
#
# # Print the title element
# all_anchor_tag = soup.find_all(name='a')
# db = {tag.getText(): tag.get('href') for tag in all_anchor_tag}
# print(db)
#
# # # heading = soup.find(name='h1', id='name')
# # # print(heading.getText())
# #
# # company_url = soup.select_one(selector='p a')
# # print(company_url.get('href'))
