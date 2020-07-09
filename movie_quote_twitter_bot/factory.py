from .bot import Bot
from .subs import Subs
from .text_clip import TextClip
from .video_clip import VideoClip
from .twitter import Twitter
from .gif import Gif


class Factory():
    def __init__(self, config):
        self.config = config

    def build(self):
        subs = Subs(
            self.config.get("SUBS_URI"),
            self.config.get("SUBS_ENCODING")
        )
        text_clip = TextClip(
            self.config.get("TEXT_SIZE"),
            self.config.get("TEXT_COLOR"),
            self.config.get("TEXT_FONT")
        )
        video_clip = VideoClip(self.config.get("VIDEO_URI"))
        twitter = Twitter(
            self.config.get("CONSUMER_KEY"),
            self.config.get("CONSUMER_SECRET"),
            self.config.get("ACCESS_TOKEN_KEY"),
            self.config.get("ACCESS_TOKEN_SECRET"),
            self.config.get("OUTPUT_URI")
        )
        gif = Gif(self.config.get("OUTPUT_URI"))
        return Bot(
            subs,
            text_clip,
            video_clip,
            twitter,
            gif,
            self.config.get("IDLE_PERIOD")
        )
