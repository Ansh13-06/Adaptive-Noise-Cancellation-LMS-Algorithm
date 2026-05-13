import matplotlib.pyplot as plt

class SignalPlotter:
    @staticmethod
    def plot_signals(t, clean_signal, noisy_signal, filtered_signal):
        plt.figure(figsize=(12, 8))

        plt.subplot(3, 1, 1)
        plt.plot(t, clean_signal, color='green')
        plt.title("Clean Signal (Reference)")
        
        plt.subplot(3, 1, 2)
        plt.plot(t, noisy_signal, color='red', alpha=0.7)
        plt.title("Noisy Signal (Input)")

        plt.subplot(3, 1, 3)
        plt.plot(t, filtered_signal, color='blue')
        plt.title("Filtered Signal (Output)")

        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_error(error_signal):
        plt.figure(figsize=(10, 4))
        plt.plot(error_signal, color='orange')
        plt.title("LMS Error Convergence")
        plt.xlabel("Samples")
        plt.ylabel("Error")
        plt.grid(True)
        plt.show()