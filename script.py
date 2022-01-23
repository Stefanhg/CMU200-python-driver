

import CMU200


CMU = CMU200.Cmu200("ASRL6::INSTR", 1, "1;")

CMU.spectrum.start_freq(100E6)
#CMU.spectrum.stop_freq(200E6)
