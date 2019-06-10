import unittest

from mock import Mock

from hdr.hdr_line_writer import HdrLineWriter

class HdrLineWriterTests(unittest.TestCase):
    def test_write_with_key(self):
        f = Mock()
        key = "A key"
        value = "A value"
        pattern = "{0} : {1}"
        hdr_line_writer = HdrLineWriter(pattern)
        hdr_line_writer.write(f, key, value)
        f.write.assert_called_once_with(pattern.format(key, value))
    
    def test_write_without_key(self):
        f = Mock()
        key = None
        value = "A value"
        pattern = "{0} : {1}"
        hdr_line_writer = HdrLineWriter(pattern)
        hdr_line_writer.write(f, key, value)
        f.write.assert_not_called()
