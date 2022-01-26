
class Fetch:
    """ Class for CMU200 spectrum configurations"""

    def __init__(self, comm):
        super(Fetch, self).__init__()
        self.comm = comm

    def spectrum_marker_peak(self):
        """
        Query the peak value in dB
        """
        self.comm.query("FETCh:SPECtrum:MARKer:PEAK?")
