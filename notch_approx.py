# Modified from the interactive plot example at https://stackoverflow.com/a/6697555
import pickle
import scipy
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin
from matplotlib.widgets import Slider, Button, RadioButtons
from fixedpoint import approx

def approx_filter(w, num, den, dig):
    _num = approx(num, dig)
    _den = approx(den, dig)

    print("num for", dig, _num)
    print("den for", dig, _den)
    print()

    sys = scipy.signal.TransferFunction(_num, _den, dt=1/fs)
    w, mag, phase = scipy.signal.dbode(sys, w=w)

    return mag

fig = plt.figure()
ax = fig.add_subplot(111)

# Adjust the subplots region to leave some space for the sliders and buttons
fig.subplots_adjust(bottom=0.25)

digit = 52

# Filter 1:
#fs = 10e6
#f0 = 60
#bw = 20
#q = f0/bw
#num, den = scipy.signal.iirnotch(f0, q, fs=fs)

## cheby2 high pass not as good attenuation at 50-60 Hz
#fs = 5e6
#f_hi = 80
#num, den = scipy.signal.cheby2(1, 3, f_hi, fs=fs, btype='highpass')

## Butter example from https://dsp.stackexchange.com/a/49435
## Butter reference from https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
#fs = 5e6
#f_lo = 50
#f_hi = 70
#num, den = scipy.signal.butter(1, [f_lo, f_hi], fs=fs, btype='bandstop')

# cheby2
fs = 5e6
f_lo = 54
f_hi = 61
num, den = scipy.signal.cheby2(1, 12, [f_lo, f_hi], fs=fs, btype='bandstop')

w = np.linspace(0, np.pi, num=2**int(fs).bit_length())

# Draw the initial plot
# The 'line' variable is used for modifying the line later
[line] = ax.semilogx(fs*w/np.pi/2, approx_filter(w, num, den, digit))
ax.set_ylim([-100, 20])

# Modified from https://stackoverflow.com/a/26835559
try:
    the_mags = pickle.load(open("the_mags.pickle", "rb"))
except (OSError, IOError) as e:
    the_mags = np.ones([53, w.size])
    for i in range(53):
        the_mags[i] *= approx_filter(w, num, den, i)
    pickle.dump(the_mags, open("the_mags.pickle", "wb"))

# Add one slider for tweaking the parameters
# Define an axes area and draw a slider in it
digit_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03])
digit_slider = Slider(digit_slider_ax, 'Digits', 0, 52, valinit=digit, valstep=1)

# Define an action for modifying the line when any slider's value changes
def sliders_on_changed(val):
    line.set_ydata(the_mags[int(digit_slider.val)])
    fig.canvas.draw_idle()
digit_slider.on_changed(sliders_on_changed)

plt.show()
