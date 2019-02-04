#!/usr/bin/python3
import srt
import random
import twitter
import config
from moviepy.editor import *


class MovieQuoteTwitterBot:

    def main(self):
        quote = random.choice(self.get_subs(config.GENERAL_CONFIG['subsURI']))
        video = self.generate_video_clip(
            config.GENERAL_CONFIG['videoURI'],
            quote.start,
            quote.end
        )
        text = self.generate_text_clip(quote.content, quote.start, quote.end)
        self.create_gif(config.GENERAL_CONFIG['outputURI'], video, text)

        api = twitter.Api(
            consumer_key=config.GENERAL_CONFIG['consumerKey'],
            consumer_secret=config.GENERAL_CONFIG['consumerSecret'],
            access_token_key=config.GENERAL_CONFIG['accessTokenKey'],
            access_token_secret=config.GENERAL_CONFIG['accessTokenSecret'],
        )
        self.post_gif_to_twitter(
            api, quote.content, config.GENERAL_CONFIG['outputURI'])

    def get_subs(self, subs_file_uri):
        subs_file = open(
            config.GENERAL_CONFIG['subsURI'],
            encoding=config.GENERAL_CONFIG['subsEncoding'])
        return list(srt.parse(subs_file.read()))

    def post_gif_to_twitter(self, api, sentence, gif_path):
        api.PostUpdate(sentence, media=gif_path, media_category='tweet_gif')

    def generate_video_clip(self, video_uri, start, end):
        return (VideoFileClip(video_uri)
                .subclip(str(start), str(end))
                .resize(0.3))

    def generate_text_clip(self, sentence, start, end):
        return TextClip(sentence, fontsize=24, color=config.GENERAL_CONFIG['textColor'],
                        font='FreeSans-Negrita').set_pos('bottom').set_duration(str(end - start))

    def create_gif(self, output_uri, video, text):
        compo = CompositeVideoClip([video, text])
        compo.write_gif(output_uri)


if __name__ == '__main__':
    MovieQuoteTwitterBot().main()
