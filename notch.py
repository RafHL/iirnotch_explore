import scipy
import matplotlib.pyplot as plt
import numpy as np

fs = 10e6
f0 = 60
bw = 5

q = f0/bw
num, den = scipy.signal.iirnotch(f0, q, fs=fs)
print("num is", num)
print("den is", den)

sys = scipy.signal.TransferFunction(num, den, dt=1/fs)
w, mag, phase = scipy.signal.dbode(sys, n=2**20)

plt.figure()
plt.semilogx(w, mag)
plt.figure()
plt.semilogx(w, phase)
plt.show()

