"""EsriHdrLineWriter class"""
from hdr.hdr_line_writer import HdrLineWriter

class EsriHdrLineWriter(HdrLineWriter):
  """A class that writes a line in an ESRI HDR file."""

  ESRI_PATTERN = "{0} {1}\n"

  def __init__(self):
    super(EsriHdrLineWriter, self).__init__(self.ESRI_PATTERN)
