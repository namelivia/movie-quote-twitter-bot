class Config:

    def __init__(self, source):
        self.config = {
            'idle_period': int(source["IDLE_PERIOD"]),
            'subs_uri': source["SUBS_URI"],
            'subs_encoding': source["SUBS_ENCODING"],
            'video_uri': source["VIDEO_URI"],
            'output_uri': source["OUTPUT_URI"],
            'consumer_key': source["CONSUMER_KEY"],
            'consumer_secret': source["CONSUMER_SECRET"],
            'access_token_key': source["ACCESS_TOKEN_KEY"],
            'access_token_secret': source["ACCESS_TOKEN_SECRET"],
            'text_size': int(source["TEXT_SIZE"]),
            'text_color': source["TEXT_COLOR"],
            'text_font': source["TEXT_FONT"],
        }

    def get(self, key):
        return self.config[key]
