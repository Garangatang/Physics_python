# approximately solves a DE with Euler's method
# improved Euler's method and Runge Kutta have been added
# the DE is of the form
#  dy/dx = f(x,y)
#  y(x0) = y0
#
# Does tables instead of plotting
import math
import matplotlib.pyplot as plt
import numpy as np

# f(x,y) from definition of DE
def f(x,y):
  return (y**2)/x

# the true solution
def ytrue(x):
  return (-1/((math.log(x))-1))

# Euler's method
def euler(f,x0,y0,h,n):
  x = [0.0]*(n+1) # n+1 x values
  y = [0.0]*(n+1) # n+1 y values
  # set initial condition
  x[0] = x0
  y[0] = y0
  for i in range(n):
      x[i+1] = x[i] + h
      y[i+1] = y[i] + h*f(x[i],y[i]) # Euler's method
      if abs(x[i+1] % 0.2) < 1e-9:
        err = abs((ytrue(x[i+1]) - y[i+1])/ytrue(x[i+1]))*100
        # print x[i+1], y[i+1], ytrue(x[i+1]), err
        print("%5.3g %10.5g %10.5g %5.5g" % (x[i+1], y[i+1], ytrue(x[i+1]), err))
  return x,y

# Improved Euler's method (aka Heun's method)
def improved_euler(f,x0,y0,h,n):
  x = [0.0]*(n+1) # n+1 x values
  y = [0.0]*(n+1) # n+1 y values
  # set initial condition
  x[0] = x0
  y[0] = y0
  for i in range(n):
      x[i+1] = x[i] + h
      k1 = f(x[i],y[i])
      u = y[i] + h*k1 # Euler's step
      k2 = f(x[i+1],u) # estimated slope of y(x) at x[i+1]
      y[i+1] = y[i] + (h/2)*(k1+k2) # update
      if abs(x[i+1] % 0.2) < 1e-9:
        err = abs((ytrue(x[i+1]) - y[i+1])/ytrue(x[i+1]))*100
        # print x[i+1], y[i+1], ytrue(x[i+1]), err
        print("%5.3g %10.5g %10.5g %5.5g" % (x[i+1], y[i+1], ytrue(x[i+1]), err))
  return x,y


# Runge-Kutta 4-5 method
def runge_kutta(f,x0,y0,h,n):
  x = [0.0]*(n+1) # n+1 x values
  y = [0.0]*(n+1) # n+1 y values
  # set initial condition
  x[0] = x0
  y[0] = y0
  for i in range(n):
      x[i+1] = x[i] + h
      k1 = f(x[i],y[i])
      k2 = f(x[i]+h/2,y[i]+h*k1/2)
      k3 = f(x[i]+h/2,y[i]+h*k2/2)
      k4 = f(x[i+1],y[i]+h*k3)
      y[i+1] = y[i] + (h/6)*(k1+2*k2+2*k3+k4) # update
      if abs(x[i+1] % 0.2) < 1e-9:
        err = abs((ytrue(x[i+1]) - y[i+1])/ytrue(x[i+1]))*100
        # print x[i+1], y[i+1], ytrue(x[i+1]), err
        print("%5.3g %10.5g %10.5g %5.5g" % (x[i+1], y[i+1], ytrue(x[i+1]), err))
  return x,y




x0 = 1; y0 = 1;
h = 0.01  # step size
n = 100  # number of steps to take

# change this to the method you want to use.
xeuler,yeuler  = euler(f,x0,y0,h,n)
