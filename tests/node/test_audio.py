import pytest   # noqa F401

from ved.node import Audio


class TestAudio:
    def test_constructing_audio_with_8_44100_does_not_error(self):
        Audio(8, 44100)
