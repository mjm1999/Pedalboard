import librosa.effects
import numpy as np


def pitchshift(input_signal: [float], sample_rate: float = 22050,
               octaves: int = 0, semitones: int = 0) -> [float]:
    """
    Modulate input signal to different pitch based on semitone and octave increments
    :param input_signal: list of audio file data
    :param sample_rate: float representing sample rate of audio file
    :param octaves: int representing positive or negative octave shift
    :param semitones: int representing positive or negative semitone shift
    :return: the modified audio signal as a list
    """
    totalshift = octaves * 12 + semitones
    output_signal = librosa.effects.pitch_shift(np.array(input_signal), sr=sample_rate, n_steps=totalshift)

    return output_signal
