import numpy as np

class AdaptiveNeuron:
    def __init__(self, input_size, learning_rate=0.01):
        self.weights = np.random.randn(input_size) * 0.01
        self.bias = 0.0
        self.learning_rate = learning_rate

    def predict(self, x):
        return np.dot(self.weights, x) + self.bias

    def calculate_error(self, desired_output, predicted_output):
        return desired_output - predicted_output

    def update_weights(self, x, error):
        self.weights += self.learning_rate * error * x
        self.bias += self.learning_rate * error

    def train_single_step(self, x, desired_output):
        predicted_output = self.predict(x)
        error = self.calculate_error(desired_output, predicted_output)
        self.update_weights(x, error)
        return predicted_output, error