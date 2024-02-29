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
    odf.to_csv("filtered_" + filename, index=False)

fs = 10e6
f0 = 60
bw = 20
q = f0/bw
num, den = scipy.signal.iirnotch(f0, q, fs=fs)

if len(sys.argv) > 1:
    names = sys.argv[1:]

    for name in names:
        filter_csv(num, den, name)

