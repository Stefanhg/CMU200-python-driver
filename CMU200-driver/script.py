from CMU200 import Cmu200, listDevices
listDevices()
CMU = Cmu200(comm_port="ASRL3::INSTR", timeout=1, sec_addr_serial="1;")

CMU.spectrum.initialize_spectrum()
CMU.spectrum.start_freq(100E6)
#CMU.spectrum.center_freq(500E6)
CMU.spectrum.span_freq(200E6)  # Set the span to 200Mhz
CMU.spectrum.bandwidth_freq(100E3)  # Set the bandwidth to 100KHz
print(CMU.fetch.spectrum_marker_peak())
CMU.spectrum.go_to_local()
CMU.close()
