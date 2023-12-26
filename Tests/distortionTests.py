import unittest
from Pedals.Distortion.distortionPedal import DistortionPedal
from Root.audiofile import AudioFile


class DistortionTests(unittest.TestCase):

    def test_distortion(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        distortionPedal = DistortionPedal()
        output_1 = distortionPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        distortionPedal.ChangeDistortion(0.2)
        output_2 = distortionPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_cutoff(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        distortionPedal = DistortionPedal()
        output_1 = distortionPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        distortionPedal.ChangeCutoff(4.0)
        output_2 = distortionPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_depth(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        distortionPedal = DistortionPedal()
        output_1 = distortionPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        distortionPedal.ChangeDepth(0.2)
        output_2 = distortionPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_level(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        distortionPedal = DistortionPedal()
        output_1 = distortionPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        distortionPedal.ChangeLevel(0.8)
        output_2 = distortionPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_basic(self):
        distortionPedal = DistortionPedal()
        self.assertEqual(distortionPedal.pedalType, "distortion")
        self.assertEqual(distortionPedal.distortionParam, 0.5)
        self.assertEqual(distortionPedal.cutoffParam, 3.7)
        self.assertEqual(distortionPedal.depthParam, 0.5)
        self.assertEqual(distortionPedal.levelParam, 0.0)


if __name__ == '__main__':
    unittest.main()
