import mne

def preprocess(raw):
    #Filter signal
    raw.filter(0.5, 40)

    #Get events - labels
    events, event_id = mne.events_from_annotations(raw)

    #Create epochs - samples
    epochs = mne.Epochs(raw, events, event_id, tmin=0, tmax=2, preload=True)
    
    return epochs