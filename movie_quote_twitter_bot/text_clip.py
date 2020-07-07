from moviepy.editor import TextClip as _TextClip


class TextClip:

    def __init__(self, config):
        self.config = config

    def build(self, sentence, start, end):
        return (
            _TextClip(
                sentence,
                fontsize=self.config.get("TEXT_SIZE"),
                color=self.config.get("TEXT_COLOR"),
                font=self.config.get("TEXT_FONT"),
            )
            .set_pos("bottom")
            .set_duration(str(end - start))
        )
