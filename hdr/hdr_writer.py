"""HdrWriter class"""

class HdrWriter(object):
  """An abstract class that writes HDR files."""

  def __init__(self, line_writer, hdr_builder):
    self.line_writer = line_writer
    self.hdr_builder = hdr_builder

  def write(self, filename):
    """Writes an HDR file using the specific line_writer and hdr_builder."""
    hdr = self.hdr_builder.build()
    with open(filename, "w") as f:
        for key, value in hdr.iteritems():
            self.line_writer.write(f, key, value)
