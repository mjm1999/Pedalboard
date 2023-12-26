from Pedals.pedalbase import BasePedal
from Pedals.Delay.delayFunctions import implementDelay


class DelayPedal(BasePedal):
    def __init__(self, time_param: float = 0.5, decay_param: float = 0.5):
        super().__init__()
        self.pedalType = 'delay'
        self.timeParam = time_param  # float range of 0 to 1 - 0 shortest time between repeats, 1 longest
        self.decayParam = decay_param  # float range of 0 to 1 - 0 fastest decay, 1 slowest

    def ChangeTime(self, value: float):
        self.timeParam = value

    def ChangeFeedback(self, value: float):
        self.feedbackParam = value

    def ChangeDecay(self, value: float):
        self.decayParam = value

    def __DelaySignal(self, audio_data, audio_rate):
        if self.timeParam > 1:
            print(f"Time parameter {self.timeParam} exceeds upper bound of 1. Adjusting to 1.")
            self.timeParam = 1
        if self.decayParam >= 1:
            print(f"Decay parameter {self.decayParam} will not result in decay effect. Adjusting.")
            self.decayParam = 0.99
        output_data = implementDelay(audio_data, audio_rate, self.timeParam, self.decayParam)
        return output_data

    def Execute(self, audio_data: [float], audio_rate: int = 22050):
        audio_data = self.__DelaySignal(audio_data, audio_rate)
        return audio_data
