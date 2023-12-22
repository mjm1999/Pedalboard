
def implementDelay(input_signal: [float], sample_rate: float = 22050,
                   delay_time: float = 300, decay_rate: float = 0.5) -> [float]:
    """
    Add a delay effect to an audio signal.
    :param input_signal: list of audio file data
    :param sample_rate: float representing sample rate of audio file
    :param delay_time: float representing time between delay impulses
    :param decay_rate: float representing how quickly delay impulses fade

    :return: the modified audio signal as a list
    """
    delay_samples = int(delay_time * sample_rate/1000)
    output_signal = input_signal
    for x in range(len(input_signal) - delay_samples):
        output_signal[x + delay_samples] += float(output_signal[x] * decay_rate)

    return output_signal
