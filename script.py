from CMU200 import Cmu200

CMU = Cmu200(comm_port="ASRL6::INSTR", timeout=1, sec_addr_serial="1;")
CMU.spectrum.start_freq(100E6)
CMU.close()
