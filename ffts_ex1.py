import numpy as np
import matplotlib
matplotlib.use('Agg') # for terminal mode only
import pylab as pl

# define the domain
N=128 # number of samples
Tmax=0.1*N  # time span of the sample, system is periodic on this interval
dt=Tmax/N
t = np.linspace(0,Tmax,N,endpoint=False) # go to T-dt, don't include endpoint @ Tmax

# define our function g(t)
f0=12/Tmax # frequency, fit 12 cycles in Tmax
g = np.exp(2*np.pi*np.imag(1)*f0*t) #(np.sin(2*np.pi*f0*t)).astype(complex)  # cos(2*pi*f0*t) + 0*1j

freq=np.fft.fftfreq(N, d=dt) # sets pu array of frequency sample. not straightforward
# FFT!
G = np.fft.fft(g) # this is the fft! G is sampled at frequencies freq

#inverse FFT
gg = np.fft.ifft(G)

# confirm g, gg are the same, to roughly machine precision
print('sum square residuals, g-gg:',np.sum(np.absolute(g-gg)**2))

#plot it, 3 panels, first is g, nextt is G, and the g from the inverse xform of G
# time domain g(t)
pl.subplot(311)
pl.xlabel('t (s)',size=16)
pl.ylabel('g(t)',size=16)
pl.plot(t,g.real,'r-',t,g.imag,'b-')

# frequency domain G(freq)
pl.subplot(312)
pl.xlabel('f (Hz)',size=16)
pl.ylabel('G(f)',size=16)
# sort freq and G, they are not fully smallest to largest/ just for plotting
msk = np.argsort(freq)
pl.plot(freq[msk],G[msk].real,'r',freq[msk],G[msk].imag,'b')

# time domain g(t)
pl.subplot(313)
pl.xlabel('t (s)',size=16)
pl.ylabel('new g(t)',size=16)
pl.plot(t,gg.real,'r-',t,gg.imag,'b-')

# pl.show()
pl.savefig("fftexample.png")
#show()

#import os
#os.system('convert fftexample.png ~/public_hml/tmp.jpg')
