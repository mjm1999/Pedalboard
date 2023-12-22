from Pedals.pedalbase import BasePedal
from Pedals.PitchShift.pitchshiftFunctions import pitchshift


class PitchShiftPedal(BasePedal):
    def __init__(self, octaves_param: int = 0, semitones_param: int = 0):
        super().__init__()
        self.pedalType = 'pitchshift'
        self.octavesParam = octaves_param  # int range of -4 to +4 - 0 lowest, 1 highest
        self.semitonesParam = semitones_param  # int range of -11 to +11 - -1 bassiest, +1 trebliest

    def ChangeOctaves(self, value: int):
        self.octavesParam = value

    def ChangeSemitones(self, value: int):
        self.semitonesParam = value

    def __PitchShiftSignal(self, audio_data, audio_rate):
        output_data = pitchshift(audio_data,
                                 audio_rate,
                                 self.octavesParam,
                                 self.semitonesParam)
        return output_data

    def Execute(self, audio_data, audio_rate=None):
        audio_data = self.__PitchShiftSignal(audio_data, audio_rate)
        return audio_data


