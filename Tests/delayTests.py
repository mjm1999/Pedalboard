import unittest
from Pedals.Delay.delayPedal import DelayPedal
from Root.audiofile import AudioFile


class DelayTests(unittest.TestCase):

    def test_time(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        delayPedal = DelayPedal()
        output_1 = delayPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        delayPedal.ChangeTime(0.2)
        output_2 = delayPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_decay(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        delayPedal = DelayPedal()
        output_1 = delayPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        delayPedal.ChangeDecay(0.2)
        output_2 = delayPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_basic(self):
        delayPedal = DelayPedal()
        self.assertEqual(delayPedal.pedalType, "delay")
        self.assertEqual(delayPedal.timeParam, 0.5)
        self.assertEqual(delayPedal.decayParam, 0.5)


if __name__ == '__main__':
    unittest.main()
