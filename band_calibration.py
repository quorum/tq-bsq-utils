"""Band Calibration utility class to process calibration values."""
import math
import re

MAX_DIGITS_WAVE_LENGTH = 7

class ParseException(Exception):
    def __init__(self, line):
        self.line = line
        super(ParseException, self).__init__("Error parsing line: {0}".format(line))

    def get_line(self):
        return self.line

class BandMismatchException(ParseException):
    pass

class NoBandsException(Exception):
    def __init__(self):
        super(NoBandsException, self).__init__("No band calibration has yet been read.")

class OutOfBoundsException(Exception):
    def __init__(self, wave_length, lowest, highest):
        super(OutOfBoundsException, self).__init__("The provided wave length [{0}] is out of bounds. \
        Lowest and highest value are {1} and {2} respectively.".format(wave_length, lowest, highest))

class BandCalibration:
    def __init__(self):
        self.band_calibration_arr = []

    def from_array(self, wave_lengths):
        """Sets the band calibration from a given existing array."""
        self.band_calibration_arr = list(map(lambda wave_length: float(wave_length), wave_lengths))

    def to_array(self):
        """Returns the band calibration list as an array."""
        return list(self.band_calibration_arr)

    def get_closest_lower_row(self, index, wave_length):
        """Returns the index of the row from band calibration array
        that is closer to the wave length starting from index and following
        to lower indexes."""
        mid = self.band_calibration_arr[index]
        if wave_length > mid:
            return index
        while True:
            next_index = index - 1
            if next_index < 0:
                return index
            else:
                next_mid = self.band_calibration_arr[next_index]
                if next_mid < wave_length:
                    return index if wave_length - next_mid > mid - wave_length else next_index
                else:
                    index = next_index
                    mid = next_mid

    def get_closest_higher_row(self, index, wave_length):
        """Returns the index of the row from band calibration array
        that is closer to the wave length starting from index and following
        to higher indexes."""
        mid = self.band_calibration_arr[index]
        if wave_length < mid:
            return index
        while True:
            next_index = index + 1
            if next_index >= len(self.band_calibration_arr):
                return index
            else:
                next_mid = self.band_calibration_arr[next_index]
                if next_mid > wave_length:
                    return index if next_mid - wave_length > wave_length - mid else next_index
                else:
                    index = next_index
                    mid = next_mid

    def get_closest_row(self, index, wave_length):
        mid = self.band_calibration_arr[index]
        if wave_length < mid:
            return self.get_closest_lower_row(index, wave_length)
        elif wave_length > mid:
            return self.get_closest_higher_row(index, wave_length)
        else:
            return index

    def get_row_from_wave_length(self, wave_length):
        """Returns the closest row number that corresponds to a given wave length.
        Raises NoBandsException if no band calibration file has been read yet.
        Raises OutOfBoundsException if wave length provided is out of bounds.
        """
        if len(self.band_calibration_arr) == 0:
            raise NoBandsException()
        else:
            lowest = self.band_calibration_arr[0]
            highest = self.band_calibration_arr[-1]
            wl = float(wave_length)
            if (wl < lowest or wl > highest):
                raise OutOfBoundsException(wl, lowest, highest)
            else:
                factor = (wl - lowest) / (highest - lowest)
                index = int(factor * (len(self.band_calibration_arr) - 1))
            return self.get_closest_row(index, wave_length)

    def get_wave_length_from_row(self, index):
        """Returns the wave length that corresponds to a given row number.
        Raises IndexError if index is out of bounds."""
        if index < 0 or index >= len(self.band_calibration_arr):
            raise IndexError
        else:
            return self.band_calibration_arr[index]

    def get_wave_length_from_decimal_row(self, decimal_row):
        """Returns the wave length that results from prorating a float based
        row number with the closest integer row numbers according to their
        corresponding wave lengths."""
        lo_in = int(math.floor(decimal_row))
        hi_in = int(math.ceil(decimal_row))
        lo_wl = self.get_wave_length_from_row(lo_in)
        hi_wl = self.get_wave_length_from_row(hi_in)
        return (decimal_row - lo_in) * (hi_wl - lo_wl) + lo_wl

    def get_wave_lengths(self, num_bands):
        """Returns an array of wave lengths based from this band calibration
        object and re-scaled according to a new number of bands."""
        res = []
        factor = float(len(self.band_calibration_arr) - 1) / float(num_bands - 1)
        for band in range(0, num_bands):
            res.append(round(self.get_wave_length_from_decimal_row(factor * band), MAX_DIGITS_WAVE_LENGTH))
        return res

    def read(self, filename):
        """Opens the file, parses the calibration values and stores
        them in memory."""
        with open(filename, 'r') as f:
            try:
                self.read_calibration_from_file(f)
            except Exception as e:
                self.band_calibration_arr = []
                raise e            

    def read_calibration_from_file(self, f):
        """Given a file handle, reads every line in it and parses
        its content to store it in memory."""
        for line in f:
          self.process_calibration_line(line)

    def process_calibration_line(self, line):
        """Given a band calibration line, it parses it and appends
        it to the band_calibration_arr."""
        (index, wave_length) = self.parse_calibration_line(line)
        if len(self.band_calibration_arr) != (index - 1):
            raise BandMismatchException(line)
        else:
            self.band_calibration_arr.append(wave_length)
    
    def parse_calibration_line(self, line):
        """Given a band calibration line, it parses it and returns
        the parsed result. If it is unable to parse it, it throws
        a ParseException."""
        components = re.split('\s+', line.rstrip().lstrip())
        if (len(components) != 2):
            raise ParseException(line)
        else:
            return (int(components[0]), float(components[1].replace(',','.')))