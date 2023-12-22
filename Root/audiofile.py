from librosa import load


class AudioFile:
    def __init__(self):
        self.data, self.rate = None, None  # sample rate defaults to 22050

    def loadFile(self, filename):
        self.data, self.rate = load(filename)

