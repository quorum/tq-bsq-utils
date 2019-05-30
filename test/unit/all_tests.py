import unittest
from test.unit.hdr.hdr_writer_tests import HdrWriterTests
from test.unit.hdr.hdr_line_writer_tests import HdrLineWriterTests
from test.unit.hdr.hdr_builder_tests import HdrBuilderTests
from test.unit.hdr.esri_hdr_line_writer_tests import EsriHdrLineWriterTests
from test.unit.hdr.envi_hdr_line_writer_tests import EnviHdrLineWriterTests

class AllTestsSuite(unittest.TestSuite):
  def suite(self):
    test_loader = unittest.TestLoader()
    return unittest.TestSuite(
      [
        test_loader.loadTestsFromTestCase(HdrWriterTests),
        test_loader.loadTestsFromTestCase(HdrLineWriterTests),
        test_loader.loadTestsFromTestCase(HdrBuilderTests),
        test_loader.loadTestsFromTestCase(EsriHdrLineWriterTests),
        test_loader.loadTestsFromTestCase(EnviHdrLineWriterTests),
      ]
    )