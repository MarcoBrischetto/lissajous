from lissajous import generate_graph
import numpy as np

#Amplitude
A1 = 10
A2 = 10

#Frequency
f1 = 9
f2 = 10

#Angular shift between curves
shift = np.pi/2

#generate, compose and plot 
generate_graph( A1, A2, f1, f2, shift)