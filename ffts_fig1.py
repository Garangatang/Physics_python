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
g = (np.cos(2*np.pi*f0*t)).astype(complex)  # cos(2*pi*f0*t) + 0*1j

freq=np.fft.fftfreq(N, d=dt) # sets pu array of frequency sample. not straightforward
# FFT!
G = np.fft.fft(g) # this is the fft! G is sampled at frequencies freq

#inverse FFT
gg = np.fft.ifft(G)

# confirm g, gg are the same, to roughly machine precision
print('sum square residuals, g-gg:',np.sum(np.absolute(g-gg)**2))

#plot it

pl.subplot(211)
#pl.axis([0,N,-1.1,1.1])
pl.ylim(-1.1,1.6)
pl.xlim(-0.01*Tmax,1.12*Tmax)
pl.text(0.55*Tmax,1.25,'g(t) = cos(2*pi*f0*t)',size=14)
pl.text(1.01*Tmax,g[-1].real-0.05,'real',color='r',size=14)
pl.text(1.01*Tmax,g[-1].imag-0.05,'imag',color='b',size=14)
pl.xlabel('t (s)',size=16)
pl.ylabel('g(t)',size=16)
pl.plot(t,g.real,'r-',t,g.imag,'b-',zorder=1)

pl.subplot(212)
pl.xlabel('f (Hz)',size=16)
pl.ylabel('G(f)',size=16)
pl.plot(freq,G.real,'r',freq,G.imag,'b')
pl.text(0.5*freq.max(),30,'f0 = '+("%4.2f")%(f0)+' Hz',size=14)

pl.tight_layout()


pl.savefig("fftcos.png")
#show()
