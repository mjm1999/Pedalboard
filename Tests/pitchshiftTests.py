import unittest
from Pedals.PitchShift.pitchshiftPedal import PitchShiftPedal
from Root.audiofile import AudioFile


class PitchShiftTests(unittest.TestCase):

    def test_octaves(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        pitchshiftPedal = PitchShiftPedal()
        output_1 = pitchshiftPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        pitchshiftPedal.ChangeOctaves(1)
        output_2 = pitchshiftPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_semitones(self):
        testAudioFile = AudioFile()
        testAudioFile.loadFile("test_input.mp3")
        testData = testAudioFile.getData()
        testRate = int(testAudioFile.getRate())
        pitchshiftPedal = PitchShiftPedal()
        output_1 = pitchshiftPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(testData, output_1)
        pitchshiftPedal.ChangeSemitones(4.)
        output_2 = pitchshiftPedal.Execute(audio_data=testData, audio_rate=testRate)
        self.assertNotEqual(output_1, output_2)

    def test_basic(self):
        pitchshiftPedal = PitchShiftPedal()
        self.assertEqual(pitchshiftPedal.pedalType, "distortion")
        self.assertEqual(pitchshiftPedal.octavesParam, 0)
        self.assertEqual(pitchshiftPedal.semitonesParam, 0)


if __name__ == '__main__':
    unittest.main()
