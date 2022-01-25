from communication import Communication


class Generator(Communication):
    """ Class for CMU200 spectrum commands"""

    def __init__(self, comport, timeout, sec_addr_serial):
        super(Generator, self).__init__(comport, timeout, sec_addr_serial)

    # SOURce:RFGenerator:MODulation OFF | SSB | AM | FM | FMST
    def set_modulation(self, value):

        command = "SOURce:RFGenerator:MODulation"
        if value in list('OFF', 'SSB', 'AM', 'FM', 'FMST'):
            self.query_write(command, value)
        else:
            raise "Incorrect command argument"

    # SOURce:RFGenerator:MODulation:SSB:FREQuency <Frequency>
    def set_modulation_ssb_frequency(self, value):

        command = "SOURce:RFGenerator:MODulation:SSB:FREQuency"

        self.query_write(command, value)

        # SOURce:RFGenerator:MODulation:AM:INDex <Mod_Index>

    def set_modulation_am_index(self, value):
        command = "SOURce:RFGenerator:MODulation:AM:INDex"

        self.query_write(command, value)

    # SOURce:RFGenerator:BANDwidth[:RESolution] <Bandwidth>
    def set_bandwidth(self, value):
        command = "SOURce:RFGenerator:BANDwidth"

        self.query_write(command, value)

    # SOURce:RFGenerator:MODulation:FM:FREQuency <Frequency>
    def set_modulation_fm_frequency(self, value):
        command = "SOURce:RFGenerator:MODulation:FM:FREQuency"

        self.query_write(command, value)

    # SOURce:RFGenerator:MODulation:FM:DEViation <Deviation>
    def set_modulation_fm_deviation(self, value):
        command = "SOURce:RFGenerator:MODulation:FM:DEViation"

        self.query_write(command, value)

    # INITiate:RFGenerator[:TX] INITiate:RFGenerator:AUXTx
    # ABORt:RFGenerator[:TX] ABORt:RFGenerator:AUXTx
    # FETCh:RFGenerator[:TX]:STATus?
    # FETCh:RFGenerator:AUXTx:STATus?
    def initialize_rfgen(self):
        command = "INITiate:RFGenerator"
        self.write(command)

    def abort_rfgen(self,,):
        command = "ABORt:RFGenerator"
        self.write(command)


# SOURce:RFGenerator[:TX]:LEVel <Level>

# SOURCe:RFGenerator[:TX]:FREQuency <Frequency>
