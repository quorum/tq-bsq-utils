"""EnviHdrBuilder class"""
from hdr.hdr_builder import HdrBuilder

class EnviHdrBuilder(HdrBuilder):
  """A class for building HDRs in ENVI format."""

  HDR_ROWS = "lines"
  HDR_COLS = "samples"
  HDR_BANDS = "bands"
  HDR_BITS = "nbits"
  HDR_PIXEL_TYPE = "data type"
  HDR_BYTE_ORDER = "byte order" # Not currently used
  HDR_LAYOUT = "layout"
  HDR_SKIP_BYTES = "skipbytes" # Not currently used
  HDR_UL_X_MAP = "ulxmap" # Not currently used
  HDR_UL_Y_MAP = "ulymap" # Not currently used
  HDR_X_DIM = "xdim" # Not currently used
  HDR_Y_DIM = "ydim" # Not currently used
  HDR_BAND_ROW_BYTES = "bandrowbytes" # Not currently used
  HDR_TOTAL_ROW_BYTES = "totalrowbytes" # Not currently used
  HDR_BAND_GAP_BYTES = "bandgapbytes" # Not currently used

  # Custom attributes
  HDR_WAVE_LENGTH = "wavelength"
  HDR_GEO_POINTS = "geo points"

  # Available layouts
  HDR_LAYOUT_BIL = "bil"
  HDR_LAYOUT_BIP = "bip"
  HDR_LAYOUT_BSQ = "bsq"
