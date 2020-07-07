from movie_quote_twitter_bot.bot import Bot
from movie_quote_twitter_bot.config import Config
from movie_quote_twitter_bot.subs import Subs
from movie_quote_twitter_bot.text_clip import TextClip
import os

if __name__ == "__main__":
    config = Config(os.environ)
    subs = Subs(config.get("SUBS_URI"), config.get("SUBS_ENCODING"))
    # TODO: Pass the specific values, not the whole config
    text_clip = TextClip(config)
    bot = Bot(config, subs)
    while True:
        bot.main()
        bot.wait()
