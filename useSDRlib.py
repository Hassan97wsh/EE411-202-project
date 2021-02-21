# This is an example of using mySDRlib.
from mySDRlib import SDR

# These are the inputs to pass to the SDR:
resolution = 50                     # Range resolution in m.
max_range = 5e3                     # Maximum range in m.
fc = int(5.8e9)                     # Carrier frequency.
fsx = 2                             # Fs = fsx*2*pulseBW. *has to be supported by the ADC
plutoIP = "192.168.2.1"
tx_attenuation = 0                  # Attenuation applied to Tx path (0dB to -90dB).
num_pulses = 2                     # Number of pulses per trigger.
# create sdr object:
sdr = SDR()


# set the parameters in program memory:
sdr.resolution = resolution
sdr.max_range = max_range
sdr.fc = fc
sdr.fsx = fsx
sdr.ip = plutoIP
sdr.tx_attenuation = tx_attenuation
sdr.num_pulses = num_pulses
# calculate the SDR parameters:
sdr.calculate()

# connect to SDR:
# sdr.connect()

# send setup(after calculation):
# sdr.send_setup()

# send and receive
# sdr.pulse()

print("Pulse BW:", sdr.pulse_BW/1000000, "MHz")
print("Pulse width:", sdr.pulse_width*1e9, "ns")
print("Sampling frequency:", sdr.sampling_frequency/1000000, "MHz")
print("Number of range steps:", sdr.range_steps)
print("Buffer size:", sdr.num_samples, 'samples.')
print(sdr.tx_signal)
