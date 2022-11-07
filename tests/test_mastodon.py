from unittest import TestCase
from movie_quote_twitter_bot.mastodon import MastodonAPI
import mock


class TestMastodon(TestCase):
    @mock.patch("movie_quote_twitter_bot.mastodon.mastodon.Mastodon")
    def test_posting_a_gif(self, m_api_factory):
        mastodon_api_mock = mock.Mock()
        m_api_factory.return_value = mastodon_api_mock
        client_id = "client_id"
        api_base_url = "api_base_url"
        login = "login"
        password = "password"
        output_uri = "/tmp/output"
        mastodon = MastodonAPI(
            client_id,
            api_base_url,
            login,
            password,
            output_uri,
        )
        m_api_factory.assert_called_once_with(
            client_id=client_id,
            api_base_url=api_base_url,
        )
        mastodon_api_mock.login.assert_called_once_with(login, password)
        text = "text"
        # m_api_factory.return_value = {"media": "dict"}
        self.assertIsNone(mastodon.post_gif(text))
        # mastodon_api_mock.media_post.assert_called_once_with(
        #    output_uri,
        #    mime_type="image/gif"
        # )
        mastodon_api_mock.status_post.assert_called_once_with(
            text,
            # media={"media": "dict"}
        )
