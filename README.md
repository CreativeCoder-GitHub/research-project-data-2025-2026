# Research Project Data 2025-2026: The Effect of Dopamine Exposure on Electroencephalogram Power Spectral Density
This repository contains all of the data from the study entitled 'The Effect of Dopamine Exposure on Electroencephalogram Power Spectral Density.'

## License
All files in this repository are licensed under the CC-BY-4.0 license.

## File Structure
The file structure of the repository is as follows:
- main branch
    - mean_graphs (This folder contains mean EEG PSD graphs.)
        - High_Mean_EEG_PSD.png
        - Low_Mean_EEG_PSD_Without_Outliers.png
        - Low_Mean_EEG_PSD.png
        - Medium_Mean_EEG_PSD.png
        - No_Mean_EEG_PSD.png
        - Quad_Graph_Mean_EEG_PSD_Without_Outliers.png
        - Quad_Graph_Mean_EEG_PSD.png
    - raw_data (This folder contains raw data of individual trials and IV levels. Each .npz file in this folder or its subfolders contains two numpy arrays: 'f' (frequencies in Hz) and 'psd' (EEG PSD).)
        - high_dopamine
            - Contains the raw data of the high dopamine exposure trials. File name format is trial_X.npz.
        - low_dopamine
            - Contains the raw data of the low dopamine exposure trials. File name format is trial_X.npz.
        - medium_dopamine
            - Contains the raw data of the medium dopamine exposure trials. File name format is trial_X.npz.
        - no_dopamine
            - Contains the raw data of the no dopamine exposure trials. File name format is trial_X.npz.
        - high_d_mean.npz
            - Contains the mean EEG PSD of all high dopamine exposure trials.
        - low_d_mean.npz
            - Contains the mean EEG PSD of all low dopamine exposure trials.
        - low_d_mean_without_outliers.npz
            - Contains the mean EEG PSD of all low dopamine exposure trials with outliers removed.
        - medium_d_mean.npz
            - Contains the mean EEG PSD of all medium dopamine exposure trials.
        - no_d_mean.npz
            - Contains the mean EEG PSD of all no dopamine exposure trials.
    - trial_graphs (This folder contains graphs of every individual trial.)
        - high_dopamine
            - Contains the graphs of each of the high dopamine exposure trials. File name format is trial_X.png.
        - low_dopamine
            - Contains the graphs of each of the low dopamine exposure trials. File name format is trial_X.png.
        - medium_dopamine
            - Contains the graphs of each of the medium dopamine exposure trials. File name format is trial_X.png.
        - no_dopamine
            - Contains the graphs of each of the no dopamine exposure trials. File name format is trial_X.png.
    - LICENSE
    - README.md
