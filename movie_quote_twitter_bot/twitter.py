import twitter


class Twitter:

    def __init__(
        self,
        consumer_key,
        consumer_secret,
        access_token_key,
        access_token_secret,
        output_uri
    ):
        self.api = twitter.Api(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token_key,
            access_token_secret=access_token_secret
        )
        self.output_uri = output_uri

    def post_gif(self, text):
        self.api.PostUpdate(
            text,
            media=self.output_uri,
            media_category="tweet_gif"
        )
        return None
