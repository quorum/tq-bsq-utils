import unittest

from mock import Mock

from tq.hdr.hdr_builder import HdrBuilder

class HdrBuilderTests(unittest.TestCase):
    def test_build(self):
        wave_lengths = [ 1.1, 2.2, 3.3, 4.4, 5.5, 6.6 ]
        hdr_builder = HdrBuilder(1, 2, 3, 4, 5, 6, wave_lengths)
        self.assertEquals(hdr_builder.build(),{
            hdr_builder.HDR_COLS: 1,
            hdr_builder.HDR_ROWS: 2,
            hdr_builder.HDR_BANDS: 3,
            hdr_builder.HDR_PIXEL_TYPE: 4,
            hdr_builder.HDR_BYTE_ORDER: 5,
            hdr_builder.HDR_LAYOUT: 6,
            hdr_builder.HDR_WAVE_LENGTH: hdr_builder.wave_lengths_to_str(wave_lengths),
        })

    def test_wave_lengths_to_str(self):
        hdr_builder = HdrBuilder(0, 0, 0, 0, 0, 0, 0)
        wave_lengths = [ 1.1, 2.2, 3.3, 4.4, 5.5, 6.6 ]
        self.assertEquals(hdr_builder.wave_lengths_to_str(wave_lengths), "{ 1.1, 2.2, 3.3, 4.4, 5.5, 6.6 }")
