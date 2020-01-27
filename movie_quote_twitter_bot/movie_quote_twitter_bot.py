#!/usr/bin/python3
import srt
import random
import twitter
import os
import time
from moviepy.editor import *


class MovieQuoteTwitterBot:
    def main(self):
        quote = random.choice(self.get_subs(os.environ["SUBS_URI"]))
        video = self.generate_video_clip(
            os.environ["VIDEO_URI"], quote.start, quote.end
        )
        text = self.generate_text_clip(quote.content, quote.start, quote.end)
        self.create_gif(os.environ["OUTPUT_URI"], video, text)

        api = twitter.Api(
            consumer_key=os.environ["CONSUMER_KEY"],
            consumer_secret=os.environ["CONSUMER_SECRET"],
            access_token_key=os.environ["ACCESS_TOKEN_KEY"],
            access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
        )
        self.post_gif_to_twitter(api, quote.content, os.environ["OUTPUT_URI"])

    def get_subs(self, subs_file_uri):
        subs_file = open(
            os.environ["SUBS_URI"],
            encoding=os.environ["SUBS_ENCODING"],
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
                fontsize=int(os.environ["TEXT_SIZE"]),
                color=os.environ["TEXT_COLOR"],
                font=os.environ["TEXT_FONT"],
            )
            .set_pos("bottom")
            .set_duration(str(end - start))
        )

    def create_gif(self, output_uri, video, text):
        compo = CompositeVideoClip([video, text])
        compo.write_gif(output_uri, verbose=False, logger=None)


if __name__ == "__main__":
    while True:
        MovieQuoteTwitterBot().main()
        time.sleep(int(os.environ["IDLE_PERIOD"]))
