from Pedals.pedalbase import BasePedal
from Pedals.Delay.delayFunctions import implementDelay


class DelayPedal(BasePedal):
    def __init__(self, time_param: float = 300, decay_param: float = 0.5):
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
        output_data = implementDelay(audio_data, audio_rate, self.timeParam, self.decayParam)
        return output_data

    def Execute(self, audio_data, audio_rate=None):
        audio_data = self.__DelaySignal(audio_data, audio_rate)
        return audio_data
