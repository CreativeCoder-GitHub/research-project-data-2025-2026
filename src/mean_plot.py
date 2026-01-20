import matplotlib.pyplot as plt
import numpy as np
import calculations

plt.style.use('grayscale')

def make_separate_figure(file_path, title):
    # Create a new, independent figure
    plt.figure(figsize=(8, 6))
    
    with np.load(file_path) as f:
        frequencies, psd = (f['f'], f['psd'])
    
    plt.plot(frequencies, psd)
    plt.title(f'Mean EEG PSD: {title}')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power (V^2/Hz)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim([1, 100])
    plt.tight_layout()

# Generate a unique figure for every entry in FILES (Mean EEG PSD)
for file_path, label in calculations.FILES: make_separate_figure(file_path, label)
plt.show()