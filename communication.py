import pyvisa



class Communication:
    def __init__(self, comm_port, timeout, sec_addr_serial, *args, **kwargs):
        super(Communication, self).__init__(*args, **kwargs)

        # Initialize the instance
        if not hasattr(self, "inst"):
            self.inst = pyvisa.ResourceManager().open_resource(comm_port)
            self.inst.timeout = timeout  # Configure the timeout
            self.sec_addr_serial = sec_addr_serial

    def __write(self, command):
        print(self.sec_addr_serial + command)
        self.inst.write(self.sec_addr_serial + command)
        print("ok")

    def __read(self):
        data = self.inst.readline()
        return data

    def query(self, command):
        data = self.query(self.sec_addr_serial + command)
        return data
