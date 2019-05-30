"""EnviHdrLineWriter class"""
from tq.hdr.hdr_line_writer import HdrLineWriter

class EnviHdrLineWriter(HdrLineWriter):
  """A class that writes a line in an ENVI HDR file."""

  ENVI_PATTERN = "{0} = {1}\n"

  def __init__(self):
    super(EnviHdrLineWriter, self).__init__(self.ENVI_PATTERN)