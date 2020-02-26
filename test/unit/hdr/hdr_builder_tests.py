import unittest

from mock import Mock

from hdr.hdr_builder import HdrBuilder

class HdrBuilderTests(unittest.TestCase):
    geo_points = [
        (1.0, 1.0, 0.0, 0.0),
        (100.0, 1.0, 0.0, 0.34),
        (1.0, 100.0, 0.34, 0.0),
        (100.0, 100.0, 0.34, 0.34),
    ]
    wave_lengths = [ 1.1, 2.2, 3.3, 4.4, 5.5, 6.6 ]
    map_info = ( "UTM", 1.0, 1.0, 503920.0, 5056650.0, 0.1000, 0.1000, 12, "North", "WGS-84", "units meters")

    def test_build(self):
        hdr_builder = HdrBuilder(1, 2, 3, 4, 5, 6, self.wave_lengths, self.geo_points, self.map_info)
        self.assertEqual(hdr_builder.build(),{
            hdr_builder.HDR_COLS: 1,
            hdr_builder.HDR_ROWS: 2,
            hdr_builder.HDR_BANDS: 3,
            hdr_builder.HDR_PIXEL_TYPE: 4,
            hdr_builder.HDR_BYTE_ORDER: 5,
            hdr_builder.HDR_LAYOUT: 6,
            hdr_builder.HDR_WAVE_LENGTH: hdr_builder.wave_lengths_to_str(self.wave_lengths),
            hdr_builder.HDR_GEO_POINTS: hdr_builder.geo_points_to_str(self.geo_points),
            hdr_builder.HDR_MAP_INFO: hdr_builder.map_info_to_str(self.map_info),
        })

    def test_wave_lengths_to_str_empty(self):
        hdr_builder = HdrBuilder(0, 0, 0, 0, 0, 0, self.wave_lengths, self.geo_points, self.map_info)
        self.assertEqual(hdr_builder.wave_lengths_to_str(None), "{  }")

    def test_wave_lengths_to_str(self):
        hdr_builder = HdrBuilder(0, 0, 0, 0, 0, 0, self.wave_lengths, self.geo_points, self.map_info)
        self.assertEqual(hdr_builder.wave_lengths_to_str(self.wave_lengths), "{ 1.1, 2.2, 3.3, 4.4, 5.5, 6.6 }")

    def test_geo_points_to_str_empty(self):
        hdr_builder = HdrBuilder(0, 0, 0, 0, 0, 0, self.wave_lengths, self.geo_points, self.map_info)
        self.assertEqual(hdr_builder.geo_points_to_str(None), "{  }")

    def test_geo_points_to_str(self):
        hdr_builder = HdrBuilder(0, 0, 0, 0, 0, 0, self.wave_lengths, self.geo_points, self.map_info)
        self.assertEqual(hdr_builder.geo_points_to_str(self.geo_points), "{ 1.0, 1.0, 0.0, 0.0, 100.0, 1.0, 0.0, 0.34, 1.0, 100.0, 0.34, 0.0, 100.0, 100.0, 0.34, 0.34 }")

    def test_map_info_to_str_empty(self):
        hdr_builder = HdrBuilder(0, 0, 0, 0, 0, 0, self.wave_lengths, self.geo_points, self.map_info)
        self.assertEqual(hdr_builder.map_info_to_str(None), "{  }")

    def test_map_info_to_str(self):
        hdr_builder = HdrBuilder(0, 0, 0, 0, 0, 0, self.wave_lengths, self.geo_points, self.map_info)
        self.assertEqual(hdr_builder.map_info_to_str(self.map_info), "{ UTM, 1.0, 1.0, 503920.0, 5056650.0, 0.1, 0.1, 12, North, WGS-84, units meters }")
        