from scraper import ScraperBot
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1&Season=2021-22&SeasonType=Regular%20Season"


def scrape_leading_scorers(html):
    soup = BeautifulSoup(html)
    table = soup.find(name="table")
    d = {
        'Player': [tag.a.contents[0] for tag in table.find_all(name="td", class_="player")],
        'PPG': [float(tag.contents[0]) for tag in table.find_all(name="td", class_="sorted")]
    }
    indices = list(range(1, 51))
    df = pd.DataFrame(
        data=d,
        index=indices
    )
    df.to_csv(path_or_buf="top_50_leading_scorers.csv", index=False)


def scrape_nba_stats():
    bot = ScraperBot(URL)
    scrape_leading_scorers(bot.html)
    bot.driver.quit()
    print("Updated csv file.")


if __name__ == "__main__":
    scrape_nba_stats()
