from internet_speed_twitter_bot import InternetSpeedTwitterBot


def internet_speed_checker():
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()


if __name__ == "__main__":
    internet_speed_checker()
