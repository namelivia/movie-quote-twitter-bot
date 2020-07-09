from unittest import TestCase
from movie_quote_twitter_bot.twitter import Twitter
import mock


class TestTwitter(TestCase):

    @mock.patch('movie_quote_twitter_bot.twitter.twitter.Api')
    def test_posting_a_gif(self, m_api_factory):
        twitter_api_mock = mock.Mock()
        m_api_factory.return_value = twitter_api_mock
        consumer_key = 'consumer_key'
        consumer_secret = 'consumer_secret'
        access_token_key = 'access_token_key'
        access_token_secret = 'access_token_secret'
        output_uri = '/tmp/output'
        twitter = Twitter(
            consumer_key,
            consumer_secret,
            access_token_key,
            access_token_secret,
            output_uri
        )
        m_api_factory.assert_called_once_with(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token_key,
            access_token_secret=access_token_secret
        )
        text = 'text'
        self.assertIsNone(twitter.post_gif(text))
        twitter_api_mock.PostUpdate.assert_called_once_with(
            text,
            media=output_uri,
            media_category="tweet_gif"
        )
