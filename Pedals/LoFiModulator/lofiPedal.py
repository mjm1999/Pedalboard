from Pedals.pedalbase import BasePedal
from Pedals.LoFiModulator.lofiFunctions import modulator


class LoFiPedal(BasePedal):
    def __init__(self, modulation_param: float = 0.2):
        super().__init__()
        self.pedalType = 'lofimodulator'
        self.modulationParam = modulation_param

    def ChangeModulation(self, value: float):
        self.modulationParam = value

    def PrintParams(self):
        print(f"\nModulation: {self.modulationParam}/0.99")
    def __ModulationSignal(self, audio_data):
        if self.modulationParam > 0.99:
            print(f"Modulation parameter {self.modulationParam} exceeds upper bound of 0.99. Adjusting.")
            self.modulationParam = 0.99
        if self.modulationParam < 0.0:
            print(f"Modulation parameter {self.modulationParam} exceeds lower bound of 0. Adjusting.")
            self.modulationParam = 0.0
        output_data = modulator(audio_data, self.modulationParam)
        return output_data

    def Execute(self, audio_data: [float], audio_rate: int = 22050):
        audio_data = self.__ModulationSignal(audio_data)
        return audio_data
