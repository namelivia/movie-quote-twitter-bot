#!/usr/bin/python3
import srt
import random
import twitter
import config
from moviepy.editor import *
subsFile = open(config.GENERAL_CONFIG['subsURI'], encoding='utf-8-sig')
subs = list(srt.parse(subsFile.read()))
selected = random.choice(subs)
video = (VideoFileClip(config.GENERAL_CONFIG['videoURI'])
         .subclip(str(selected.start), str(selected.end))
         .resize(0.3))
text = TextClip(selected.content, fontsize=24, color='yellow',
                font='Amiri-bold').set_pos('bottom').set_duration(str(selected.end - selected.start))
compo = CompositeVideoClip([video, text])
compo.write_gif(config.GENERAL_CONFIG['outputPath'])
api = twitter.Api(
    consumer_key=config.GENERAL_CONFIG['consumerKey'],
    consumer_secret=config.GENERAL_CONFIG['consumerSecret'],
    access_token_key=config.GENERAL_CONFIG['accessTokenKey'],
    access_token_secret=config.GENERAL_CONFIG['accessTokenSecret'],
)
status = api.PostUpdate(
    selected.content,
    media=config.GENERAL_CONFIG['outputPath'],
    media_category='tweet_gif')
