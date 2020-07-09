from unittest import TestCase
from movie_quote_twitter_bot.factory import Factory


class TestTwitter(TestCase):
    def setUp(self):
        self.config = {}
        self.factory = Factory(self.config)

    def test_building_bot(self):
        self.factory.build()
