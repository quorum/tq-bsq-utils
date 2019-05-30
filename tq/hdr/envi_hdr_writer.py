"""EnviHdrWriter class"""
from tq.hdr.hdr_writer import HdrWriter
from tq.hdr.envi_hdr_line_writer import EnviHdrLineWriter
from tq.hdr.envi_hdr_builder import EnviHdrBuilder

class EnviHdrWriter(HdrWriter):
  """A class that writes HDR files in ENVI format."""

  def __init__(self, cols, rows, bands, pixel_type, layout, wave_lengths):
    super(EnviHdrWriter, self).__init__(EnviHdrLineWriter(), EnviHdrBuilder(cols, rows, bands, pixel_type, "0", layout, wave_lengths))
