
class Misc:
    """ Class for CMU200 Misc commands"""
    def __init__(self, communication):
        super(Misc, self).__init__()
        # Configure the secoundary address
        self.secoundary_addr = 1
        self.comm = communication
        self.comm.write("SYSTem:REMote:ADDRess:SECondary 1 RF_NSig")

    def go_to_local(self):
        self.comm.write("*GTL")