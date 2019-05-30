"""HdrLineWriter class"""

class HdrLineWriter(object):
  """An abstract class that writes lines in an HDR file using a particular pattern."""

  def __init__(self, pattern):
    self.pattern = pattern
  
  def write(self, f, key, value):
    """Writes a line in a particular file using the pattern provided."""
    if (key):
      f.write(self.pattern.format(key, value))
