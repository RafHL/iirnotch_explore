# Modified from the interactive plot example at https://stackoverflow.com/a/6697555
import sys
import scipy
import pandas as pd

def filter_csv(num, den, filename):
    df = pd.read_csv(filename)

    times = df["Timestamp"].values
    value = df["HF Channel Value"].values

    filtered = scipy.signal.lfilter(num, den, value)

    odf = pd.DataFrame({"Timestamp": times, "HF Channel Value": filtered})
    dots = filename.split('.')
    dots[-2] += "_filtered"
    csvname = '.'.join(dots)
    odf.to_csv(csvname, index=False)
    print(f"Saved csv: '{csvname}'")

# 1st filter:
#fs = 10e6
#f0 = 60
#bw = 20
#q = f0/bw
# Feedback: Q too high, want 55 Hz down too. 5 MHz sampling freq, not 10 MHz

# cheby2
fs = 5e6
f_lo = 54
f_hi = 61
num, den = scipy.signal.cheby2(1, 12, [f_lo, f_hi], fs=fs, btype='bandstop')

if len(sys.argv) > 1:
    names = sys.argv[1:]

    for name in names:
        filter_csv(num, den, name)

