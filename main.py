from bs4 import BeautifulSoup

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

all = soup.find_all('a')
# for tag in all:
#     print(tag.get('href'))

heading = soup.find(name= 'h1', class_ = 'heading')
# print(heading.get('class'))

company_url = soup.select(selector='a')
print(company_url)