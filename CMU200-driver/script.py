from CMU200 import Cmu200

CMU = Cmu200(comm_port="ASRL6::INSTR", timeout=1, sec_addr_serial="1;")

CMU.spectrum.center_freq(100E6)
CMU.spectrum.span_freq(200E6)  # Set the span to 200Mhz
CMU.spectrum.bandwidth_freq(100E3)  # Set the bandwidth to 100KHz
print(CMU.fetch.spectrum_marker_peak())
CMU.close()
