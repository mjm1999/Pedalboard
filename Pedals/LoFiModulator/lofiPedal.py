from Pedals.pedalbase import BasePedal
from Pedals.LoFiModulator.lofiFunctions import modulator


class LoFiPedal(BasePedal):
    def __init__(self, modulation_param: float = 1):
        super().__init__()
        self.pedalType = 'lofimodulator'
        self.modulationParam = modulation_param  # float range of 1 to 5

    def ChangeModulation(self, value: float):
        self.modulationParam = value

    def __ModulationSignal(self, audio_data):
        if self.modulationParam > 5.0:
            self.modulationParam = 5.0
        if self.modulationParam < 1.0:
            self.modulationParam = 1.0
        output_data = modulator(audio_data, self.modulationParam)
        return output_data

    def Execute(self, audio_data, audio_rate=None):
        audio_data = self.__ModulationSignal(audio_data)
        return audio_data
