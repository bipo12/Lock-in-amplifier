# Lock_In amplifier

This script employs the principles of an ideal phase-sensitive amplifier, combined with a low-pass Finite Impulse Response (FIR) filter. The filter is implemented using a normalized sinc function and augmented by a Blackman window to compute both in-phase and quadrature scales.
The resultant output signal is determined as the magnitude R, derived from the square root of the sum of squares of the in-phase and quadrature component. 
The utilization of an ideal phase-sensitive amplifier ensures that the phase information is appropriately considered, while the low-pass FIR filter aids in refining the signal by attenuating high-frequency components. 
This approach can find application in diverse fields such as communication systems, radar signal processing, spectroscopy and various other domains where detection of signal with precise frequency is essential.
