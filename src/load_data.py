import mne
import mne.io

def load_def(file_path):
    return mne.io.read_raw_edf(file_path, preload=True)

if __name__ == "__main__":
    file_path = "/Users/krithikasaravanan/physionet.org/files/eegmmidb/1.0.0/S001/S001R01.edf"
    raw = mne.io.read_raw_edf(file_path) 
    print(raw.info)
    raw.plot(duration = 5)
