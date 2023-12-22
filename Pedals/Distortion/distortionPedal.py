from Pedals.pedalbase import BasePedal
from Pedals.Distortion.distortionFunctions import distort, tone, level


class DistortionPedal(BasePedal):
    def __init__(self, distortion_param: float = 20, tone_param: float = 0, level_param: float = 0):
        super().__init__()
        self.pedalType = 'distortion'
        self.distortionParam = distortion_param  # float range of 0 to 1 - 0 lowest, 1 highest
        self.toneParam = tone_param  # float range of -1 to 1 - -1 bassiest, +1 trebliest
        self.levelParam = level_param  # adjusted volume of output - 0 normal, 1 highest

    def ChangeDistortion(self, value: float):
        self.distortionParam = value

    def ChangeTone(self, value: float):
        self.toneParam = value

    def ChangeLevel(self, value: float):
        self.levelParam = value

    def __DistortSignal(self, audio_data):
        output_data = distort(audio_data, self.distortionParam)
        return output_data

    def __ToneSignal(self, audio_data, audio_rate):
        if self.toneParam == 0:
            return audio_data
        output_data = tone(audio_data, audio_rate, self.toneParam)
        return output_data

    def __LevelSignal(self, audio_data):
        output_data = level(audio_data, self.levelParam)
        return output_data

    def Execute(self, audio_data, audio_rate):
        audio_data = self.__DistortSignal(audio_data)
        audio_data = self.__ToneSignal(audio_data, audio_rate)
        audio_data = self.__LevelSignal(audio_data)
        return audio_data


