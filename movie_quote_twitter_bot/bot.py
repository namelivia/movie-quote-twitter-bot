class Bot:
    def __init__(self, subs, text_clip, video_clip, twitter, mastodon, gif):
        self.subs = subs
        self.text_clip = text_clip
        self.video_clip = video_clip
        self.twitter = twitter
        self.mastodon = mastodon
        self.gif = gif

    def run(self):
        quote = self.subs.get_random()
        video = self.video_clip.generate_quote_video(quote)
        text = self.text_clip.generate_quote_text(quote)
        self.gif.generate_composite_gif(video, text)
        self.twitter.post_gif(quote.content)
        self.mastodon.post_gif(quote.content)
