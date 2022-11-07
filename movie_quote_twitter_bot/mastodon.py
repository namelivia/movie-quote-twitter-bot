from mastodon import Mastodon


class MastodonAPI:
    def __init__(
        self,
        client_id,
        client_secret,
        api_base_url,
        login,
        password,
        output_uri,
    ):
        self.mastodon = Mastodon(
            client_id=client_id, client_secret=client_secret, api_base_url=api_base_url
        )
        self.mastodon.log_in(login, password)
        self.output_uri = output_uri

    def post_gif(self, text):
        media_dict = self.mastodon.media_post(self.output_uri, mime_type="image/gif")
        self.mastodon.status_post(text, media_ids=media_dict)
        return None
