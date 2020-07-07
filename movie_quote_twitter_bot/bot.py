import twitter
import time
from moviepy.editor import *


class Bot:

    def __init__(self, config, subs, text_clip):
        self.config = config
        self.subs = subs
        self.text_clip = text_clip

    def wait(self):
        time.sleep(int(self.config["IDLE_PERIOD"]))

    def main(self):
        quote = self.subs.get_random()
        video = self.generate_video_clip(
            self.config["VIDEO_URI"], quote.start, quote.end
        )
        text = self.text_clip.build(quote.content, quote.start, quote.end)
        self.create_gif(self.config["OUTPUT_URI"], video, text)

        api = twitter.Api(
            consumer_key=self.config["CONSUMER_KEY"],
            consumer_secret=self.config["CONSUMER_SECRET"],
            access_token_key=self.config["ACCESS_TOKEN_KEY"],
            access_token_secret=self.config["ACCESS_TOKEN_SECRET"]
        )
        self.post_gif_to_twitter(api, quote.content, self.config["OUTPUT_URI"])

    def post_gif_to_twitter(self, api, sentence, gif_path):
        api.PostUpdate(sentence, media=gif_path, media_category="tweet_gif")

    def generate_video_clip(self, video_uri, start, end):
        return VideoFileClip(video_uri).subclip(str(start), str(end)).resize(0.3)

    def create_gif(self, output_uri, video, text):
        compo = CompositeVideoClip([video, text])
        compo.write_gif(output_uri, verbose=False, logger=None)
