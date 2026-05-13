import numpy as np
from models.adaptive_neuron import AdaptiveNeuron

class LMSFilter:
    def __init__(self, filter_order=4, learning_rate=0.01):
        self.filter_order = filter_order
        self.neuron = AdaptiveNeuron(filter_order, learning_rate)

    def filter_signal(self, noisy_signal, desired_signal):
        n_samples = len(noisy_signal)
        output_signal = np.zeros(n_samples)
        error_signal = np.zeros(n_samples)

        # Iterate through the signal using a sliding window
        for i in range(self.filter_order, n_samples):
            x = noisy_signal[i - self.filter_order:i]
            
            # Predict and update using the neuron
            prediction, error = self.neuron.train_single_step(x, desired_signal[i])
            
            output_signal[i] = prediction
            error_signal[i] = error

        return output_signal, error_signal