import numpy as np
from math import sin, pi
from scipy.signal import butter, lfilter


def overdrive(input_signal: [float], drive: int = 0) -> [float]:
    """
    Distort audio signal using equation f(x) = C1 * atan(C2 * x)
    :param input_signal: list of audio file data
    :param drive: float representing how much to overdrive signal
    :return: the modified audio signal as a list
    """
    a = sin(((drive + 1) / 101) * pi / 2)
    k = (2 * a) / (1 - a)
    output_signal = [float((1 + k) * x) for x in input_signal]
    output_signal = [float(x / (1 + (k * np.absolute(x)))) for x in output_signal]

    return output_signal


def butter_lowpass(cutoff: float, fs: float, order: int = 5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)


def butter_lowpass_filter(input_signal: [float], cutoff: float, fs: float, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, input_signal)
    return y


def tone(input_signal: [float], cutoff: float = 3.7, depth: float = 30) -> [float]:
    """
    Modifies the audio signal tone using a lowpass filter
    :param input_signal: list of audio file data
    :param cutoff: float indicating cutoff value for lowpass filter in kHz
    :param depth: int indicating steepness of cutoff for filter
    :return: the modified audio signal as a list
    """

    output_signal = butter_lowpass_filter(input_signal, cutoff, depth, 20)
    return output_signal


def boost(input_signal: [float], increase: float = 0) -> [float]:
    """
    Volume boost to add to the distortion effect in postprocessing
    :param input_signal: list of audio file data
    :param increase: float indicating decibel increase to add in postprocessing
    :return: the modified audio signal as a list
    """

    decibelToFloat = 10 ** (increase / 10)
    output_signal = [x * decibelToFloat for x in input_signal]
    return output_signal
