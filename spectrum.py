from communication import Communication


class Spectrum(Communication):
    """ Class for CMU200 spectrum configurations"""
    def __init__(self, comport, timeout, sec_addr_serial, *args, **kwargs):
        super(Spectrum, self).__init__(comport, timeout, sec_addr_serial, *args, **kwargs)


    def start_freq(self, value):
        """
        Set the spectrum Analyzer start frequency in Hz
        :param value: Frequency in Hz
        :return: None
        """
        self.__write("SENSe:SPECtrum:FREQuency:STARt {}".format(value))

    def stop_freq(self, value):
        """
        Set the spectrum Analyzer stop frequency in Hz
        :param value: Frequency in Hz
        :return: None
        """
        self.__write("SENSe:SPECtrum:FREQuency:STOP {}".format(value))

    def span_freq(self, value):
        """
        Set the spectrum Analyzer span frequency in Hz
        :param value: Frequency in Hz
        :return: None
        """
        self.__write("SENSe:SPECtrum:FREQuency:SPAN {}".format(value))

    def center_freq(self, value):
        """
        Set the spectrum Analyzer center frequency in Hz
        :param value: Frequency in Hz
        :return: None
        """
        self.__write("SENSe:SPECtrum:FREQuency:CENTer {}".format(value))

    def Bandwidth_freq(self, value):
        """
        Set the spectrum Analyzer bandwidth frequency in Hz
        :param value: Frequency in Hz
        :return: None
        """
        self.__write("SENSe:SPECtrum:FREQuency:BANDwidth {}".format(value))

    def level_range(self, value):
        """
        Set the spectrum Analyzer level range in dB
        :param value: level in dB
        :return: None
        """
        self.__write("SENSe:SPECtrum:LEVel:RANGe {}".format(value))


        # Todo add more functions
        # list: https://github.com/bryan-rozier/Brython/blob/master/CRTU_Spectrum.py
