import mne
import mne.io

def load_def(file_path):
    raw = mne.io.read_raw_edf(file_path, preload=False)
    return raw

if __name__ == "__main__":
    file_path = "/Users/krithikasaravanan/data/S001R01.edf"
    raw = mne.io.read_raw_edf(file_path) 
    print(raw.info)
    raw.plot(duration = 5)