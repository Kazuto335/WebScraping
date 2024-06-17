from bs4 import BeautifulSoup

# Open and read the HTML file with the specified encoding (UTF-8)
with open('C:\\Users\\ranah\\PycharmProjects\\WebScraping\\website.html', 'r', encoding='utf-8') as data:
    html_content = data.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Print the title element
# all_anchor_tag = soup.find_all(name='a')
# db = {tag.getText(): tag.get('href') for tag in all_anchor_tag}
# # print(db)

# heading = soup.find(name='h1', id='name')
# print(heading.getText())

company_url = soup.select_one(selector='p a')
print(company_url.get('href'))
