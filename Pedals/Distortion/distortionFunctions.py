from math import atan
from scipy.signal import butter, lfilter


def distort(input_signal: [], gain: float = 0.5) -> [float]:  #
    """
    Distort audio signal using equation f(x) = C1 * atan(C2 * x)
    :param input_signal: list of audio file data
    :param gain: float representing how much distortion to add
    :return: the modified audio signal as a list
    """

    C1 = gain * 40
    C2 = 2/(gain * 40)
    output_signal = input_signal

    #  multiply by C2
    output_signal = [float(x * C1) for x in output_signal]

    #  apply arctangent
    output_signal = [atan(x) for x in output_signal]

    #  multiply by C1
    output_signal = [float(x * C2) for x in output_signal]

    return output_signal


def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)


def butter_lowpass_filter(data, cutoff, fs, order=5):
    print(cutoff)
    print(fs)
    print(order)
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


def tone(input_signal: [float], cutoff: float = 3.7, depth=0.5) -> [float]:
    """
    Modifies the audio signal tone using a lowpass filter
    :param input_signal: list of audio file data
    :param cutoff: float indicating cutoff value for lowpass filter in kHz
    :param depth: int indicating steepness of cutoff for filter
    :return: the modified audio signal as a list
    """

    # Filter the data, and plot both the original and filtered signals.
    output_signal = butter_lowpass_filter(input_signal, cutoff, depth * 60, 20)
    return output_signal


def level(input_signal: [float], increase: float = 0) -> [float]:
    """
    Volume boost to add to the distortion effect in postprocessing
    :param input_signal: list of audio file data
    :param increase: float indicating decibel increase to add in postprocessing
    :return: the modified audio signal as a list
    """

    decibelToFloat = 10 ** (increase)
    output_signal = [x * decibelToFloat for x in input_signal]
    return output_signal
