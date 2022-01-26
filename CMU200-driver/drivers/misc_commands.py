from .communication import Communication


class Misc(Communication):
    """ Class for CMU200 Misc commands"""
    def __init__(self, comport, timeout, sec_addr_serial):
        super(Misc, self).__init__(comport, timeout, sec_addr_serial)
        # Configure the secoundary address
        self.secoundary_addr = 1
        self.write("SYSTem:REMote:ADDRess:SECondary 1 RF_NSig")

    def go_to_local(self):
        self.write("*GTL")