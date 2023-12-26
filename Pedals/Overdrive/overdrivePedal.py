from Pedals.pedalbase import BasePedal
from Pedals.Overdrive.overdriveFunctions import overdrive, tone, boost


class OverdrivePedal(BasePedal):
    def __init__(self, overdrive_param: int = 30, cutoff_param: float = 3.7,
                 depth_param: float = 0.5, boost_param: float = 0):
        super().__init__()
        self.pedalType = 'overdrive'
        self.overdriveParam = overdrive_param  # float range of 0 to 1 - 0 lowest, 1 highest
        self.cutoffParam = cutoff_param  # float range of -1 to 1 - -1 bassiest, +1 trebliest
        self.depthParam = depth_param
        self.boostParam = boost_param  # adjusted volume of output - 0 normal, 1 highest

    def ChangeOverdrive(self, value: float):
        self.overdriveParam = value

    def ChangeCutoff(self, value: float):
        self.cutoffParam = value

    def ChangeDepth(self, value: float):
        self.depthParam = value

    def ChangeBoost(self, value: float):
        self.boostParam = value

    def PrintParams(self):
        print(f"\nOverdrive: {self.overdriveParam}/1.0"
              f"\nCutoff: {self.cutoffParam}kHz"
              f"\nDepth: {self.depthParam}/1.0"
              f"\nBoost: {self.boostParam}/1.0")
    def __OverdriveSignal(self, audio_data):
        output_data = overdrive(audio_data, self.overdriveParam)
        return output_data

    def __ToneSignal(self, audio_data):
        if self.cutoffParam == 0:
            return audio_data
        if self.depthParam > 1:
            print(f"Depth parameter {self.depthParam} exceeds upper bound of 1. Adjusting.")
            self.toneParam = 1
        output_data = tone(audio_data, self.cutoffParam, self.depthParam)
        return output_data

    def __BoostSignal(self, audio_data):
        if self.boostParam > 1:
            print(f"Level parameter {self.boostParam} exceeds upper bound of 1. Adjusting.")
            self.boostParam = 1
        output_data = boost(audio_data, self.boostParam)
        return output_data

    def Execute(self, audio_data: [float], audio_rate: int = 22050):
        audio_data = self.__BoostSignal(audio_data)
        audio_data = self.__OverdriveSignal(audio_data)
        audio_data = self.__ToneSignal(audio_data, audio_rate)
        return audio_data

