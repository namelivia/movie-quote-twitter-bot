import srt
import random
import twitter
import os
import time
from moviepy.editor import *


class Bot:

    def __init__(self, config):
        self.config = config

    def wait(self):
        time.sleep(int(self.config["IDLE_PERIOD"]))

    def main(self):
        quote = random.choice(self.get_subs(self.config["SUBS_URI"]))
        video = self.generate_video_clip(
            self.config["VIDEO_URI"], quote.start, quote.end
        )
        text = self.generate_text_clip(quote.content, quote.start, quote.end)
        self.create_gif(self.config["OUTPUT_URI"], video, text)

        api = twitter.Api(
            consumer_key=self.config["CONSUMER_KEY"],
            consumer_secret=self.config["CONSUMER_SECRET"],
            access_token_key=self.config["ACCESS_TOKEN_KEY"],
            access_token_secret=self.config["ACCESS_TOKEN_SECRET"]
        )
        self.post_gif_to_twitter(api, quote.content, self.config["OUTPUT_URI"])

    def get_subs(self, subs_file_uri):
        subs_file = open(
            self.config["SUBS_URI"],
            encoding=self.config["SUBS_ENCODING"],
        )
        return list(srt.parse(subs_file.read()))

    def post_gif_to_twitter(self, api, sentence, gif_path):
        api.PostUpdate(sentence, media=gif_path, media_category="tweet_gif")

    def generate_video_clip(self, video_uri, start, end):
        return VideoFileClip(video_uri).subclip(str(start), str(end)).resize(0.3)

    def generate_text_clip(self, sentence, start, end):
        return (
            TextClip(
                sentence,
                fontsize=int(self.config["TEXT_SIZE"]),
                color=self.config["TEXT_COLOR"],
                font=self.config["TEXT_FONT"],
            )
            .set_pos("bottom")
            .set_duration(str(end - start))
        )

    def create_gif(self, output_uri, video, text):
        compo = CompositeVideoClip([video, text])
        compo.write_gif(output_uri, verbose=False, logger=None)
