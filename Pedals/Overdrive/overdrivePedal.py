from Pedals.pedalbase import BasePedal
from Pedals.Overdrive.overdriveFunctions import overdrive, tone, boost


class OverdrivePedal(BasePedal):
    def __init__(self, overdrive_param: int = 30, tone_param: float = 0, boost_param: float = 0):
        super().__init__()
        self.pedalType = 'overdrive'
        self.overdriveParam = overdrive_param  # float range of 0 to 1 - 0 lowest, 1 highest
        self.toneParam = tone_param  # float range of -1 to 1 - -1 bassiest, +1 trebliest
        self.boostParam = boost_param  # adjusted volume of output - 0 normal, 1 highest

    def ChangeOverdrive(self, value: float):
        self.overdriveParam = value

    def ChangeTone(self, value: float):
        self.toneParam = value

    def ChangeLevel(self, value: float):
        self.boostParam = value

    def __OverdriveSignal(self, audio_data):
        output_data = overdrive(audio_data, self.overdriveParam)
        return output_data

    def __ToneSignal(self, audio_data, audio_rate):
        if self.toneParam == 0:
            return audio_data
        output_data = tone(audio_data, audio_rate, self.toneParam)
        return output_data

    def __BoostSignal(self, audio_data):
        output_data = boost(audio_data)
        return output_data

    def Execute(self, audio_data, audio_rate):
        audio_data = self.__BoostSignal(audio_data)
        audio_data = self.__OverdriveSignal(audio_data)
        audio_data = self.__ToneSignal(audio_data, audio_rate)
        return audio_data

