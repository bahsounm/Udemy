# # Beautiful Soup is a python library for pulling data out of HTML and XML files

# from bs4 import BeautifulSoup

# # open the html file and grab the contents of the file
# with open("website.html","r") as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)


# # how do we get a hold of all elements of a certain tag
# all_anchor_tags = soup.find_all(name="a") # find all anchor tags

# for tag in all_anchor_tags:
#     # print the actual text of the tag
#     print(tag.getText())
#     # isolate the ling
#     print(tag.get("href"))

# # how to isolate by class name
# heading = soup.find(name="h1", id="name") # can do the same with the 
# print(heading)

# # how can we select specific elements
# print(soup.select(".heading")) # similar to css selectors

#---------------------------------------------------------------
# Scraping a Live website
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []

articles = soup.find_all(name="span",class_="titleline")
for article in articles:
    article_texts.append(article.a.getText())
    article_links.append(article.a["href"])

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span",class_="score")]


# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_vote = article_upvotes.index(max(article_upvotes))
most_popular_text = article_texts[max_vote]
most_popular_link = article_links[max_vote]

print(most_popular_text, most_popular_link)

# all_anchor = soup.find_all(name="a")
# for anchor in all_anchor:
#     print(anchor.getText())
