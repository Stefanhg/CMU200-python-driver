from spectrum import Spectrum
from communication import Communication


class Cmu200(object):
    def __init__(self, comm_port, timeout=1, sec_addr_serial=""):
        """

        :param comm_port:
        """
        # Initialize the other configuration classes
        # Communication(comm_port, timeout, sec_addr_serial)
        self.spectrum = Spectrum(comm_port, timeout, sec_addr_serial)
