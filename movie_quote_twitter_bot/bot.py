import time


class Bot:

    def __init__(
        self,
        subs,
        text_clip,
        video_clip,
        twitter,
        gif,
        idle_period
    ):
        self.subs = subs
        self.text_clip = text_clip
        self.video_clip = video_clip
        self.twitter = twitter
        self.gif = gif
        self.idle_period = idle_period

    def wait(self):
        time.sleep(self.idle_period)

    def run(self):
        quote = self.subs.get_random()
        video = self.video_clip.generate_quote_video(quote)
        text = self.text_clip.build(quote)
        self.gif.generate_composite_gif(video, text)
        self.twitter.post_gif(quote.content)
