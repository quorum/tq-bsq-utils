import unittest

from mock import Mock, mock_open, patch

from tq.hdr.hdr_writer import HdrWriter

class HdrWriterTests(unittest.TestCase):
    def test_write(self):
        key = "key"
        value = "value"
        filename = "a/filename"
        m = mock_open(read_data="data")
        line_writer = Mock()
        line_writer.write = Mock()
        hdr_builder = Mock()
        hdr_builder.build = Mock(return_value={key: value})
        hdr_writer = HdrWriter(line_writer, hdr_builder)
        with patch("__builtin__.open", m, create=True):
            hdr_writer.write(filename)
            hdr_builder.build.assert_called_once()
            m.assert_called_once_with(filename, "w")
            handle = m()
            line_writer.write.assert_called_once_with(handle, key, value)