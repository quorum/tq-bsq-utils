import unittest

from mock import Mock

from hdr.esri_hdr_line_writer import EsriHdrLineWriter

class EsriHdrLineWriterTests(unittest.TestCase):
    def test_write_with_key(self):
        f = Mock()
        key = "A key"
        value = "A value"
        esri_hdr_line_writer = EsriHdrLineWriter()
        esri_hdr_line_writer.write(f, key, value)
        f.write.assert_called_once_with(esri_hdr_line_writer.ESRI_PATTERN.format(key, value))
    
    def test_write_without_key(self):
        f = Mock()
        key = None
        value = "A value"
        esri_hdr_line_writer = EsriHdrLineWriter()
        esri_hdr_line_writer.write(f, key, value)
        f.write.assert_not_called()
