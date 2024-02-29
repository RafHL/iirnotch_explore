# Noise folder example
RafHL

```
$ # Apply the 60 Hz notch filter to the given csv file
$ python filter_notch.py 2024-02-13-04-36-52.csv
$ # Plot both the filtered csv and the original csv's values and fft magnitude plots
$ python plot_noise.py *2024-02-13-04-36-52.csv
$ # Open both images to compare
$ viewnior *2024-02-13-04-36-52.png

$ # Show and save the plot and fft plot for the given csv
$ python filter_notch.py show 2024-02-13-04-36-52.csv

$ # Save the plot and fft plot for all csvs
$ python filter_notch.py *.csv
```
