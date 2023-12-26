import unittest
from Pedals.LoFiModulator.lofiPedal import LoFiPedal
from Root.audiofile import AudioFile


class LoFiTests(unittest.TestCase):

    def test_modulation(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        lofiPedal = LoFiPedal()
        output_1 = lofiPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        lofiPedal.ChangeModulation(0.8)
        output_2 = lofiPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_basic(self):
        lofiPedal = LoFiPedal()
        self.assertEqual(lofiPedal.pedalType, "lofimodulator")
        self.assertEqual(lofiPedal.modulationParam, 0.2)


if __name__ == '__main__':
    unittest.main()
