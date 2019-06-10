"""EsriHdrWriter class"""
from hdr.hdr_writer import HdrWriter
from hdr.esri_hdr_line_writer import EsriHdrLineWriter
from hdr.esri_hdr_builder import EsriHdrBuilder

class EsriHdrWriter(HdrWriter):
  """A class that writes HDR files in ESRI format."""

  def __init__(self, cols, rows, bands, pixel_type, layout, wave_lengths):
    super(EsriHdrWriter, self).__init__(EsriHdrLineWriter(), EsriHdrBuilder(cols, rows, bands, pixel_type, "", layout, wave_lengths))
