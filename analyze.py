#!/usr/bin/env python
import scikits.audiolab as audiolab
import scipy
# from matplotlib import pylab

x, fs, nbits = audiolab.wavread('demo.wav')
audiolab.play(x, fs)
N = 4*fs    # four seconds of audio
X = scipy.fft(x[:N])
Xdb = 20*scipy.log10(scipy.absolute(X))
f = scipy.linspace(0, fs, N, endpoint=False)

print "--- N -----------------------------------------------------------------"
print N
print "--- X -----------------------------------------------------------------"
print X
print "--- Xdb ---------------------------------------------------------------"
print Xdb
print "--- f -----------------------------------------------------------------"
print f
# pylab.plot(f, Xdb)
# pylab.xlim(0, 5000)   # view up to 5 kHz
#
# H = 2  # ??
#
# Y = X * H
# y = scipy.real(scipy.ifft(Y))
