import pyvisa


class Communication:
    """Class for the CMU200 communication module"""
    def __init__(self, comm_port, timeout, sec_addr_serial):
        super(Communication, self).__init__()

        # Initialize the instance if not already initialized
        if not hasattr(self, "inst"):
            self.inst = pyvisa.ResourceManager().open_resource(comm_port)
            self.inst.timeout = timeout * 1000.0  # Configure the timeout
            self.sec_addr_serial = sec_addr_serial

    def write(self, command):
        """
        Write command to CMU200
        :param command: Command to write to CMU200, for Serial configure the sec_addr_serial to communicate
        """

        self.inst.write(self.sec_addr_serial + command)

    def read(self):
        """Read data from CMU200"""
        data = self.inst.readline()
        return data

    def query(self, command):
        """
        Query data from CMU200
        :param command: Command to write to CMU200, for Serial configure the sec_addr_serial to communicate

        """
        data = self.inst.query(self.sec_addr_serial + command)
        return data

    def close(self):
        self.inst.close()
