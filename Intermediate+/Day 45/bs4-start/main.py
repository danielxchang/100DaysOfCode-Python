from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(class_="titlelink")
articles_texts = []
articles_links = []
for article_tag in articles:
     articles_texts.append(article_tag.getText())
     articles_links.append(article_tag.get("href"))

article_upvotes = [int(score_tag.getText().split()[0]) for score_tag in soup.find_all(class_="score")]
print(articles_texts)
print(articles_links)
print(article_upvotes)

max_votes = max(article_upvotes)
max_idx = article_upvotes.index(max_votes)
print(max_idx)
print(max_votes)
print(articles_texts[max_idx])
print(articles_links[max_idx])


