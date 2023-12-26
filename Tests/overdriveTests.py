import unittest
from Pedals.Overdrive.overdrivePedal import OverdrivePedal
from Root.audiofile import AudioFile


class OverdriveTests(unittest.TestCase):

    def test_distortion(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        overdrivePedal = OverdrivePedal()
        output_1 = overdrivePedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        overdrivePedal.ChangeOverdrive(0.2)
        output_2 = overdrivePedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_cutoff(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        overdrivePedal = OverdrivePedal()
        output_1 = overdrivePedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        overdrivePedal.ChangeCutoff(4.0)
        output_2 = overdrivePedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_depth(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        overdrivePedal = OverdrivePedal()
        output_1 = overdrivePedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        overdrivePedal.ChangeDepth(0.2)
        output_2 = overdrivePedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_level(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        overdrivePedal = OverdrivePedal()
        output_1 = overdrivePedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        overdrivePedal.ChangeBoost(0.8)
        output_2 = overdrivePedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_basic(self):
        overdrivePedal = OverdrivePedal()
        self.assertEqual(overdrivePedal.pedalType, "overdrive")
        self.assertEqual(overdrivePedal.overdriveParam, 0.5)
        self.assertEqual(overdrivePedal.cutoffParam, 3.7)
        self.assertEqual(overdrivePedal.depthParam, 0.5)
        self.assertEqual(overdrivePedal.boostParam, 0.0)


if __name__ == '__main__':
    unittest.main()
