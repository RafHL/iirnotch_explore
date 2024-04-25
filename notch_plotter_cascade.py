# Modified from the interactive plot example at https://stackoverflow.com/a/6697555
import pickle
import scipy
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin
from matplotlib.widgets import Slider, Button, RadioButtons
from fixedpoint import approx

def approx_filter(fs, w, num, den, dig):
    _num = approx(num, dig)
    _den = approx(den, dig)

    [print(f"{dig:2}'num[{i}] = {n:56.53f}") for i,n in enumerate(_num)]
    [print(f"{dig:2}'den[{i}] = {d:56.53f}") for i,d in enumerate(_den)]
    print()

    sys = scipy.signal.TransferFunction(_num, _den, dt=1/fs)
    w, mag, phase = scipy.signal.dbode(sys, w=w)

    return mag

fig = plt.figure()
ax = fig.add_subplot(111)

# Adjust the subplots region to leave some space for the sliders and buttons
fig.subplots_adjust(bottom=0.25)

digit = 31

# Notches
fs = 5e6
f_lo = 55
f_hi = 60
bw = 20

q_lo = f_lo/bw
q_hi = f_hi/bw

num_lo, den_lo = scipy.signal.iirnotch(f_lo, q_lo, fs=fs)
[print(f"num{f_lo}[{i}] = {n:56.53f}") for i,n in enumerate(num_lo)]
[print(f"den{f_lo}[{i}] = {d:56.53f}") for i,d in enumerate(den_lo)]
print()

num_hi, den_hi = scipy.signal.iirnotch(f_hi, q_hi, fs=fs)
[print(f"num{f_hi}[{i}] = {n:56.53f}") for i,n in enumerate(num_hi)]
[print(f"den{f_hi}[{i}] = {d:56.53f}") for i,d in enumerate(den_hi)]
print()


w = np.linspace(0, np.pi, num=2**int(fs).bit_length())

# Draw the initial plot
# The 'line' variable is used for modifying the line later
x = fs*w/np.pi/2
y_lo = approx_filter(fs, w, num_lo, den_lo, digit)
y_hi = approx_filter(fs, w, num_hi, den_hi, digit)
ax.semilogx(x, y_lo, label=f"{f_lo}")
ax.semilogx(x, y_hi, label=f"{f_hi}")
ax.semilogx(x, y_lo*y_hi, label=f"Cascade")
ax.legend()

plt.show()
