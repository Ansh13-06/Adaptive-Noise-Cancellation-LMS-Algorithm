from signals.signal_generator import generate_clean_signal, generate_noise, generate_noisy_signal
from filters.lms_filters import LMSFilter
from visualization.plotter import SignalPlotter

# STEP 1 — Generate Clean Signal
print("Generating clean signal...")
sampling_rate = 1000
t, clean_signal = generate_clean_signal(duration=2.0, sampling_rate=sampling_rate, frequency=5)

# STEP 2 — Generate Noise
print("Generating noise...")
noise = generate_noise(len(clean_signal), noise_level=0.5)

# STEP 3 — Create Noisy Signal
print("Adding noise to signal...")
noisy_signal = generate_noisy_signal(clean_signal, noise)

# STEP 4 — LMS Adaptive Filtering
print("Applying LMS adaptive filter...")
lms_filter = LMSFilter(filter_order=8, learning_rate=0.01)
filtered_signal, error_signal = lms_filter.filter_signal(noisy_signal, clean_signal)

# STEP 5 — Visualization
print("Displaying results...")
SignalPlotter.plot_signals(t, clean_signal, noisy_signal, filtered_signal)
SignalPlotter.plot_error(error_signal)

print("Project execution completed successfully!")