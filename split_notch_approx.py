import scipy
import matplotlib.pyplot as plt
import numpy as np
from fixedpoint import approx

fs = 10e6
f0 = 60
bw = 5

q = f0/bw
num, den = scipy.signal.iirnotch(f0, q, fs=fs)
print("num is", num)
print("den is", den)
print()

fig, ax = plt.subplots(6,1)

for dig in range(60):
    _num = approx(num, dig)
    _den = approx(den, dig)

    print("num for", dig, _num)
    print("den for", dig, _den)
    print()

    sys = scipy.signal.TransferFunction(_num, _den, dt=1/fs)
    w, mag, phase = scipy.signal.dbode(sys, n=2**20)

    ax[int(dig/10)].semilogx(w, mag, label=f'{dig} digits')

for axis in ax:
    axis.legend()

plt.show()

