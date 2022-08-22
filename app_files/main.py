import pandas as pd
import scipy.io
import os
import mne
from halo import Halo
from secrets import Secrets

folder = Secrets().cerebro_long_eegs_mat_folder

def visualize_mat_eeg(filename, folder=folder, scalings=100, start_time=0, duration=60):
    '''
    Get as input an EEG filename (mat file) and plot by default the first 60 seconds
    interactive window.
    '''
    spinner = Halo(text='Loading...', spinner='dots')
    spinner.start()
    mat = scipy.io.loadmat(os.path.join(folder,filename))
    fs = mat['fs'][0][0]
    ch_labels = [x[0].upper() for x in mat['ch_labels'][0]]
    eeg_data = list(list(x) for x in mat['eeg_data'])
    dict_data = dict(zip(ch_labels,eeg_data))
    df = pd.DataFrame(dict_data)
    df = df.T.sort_index().T
    info = mne.create_info(ch_names = list(df.columns), sfreq = fs, ch_types=['eeg']*len(df.columns))
    raw = mne.io.RawArray(df.T, info)
    raw.plot(start=start_time, duration=duration, scalings={'eeg': scalings}, block=True)
    spinner.stop()