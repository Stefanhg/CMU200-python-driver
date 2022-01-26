

class Spectrum:
    """ Class for CMU200 spectrum commands"""
    def __init__(self, comm):
        super(Spectrum, self).__init__()
        # Configure the secoundary address
        self.comm = comm
        self.secoundary_addr = 1
        self.comm.write("SYSTem:REMote:ADDRess:SECondary 1 RF_NSig")

    def initialize_spectrum(self):
        command = "INITiate:SPECtrum"
        self.comm.write(command)
    def abort_spectrum(self):
        command = "ABORt:SPECtrum"
        self.comm.write(command)

    def start_freq(self, value):
        """
        Set the spectrum Analyzer start frequency in Hz
        :param value: Frequency in Hz
        :return: None
        """
        self.comm.query_write("SENSe:SPECtrum:FREQuency:STARt", value)

    def stop_freq(self, value):
        """
        Set the spectrum Analyzer stop frequency in Hz
        :param value: Frequency in Hz
        :return: None
        """
        self.comm.query_write("SENSe:SPECtrum:FREQuency:STOP", value)

    def span_freq(self, value):
        """
        Set the spectrum Analyzer span frequency in Hz
        :param value: Frequency in Hz
        :return: None
        """
        self.comm.query_write("SENSe:SPECtrum:FREQuency:SPAN", value)

    def center_freq(self, value):
        """
        Set the spectrum Analyzer center frequency in Hz
        :param value: Frequency in Hz
        :return: None
        """
        self.comm.query_write("SENSe:SPECtrum:FREQuency:CENTer", value)

    def bandwidth_freq(self, value):
        """
        Set or query the spectrum Analyzer bandwidth frequency in Hz
        :param value: Frequency in Hz
        :return: None
        """
        self.comm.query_write("SENSe:SPECtrum:FREQuency:BANDwidth", value)

    def level_range(self, value):
        """
        Set the spectrum Analyzer level range in dB
        :param value: level in dB
        :return: None
        """
        self.comm.query_write("SENSe:SPECtrum:LEVel:RANGe", value)

        # Todo add more functions
        # list: https://github.com/bryan-rozier/Brython/blob/master/CRTU_Spectrum.py


