import numpy as np
from scipy import stats
import os
import glob

FILES = [
    ('.\\raw_data\\no_dopamine_mean.npz','No Dopamine Trials'),
    ('.\\raw_data\\low_dopamine_mean.npz','Low Dopamine Trials'),
    ('.\\raw_data\\medium_dopamine_mean.npz','Medium Dopamine Trials'),
    ('.\\raw_data\\high_dopamine_mean.npz','High Dopamine Trials'),
    ('.\\raw_data\\low_dopamine_mean_without_outliers.npz','Low Dopamine Trials (Outliers Removed)'),
]

def get_npz_files(folder_path):
    # Get a list of all .npz files in the target folder
    search_path = os.path.join(folder_path, "*.npz")
    file_list = glob.glob(search_path)
    if not file_list: raise FileNotFoundError(f"No .npz files found in {folder_path}")
    return file_list

def general_calculate(folder_path: str):
    file_list = get_npz_files(folder_path)
    all_psds = []

    for file in file_list:
        with np.load(file) as data: all_psds.append(data['psd'])

    psd_means = np.array([np.mean(i) for i in all_psds])
    std = np.std(psd_means)
    mean = np.mean(psd_means)
    median = np.median(psd_means)
    mode = stats.mode(psd_means)
    mode = None if mode.count == 1 else mode.mode
    outliers = []

    for i in range(len(psd_means)):
        z_score = (psd_means[i] - mean) / std
        if abs(z_score) > 2: outliers.append(i)

    return {'outliers': outliers, 
            'std': std, 
            'mean': mean, 
            'median': median, 
            'mode': mode,
            }

def average_psd_from_folder(folder_path, remove_outliers: bool = False):
    """
    Loads all .npz files in a folder, averages the 'psd' data, 
    and returns (frequencies, averaged_psd).
    """
    file_list = get_npz_files(folder_path)
    if remove_outliers:
        outlier_idxs = general_calculate(folder_path)['outliers']
        print('Outliers at', outlier_idxs)
        for i in outlier_idxs: file_list.pop(i)

    all_psds = []
    freqs = None

    for file in file_list:
        with np.load(file) as data:
            all_psds.append(data['psd'])
            if freqs is None: freqs = data['f']

    mean_psd = np.mean(all_psds, axis=0)
    print(f"Successfully averaged {len(file_list)} trials from: {folder_path}")
    return freqs, mean_psd

def get_psds_from_folder(folder_path):
    """
    Loads all .npz files in a folder, and return their mean 'psd' data.
    """
    file_list = get_npz_files(folder_path)
    all_psds = []
    i = 1
    for file in file_list:
        with np.load(file) as data:
            # Append PSD to list; assumes shape is (n_frequencies, n_sensors)
            all_psds.append({'trial': i, 'mean_psd': float(np.mean(data['psd']))})
            i += 1
    return all_psds

if __name__ == '__main__':
    # averages = average_psd_from_folder('.\\raw_data\\low_dopamine', True)
    # np.savez('.\\raw_data\\low_dopamine_mean_without_outliers.npz',  f=averages[0], psd=averages[1])

    for i in FILES:
        with np.load(i[0]) as f:
            psd = f['psd']
            print(i[1], 'Mean EEG PSD:\t', np.mean(psd))

    print('')
    print('================================================================')
    print('')

    x = general_calculate('.\\raw_data\\no_d')
    print(f'No Dopamine Trials Outlier Count of {len(x["outliers"])} and Standard Deviation of {x["std"]}')
    print(f'No Dopamine Trials Mean\t', x['mean'])
    print(f'No Dopamine Trials Median\t', x['median'])
    print(f'No Dopamine Trials Mode\t', x['mode'])
    print()

    x = general_calculate('.\\raw_data\\low_d')
    print(f'Low Dopamine Trials Outlier Count of {len(x["outliers"])} and Standard Deviation of {x["std"]}')
    print(f'Low Dopamine Trials Mean\t', x['mean'])
    print(f'Low Dopamine Trials Median\t', x['median'])
    print(f'Low Dopamine Trials Mode\t', x['mode'])
    print()

    x = general_calculate('.\\raw_data\\medium_d')
    print(f'Medium Dopamine Trials Outlier Count of {len(x["outliers"])} and Standard Deviation of {x["std"]}')
    print(f'Medium Dopamine Trials Mean\t', x['mean'])
    print(f'Medium Dopamine Trials Median\t', x['median'])
    print(f'Medium Dopamine Trials Mode\t', x['mode'])
    print()

    x = general_calculate('.\\raw_data\\high_D')
    print(f'High Dopamine Trials Outlier Count of {len(x["outliers"])} and Standard Deviation of {x["std"]}')
    print(f'High Dopamine Trials Mean \t', x['mean'])
    print(f'High Dopamine Trials Median\t', x['median'])
    print(f'High Dopamine Trials Mode\t', x['mode'])