from Pedals.pedalbase import BasePedal
from Pedals.Distortion.distortionFunctions import distort, tone, level


class DistortionPedal(BasePedal):
    def __init__(self, distortion_param: float = 0.5, cutoff_param: float = 3.7,
                 depth_param: float = 0.5, level_param: float = 0):
        super().__init__()
        self.pedalType = 'distortion'
        self.distortionParam = distortion_param  # float range of 0 to 1 - 0 lowest, 1 highest
        self.cutoffParam = cutoff_param
        self.depthParam = depth_param  # float range of -1 to 1 - -1 bassiest, +1 trebliest
        self.levelParam = level_param  # adjusted volume of output - 0 normal, 1 highest

    def ChangeDistortion(self, value: float):
        self.distortionParam = value

    def ChangeCutoff(self, value: float):
        self.cutoffParam = value

    def ChangeDepth(self, value: float):
        self.depthParam = value

    def ChangeLevel(self, value: float):
        self.levelParam = value

    def PrintParams(self):
        print(f"\nDistortion: {self.distortionParam}/1.0"
              f"\nCutoff: {self.cutoffParam}kHz"
              f"\nDepth: {self.depthParam}/1.0"
              f"\nLevel: {self.levelParam}/1.0")
    def __DistortSignal(self, audio_data):
        if self.distortionParam > 1:
            print(f"Distortion parameter {self.distortionParam} exceeds upper bound of 1. Adjusting.")
            self.distortionParam = 1
        output_data = distort(audio_data, self.distortionParam)
        return output_data

    def __ToneSignal(self, audio_data):
        if self.cutoffParam == 0:
            return audio_data
        if self.depthParam > 1:
            print(f"Depth parameter {self.depthParam} exceeds upper bound of 1. Adjusting.")
            self.toneParam = 1
        output_data = tone(audio_data, self.cutoffParam, self.depthParam)
        return output_data

    def __LevelSignal(self, audio_data):
        if self.levelParam > 1:
            print(f"Level parameter {self.levelParam} exceeds upper bound of 1. Adjusting.")
            self.levelParam = 1
        output_data = level(audio_data, self.levelParam)
        return output_data

    def Execute(self, audio_data: [float], audio_rate: int = 22050):
        audio_data = self.__DistortSignal(audio_data)
        audio_data = self.__ToneSignal(audio_data, audio_rate)
        audio_data = self.__LevelSignal(audio_data)
        return audio_data


