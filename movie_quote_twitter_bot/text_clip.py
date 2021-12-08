from moviepy.editor import TextClip as _TextClip


class TextClip:
    def __init__(self, size, color, font):
        self.size = size
        self.color = color
        self.font = font

    def generate_quote_text(self, quote):
        return (
            _TextClip(
                quote.content,
                fontsize=self.size,
                color=self.color,
                font=self.font,
            )
            .set_postion(("center", "bottom"))
            .set_duration(str(quote.end - quote.start))
        )
