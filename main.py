from bs4 import BeautifulSoup
import requests

# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# all = soup.find_all('a')
# # for tag in all:
# #     print(tag.get('href'))
#
# heading = soup.find(name= 'h1', class_ = 'heading')
# # print(heading.get('class'))
#
# company_url = soup.select(selector='a')
# print(company_url)

response = requests.get('http://news.ycombinator.com/news')

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
# print(soup)
article = soup.find_all(name='a', class_='titlelink')

article_texts = []
article_links = []

for article_tag in article:
    article_text = article_tag.get_text()
    article_texts.append(article_text)
    article_link = article_tag.get('href')
    article_links.append(article_link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)


print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvote)