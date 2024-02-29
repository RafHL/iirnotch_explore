import sys
import scipy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_noise(filename, show=False):
    fs = 10e6
    df = pd.read_csv(filename)

    times = df["Timestamp"].values
    value = df["HF Channel Value"].values
    fft   = abs(scipy.fft.rfft(value))
    x = np.linspace(0, 1, num=len(fft)) * fs/2

    fig, ax = plt.subplots(2,1)

    ax[0].set_title(filename)
    ax[0].set_xlabel("Timestamp")
    ax[0].set_ylabel("Value")
    ax[0].plot(times, value)

    ax[1].set_title("FFT Magnitude")
    ax[1].set_xlabel("Frequency (Hz)")
    ax[1].semilogx(x, fft, label="FFT")
    ax[1].semilogx([60, 60], [min(fft), max(fft)], linestyle='--', dashes=(5, 10), label="60 Hz", linewidth=1)
    ax[1].legend()

    fig.set_size_inches(16, 9, forward=True)
    fig.set_dpi(600)
    plt.tight_layout()

    plotname = filename[:filename.rfind('.')] + ".png"
    plt.savefig(plotname, dpi=fig.dpi, bbox_inches='tight')
    print(f"Saved plot: '{plotname}'")

    if show:
        plt.show()

    plt.close()

if len(sys.argv) > 1:
    show = sys.argv[1] == "show"

    if show:
        names = sys.argv[2:]
    else:
        names = sys.argv[1:]

    for name in names:
        plot_noise(name, show)

