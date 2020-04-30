import numpy as np
import re

from hdr.hdr_builder import HdrBuilder

def parse_hdr_line(line):
    """Parses a line from an HDR file."""
    m = re.search('([\w ]+) = (.*)', line)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    else:
        return None, None

def read_hdr(filename):
    """Parses an HDR file."""
    hdr = {}
    with open(filename, "rb") as f:
        for line in f:
            try:
                line = line.decode("utf-8")
            except (UnicodeDecodeError, AttributeError):
                pass
            key, value = parse_hdr_line(line)
            if key:
                if key == HdrBuilder.HDR_WAVE_LENGTH:
                    hdr[key] = parse_wave_lengths(value)
                else:
                    hdr[key] = value
    return hdr

def get_dtype(data_type):
    """Returns the proper dtype."""
    return {
        '8': 'int8',
        '16': 'int16',
        '32': 'int32'
    }[data_type]

def parse_wave_lengths(wave_length):
    """Returns the proper wave lengths."""
    m = re.search('{(.+)}', wave_length)
    return m.group(1).strip().split(', ')

def get_wave_length_index(wave_lengths, wave_length, default):
    """Gets the wave length."""
    i = 0
    for wl in wave_lengths:
        if wl == wave_length:
            return i
        i = i + 1
    return default

def read_bsq(filename, num_samples, num_lines, num_bands, data_type):
    """Reads a bsq file given the number of samples (columns),
    lines, bands and data type."""
    img = np.fromfile(filename, dtype=data_type)
    return img.reshape((num_bands, num_lines, num_samples))

def read_bil_from_buf(buf, num_samples, num_lines, num_bands, data_type):
    """Reads a bil from a buffer given the number of samples (columns),
    lines, bands and data type."""
    img = np.frombuffer(buf, dtype=data_type)
    return img.reshape((num_lines, num_bands, num_samples))

def read_bil(filename, num_samples, num_lines, num_bands, data_type):
    """Reads a bil file given the number of samples (columns),
    lines, bands and data type."""
    img = np.fromfile(filename, dtype=data_type)
    return img.reshape((num_lines, num_bands, num_samples))

def read_bip(filename, num_samples, num_lines, num_bands, data_type):
    """Reads a bip file given the number of samples (columns),
    lines, bands and data type."""
    img = np.fromfile(filename, dtype=data_type)
    return img.reshape((num_lines, num_samples, num_bands))

def read_bsq_from_hdr(hdr, filename):
    """Reads a BSQ from the values in the proper hdr file."""
    num_samples = int(hdr[HdrBuilder.HDR_COLS])
    num_lines = int(hdr[HdrBuilder.HDR_ROWS])
    num_bands = int(hdr[HdrBuilder.HDR_BANDS])
    dtype = get_dtype(int(hdr[HdrBuilder.HDR_PIXEL_TYPE]))
    return read_bsq(filename, num_samples, num_lines, num_bands, dtype)

def bsq2bip(bsq):
    """Converts a bsq to bip."""
    return np.moveaxis(bsq, 0, -1)

def bsq2bil(bsq):
    """Converts a bsq to bil."""
    return np.moveaxis(bsq, 1, 0)

def bip2bsq(bip):
    """Converts a bip to bsq."""
    return np.moveaxis(bip, 2, 0)

def bip2bil(bip):
    """Converts a bip to bil."""
    return np.moveaxis(bip, 1, 2)

def bil2bsq(bil):
    """Converts a bil to bsq."""
    return np.moveaxis(bil, 0, 1)

def bil2bip(bil):
    """Converts a bil to bip."""
    return np.moveaxis(bil, 1, 2)

def arr_multiply(arr, scalar):
    with np.nditer(arr, flags=['external_loop', 'buffered'], op_flags=['readwrite']) as it:
        for x in it:
            x[...] = x * scalar

def normalize(bip):
    """Normalizes all pixels according to its max value."""
    max_value = np.amax(bip)
    factor = float(2**(bip.dtype.itemsize * 8) - 1) / float(max_value)
    arr_multiply(bip, factor)
    return res.astype(bip.dtype)

def calc_histogram_variance(bsq):
    """Calculates the histogram variance."""
    variances = np.zeros((np.shape(bsq)[0]))
    for b, band in enumerate(bsq):
        variances[b] = np.bincount(band.ravel()).var()
    return variances
