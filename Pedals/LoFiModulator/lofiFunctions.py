import librosa.effects
import numpy as np


def timestretch(input_signal: [float], stretch: float = 1.0) -> [float]:
    out = librosa.effects.time_stretch(input_signal, rate=stretch)

    return out


def modulator(input_signal: [float], factor: float = 0.0) -> [float]:
    """
    Add a lo-fi effect to an audio signal by signal compression and decompression
    :param input_signal: list of audio file data
    :param factor: float indicating factor by which signal should be compressed and decompressed
    :return: the modified audio signal as a list
    """
    output_signal = timestretch(np.array(input_signal), factor)
    output_signal = timestretch(output_signal, (1 - factor))

    return output_signal
