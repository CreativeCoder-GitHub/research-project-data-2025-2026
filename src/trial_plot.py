import matplotlib.pyplot as plt
import numpy as np

plt.style.use('grayscale')

def plot_psd_from_file(file_path: str, title: str):
    fig, axs = plt.subplots(1, 1, figsize=(8, 6))
    with np.load(file_path) as f: frequencies, psd = (f['f'], f['psd'])

    # Filter frequencies below 140Hz
    frequencies = [i for i in frequencies if i < 140]
    psd = psd[0:len(frequencies)]
    
    axs.plot(frequencies, psd)
    axs.set_title(title)
    axs.set_xlabel("Frequency (Hz)")
    axs.set_ylabel("Power (V^2/Hz)")
    axs.grid(True, linestyle='--', alpha=0.5)
    axs.set_xlim([1, 100])
    
    return fig, axs

FOLDERS = [
    ('no_dopamine', 'No Dopamine Exposure'),
    ('low_dopamine', 'Low Dopamine Exposure'),
    ('medium_dopamine', 'Medium Dopamine Exposure'),
    ('high_dopamine', 'High Dopamine Exposure'),
]

for folder_path, label in FOLDERS:
    for i in range(15):
        trial = i + 1 # The range function goes from 0 to stop non-inclusive. This corrects that.
        fig, _ = plot_psd_from_file(f'.\\raw_data\\{folder_path}\\trial_{trial}.npz', f'{label}: Trial {trial}')
        fig.savefig(f'.\\trial_graphs\\{folder_path}\\trial_{trial}.png')
        plt.close(fig)