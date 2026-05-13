import numpy as np

def generate_clean_signal(duration=1.0, sampling_rate=1000, frequency=5):
    t = np.linspace(0, duration, int(sampling_rate * duration))
    clean_signal = np.sin(2 * np.pi * frequency * t)
    return t, clean_signal

def generate_noise(signal_length, noise_level=0.5):
    return noise_level * np.random.randn(signal_length)

def generate_noisy_signal(clean_signal, noise):
    return clean_signal + noise