from Pedals.pedalbase import BasePedal
from audiofile import AudioFile
import soundfile as sf


class Pedalboard:
    def __init__(self):
        self.pedals = []

    def addPedal(self, pedal: BasePedal, index: int = -1):
        if index == -1:
            self.pedals.append(pedal)
        else:
            self.pedals.insert(index, pedal)

    def delPedal(self, index: int = -1):
        self.pedals.pop(index)

    def displayPedals(self):
        for i, pedal in enumerate(self.pedals):
            print(f"{i} - {pedal.pedalType}")
            pedal.PrintParams()
            print("\n__________\n")

    def processFile(self, audio: AudioFile, output_name: str = 'out.mp3'):
        audio_data = audio.data
        audio_rate = audio.rate
        for pedal in self.pedals:
            audio_data = pedal.Execute(audio_data, audio_rate)

        sf.write(output_name, audio_data, int(audio_rate))
