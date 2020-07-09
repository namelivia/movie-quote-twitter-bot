from movie_quote_twitter_bot.factory import Factory
from movie_quote_twitter_bot.config import Config
import os

if __name__ == "__main__":

    config = Config(os.environ)
    bot = Factory(config).build()

    while True:
        bot.run()
        bot.wait()
