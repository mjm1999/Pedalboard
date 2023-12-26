import unittest
from Pedals.Delay.delayPedal import DelayPedal
from Pedals.Delay.delayFunctions import *
from Root.audiofile import AudioFile


class DelayFunctionTests(unittest.TestCase):

    testAudioFile = AudioFile()
    testAudioFile.loadFile("test_input.mp3")
    testData = testAudioFile.getData()
    testRate = testAudioFile.getRate()

    def test_time(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
