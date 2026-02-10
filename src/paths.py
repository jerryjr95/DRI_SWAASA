import os

# Project root = parent of src folder
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Data paths
RAW_AUDIO_DIR = os.path.join(PROJECT_ROOT, "data", "raw", "audio")
PROCESSED_AUDIO_DIR = os.path.join(PROJECT_ROOT, "data", "processed", "audio")
FEATURES_CSV = os.path.join(PROJECT_ROOT, "data", "processed", "features.csv")



# Plots
PLOTS_DIR = os.path.join(PROJECT_ROOT, "plots")
SNR_PLOTS_DIR = os.path.join(PLOTS_DIR, "snr")
SPECTRAL_PLOTS_DIR = os.path.join(PLOTS_DIR, "spectral")
MFCC_PLOTS_DIR = os.path.join(PLOTS_DIR, "mfcc")

# Ensure folders exist
for path in [
    PROCESSED_AUDIO_DIR,
    SNR_PLOTS_DIR,
    SPECTRAL_PLOTS_DIR,
    MFCC_PLOTS_DIR
]:
    os.makedirs(path, exist_ok=True)
