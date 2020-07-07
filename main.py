from movie_quote_twitter_bot.bot import Bot
from movie_quote_twitter_bot.config import Config
import os

if __name__ == "__main__":
    config = Config(os.environ)
    bot = Bot()
    while True:
        bot.main()
        bot.wait()
