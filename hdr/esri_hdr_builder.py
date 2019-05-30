"""EsriHdrBuilder class"""
from tq.hdr.hdr_builder import HdrBuilder

class EsriHdrBuilder(HdrBuilder):
  """A class for building HDRs in ESRI format."""

  HDR_ROWS = "nrows"
  HDR_COLS = "ncols"
  HDR_BANDS = "nbands"
  HDR_BITS = "nbits"
  HDR_PIXEL_TYPE = "pixeltype"
  HDR_BYTE_ORDER = "byteorder" # Not currently used
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

  # Available layouts
  HDR_LAYOUT_BIL = "bil"
  HDR_LAYOUT_BIP = "bip"
  HDR_LAYOUT_BSQ = "bsq"
