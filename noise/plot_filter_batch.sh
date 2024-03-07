
# Plot all the input csvs
python ../plot_noise.py input_csvs/*
mkdir -p input_plots
mv input_csvs/*.png -t input_plots

# Apply the filter to the input csvs
python ../filter_notch.py input_csvs/*
mkdir -p filtered_csvs
mv input_csvs/filtered* -t filtered_csvs


# Plot the filtered csvs
python ../plot_noise.py filtered_csvs/*
mkdir -p filtered_plots
mv filtered_csvs/*.png -t filtered_plots

