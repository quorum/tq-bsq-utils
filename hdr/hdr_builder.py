"""HdrBuilder class"""

class HdrBuilder(object):
  """An abstract class for implementing builders for HDR based formats."""

  # Default attribute names

  HDR_ROWS = "nrows"
  HDR_COLS = "ncols"
  HDR_BANDS = "nbands"
  HDR_BITS = "nbits" # Not currently used
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
  HDR_GEO_POINTS = "geo points"

  # Available layouts
  HDR_LAYOUT_BIL = "bil"
  HDR_LAYOUT_BIP = "bip"
  HDR_LAYOUT_BSQ = "bsq"

  def __init__(self, cols, rows, bands, pixel_type, byte_order, layout, wave_lengths, geo_points = []):
    self.cols = cols
    self.rows = rows
    self.bands = bands
    self.pixel_type = pixel_type
    self.byte_order = byte_order
    self.layout = layout
    self.wave_lengths = wave_lengths
    self.geo_points = geo_points

  def build(self):
    """Builds an object with all the attributes according to the appropriate HDR format."""
    return {
        self.HDR_COLS: self.cols,
        self.HDR_ROWS: self.rows,
        self.HDR_BANDS: self.bands,
        self.HDR_PIXEL_TYPE: self.pixel_type,
        self.HDR_BYTE_ORDER: self.byte_order,
        self.HDR_LAYOUT: self.layout,
        self.HDR_WAVE_LENGTH: self.wave_lengths_to_str(self.wave_lengths),
        self.HDR_GEO_POINTS: self.geo_points_to_str(self.geo_points),
    }

  def wave_lengths_to_str(self, wave_lengths):
    """Creates a proper HDR string representation for wave lengths."""
    res = "{ "
    i = 0
    for wave_length in wave_lengths:
        if i > 0 : res = res + ", "
        res = res + str(wave_length)
        i = i + 1
    res = res + " }"
    return res

  def geo_points_to_str(self, geo_points):
    """Creates a proper HDR string representation for geo points."""
    res = "{ "
    i = 0
    for geo_point in geo_points:
        if i > 0 : res = res + ", "
        res = res + str(geo_point[0]) + ", " + str(geo_point[1]) + ", " + str(geo_point[2]) + ", " + str(geo_point[3])
        i = i + 1
    res = res + " }"
    return res
