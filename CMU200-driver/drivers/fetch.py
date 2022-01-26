
from .communication import Communication


class Fetch(Communication):
    """ Class for CMU200 spectrum configurations"""

    def __init__(self, comport, timeout, sec_addr_serial):
        super(Communication, self).__init__(comport, timeout, sec_addr_serial)


    def spectrum_marker_peak(self):
        """
        Query the peak value in dB
        """
        self.query("FETCh:SPECtrum:MARKer:PEAK?")
