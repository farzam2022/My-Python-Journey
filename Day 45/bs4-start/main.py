from bs4 import BeautifulSoup
import lxml
import requests

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.p)
# all_anchor_tags=soup.find_all(name="a")
# # print(soup.find_all(name="a"))
# for tag in all_anchor_tags:
#     # print(tag.get("href"))
#     # print(tag.get_text())
#     pass
# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get)
# name = soup.select_one(selector="#name")
# # print(name)
# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="a", class_="storylink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").get_text()
print(article_link)
