import srt
import random


class Subs:

    def __init__(self, filepath, encoding):
        self.filepath = filepath
        self.encoding = encoding

    def get_all(self):
        # TODO: I don't need to open and parse the whole file each time
        subs_file = open(
            self.filepath,
            encoding=self.encoding,
        )
        return random.choice(list(srt.parse(subs_file.read())))
