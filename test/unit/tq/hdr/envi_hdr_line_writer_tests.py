import unittest

from mock import Mock

from tq.hdr.envi_hdr_line_writer import EnviHdrLineWriter

class EnviHdrLineWriterTests(unittest.TestCase):
    def test_write_with_key(self):
        f = Mock()
        key = "A key"
        value = "A value"
        envi_hdr_line_writer = EnviHdrLineWriter()
        envi_hdr_line_writer.write(f, key, value)
        f.write.assert_called_once_with(envi_hdr_line_writer.ENVI_PATTERN.format(key, value))
    
    def test_write_without_key(self):
        f = Mock()
        key = None
        value = "A value"
        envi_hdr_line_writer = EnviHdrLineWriter()
        envi_hdr_line_writer.write(f, key, value)
        f.write.assert_not_called()
