import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# anchs = soup.find_all("a")
#
# for tag in anchs:
#     print(tag.get("href"))
# print(response.text)
articles = soup.find_all("span", class_="titleline")
article_texts = []
# article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    # article_texts.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
article_links = [link.get("href") for link in soup.find_all("a")]

# for _ in article_upvotes:
#     print(_)
# print(article_upvotes)
# print(article_texts)

# datasets = pd.DataFrame(article_texts,article_upvotes)
# articles_dict = datasets.to_dict()
# print(datasets)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_number)
print(article_texts[largest_index])



















# from bs4 import BeautifulSoup
# import lxml
#
# with open("website.html") as data:
#     contents = data.read()
#     # print(contents)
#
# soup = BeautifulSoup(contents, 'html.parser')
# # all_anchor_tags = soup.find_all(name="a")
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
# # print(all_anchor_tags)
#
# # heading = soup.find(name="h3", class_="heading")
# # print(heading.get("class"))
#
# # company_url = soup.select_one(selector="p a")
# company_url = soup.select_one(selector=".heading")
# print(company_url)