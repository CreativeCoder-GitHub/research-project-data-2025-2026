import matplotlib.pyplot as plt
import numpy as np
import calculations

plt.style.use('grayscale')

fig, axs = plt.subplots(2, 2, figsize=(8, 8))

def make_subplot(x, y, idx, title_idx=None):
    with np.load(calculations.FILES[idx][0]) as f:
        frequencies, psd = (f['f'], f['psd'])
    axs[x, y].set_title(calculations.FILES[idx][1])
    if title_idx: axs[x, y].set_title(calculations.FILES[title_idx][1])
    axs[x, y].set_xlabel('Frequency (Hz)')
    axs[x, y].set_ylabel('Power (V^2/Hz)')
    axs[x, y].set_xlim([1, 100])
    axs[x, y].grid(True, linestyle='--', alpha=0.5)
    axs[x, y].plot(frequencies, psd)

remove_outliers = True # Can set to True or False depending on whether you want to remove outliers from the graph.

make_subplot(0, 0, 0)
make_subplot(0, 1, 4 if remove_outliers else 1, 1)
make_subplot(1, 0, 2)
make_subplot(1, 1, 3)

plt.suptitle(f'Mean Electroencephalogram (EEG) Power Spectral Density (PSD) Graphs{" (Outliers Removed)" if remove_outliers else ""}')
plt.tight_layout()
plt.show()