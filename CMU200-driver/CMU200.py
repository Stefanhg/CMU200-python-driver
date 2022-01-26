from drivers.spectrum import Spectrum
from drivers.fetch import Fetch
from drivers.communication import Communication

class Cmu200(object):
    """Class for controlling the CMU200 """
    def __init__(self, comm_port, timeout=1, sec_addr_serial=""):
        """
        :param comm_port: communication port, refer to PyVisa documentation
        :param timeout: PyVisa communicaiton timeout in seconds
        :param sec_addr_serial: Secoundary addressing for when using comport
        """

        # Initialize the other configuration classes
        self.comm = Communication(comm_port, timeout, sec_addr_serial)
        self.spectrum = Spectrum(self.comm)
        self.fetch = Fetch(self.comm)

    def close(self):
        """Closes the Cmu200 instance"""
        self.spectrum.inst.close()

class listDevices:

    def __init__(self):
        import pyvisa
        rm = pyvisa.ResourceManager()

        data = rm.list_resources()
        print(data)
