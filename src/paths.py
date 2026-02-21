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

# Direct audio extraction plots (plots_from_audio)
PLOTS_FROM_AUDIO_DIR = os.path.join(PLOTS_DIR, "plots_from_audio")
MFCC_FROM_AUDIO_DIR = os.path.join(PLOTS_FROM_AUDIO_DIR, "mfcc")
SPECTRAL_FROM_AUDIO_DIR = os.path.join(PLOTS_FROM_AUDIO_DIR, "spectral")
SPECTROGRAMS_FROM_AUDIO_DIR = os.path.join(PLOTS_FROM_AUDIO_DIR, "spectrograms")
CHROMA_FROM_AUDIO_DIR = os.path.join(PLOTS_FROM_AUDIO_DIR, "chroma")
MFCC_HEATMAPS_FROM_AUDIO_DIR = os.path.join(PLOTS_FROM_AUDIO_DIR, "mfcc_heatmaps")
POLLUTANTS_GRAPHS_DIR = os.path.join(PLOTS_DIR, "pollutants_graphs")

# Individual MFCC coefficient folders (in plots_from_audio)
MFCC_INDIVIDUAL_FROM_AUDIO = [os.path.join(MFCC_FROM_AUDIO_DIR, f"mfcc{i}") for i in range(1, 14)]

# Individual spectral feature folders (in plots_from_audio)
SPECTRAL_FEATURES = [
    "spectral_centroid",
    "spectral_rolloff",
    "spectral_spread",
    "spectral_flatness",
    "spectral_skewness",
    "spectral_kurtosis",
    "spectral_std",
    "spectral_slope",
    "spectral_decrease"
]
SPECTRAL_INDIVIDUAL_FROM_AUDIO = [os.path.join(SPECTRAL_FROM_AUDIO_DIR, f) for f in SPECTRAL_FEATURES]

# Pollutants graphs subdirectories
POLLUTANTS_MONTHLY_DIR = os.path.join(POLLUTANTS_GRAPHS_DIR, "monthly_plots")
POLLUTANTS_TREND_DIR = os.path.join(POLLUTANTS_GRAPHS_DIR, "trend_analysis")

# Ensure folders exist
paths_to_create = [
    PROCESSED_AUDIO_DIR,
    SNR_PLOTS_DIR,
    SPECTRAL_PLOTS_DIR,
    MFCC_PLOTS_DIR,
    PLOTS_FROM_AUDIO_DIR,
    MFCC_FROM_AUDIO_DIR,
    SPECTRAL_FROM_AUDIO_DIR,
    SPECTROGRAMS_FROM_AUDIO_DIR,
    CHROMA_FROM_AUDIO_DIR,
    MFCC_HEATMAPS_FROM_AUDIO_DIR,
    POLLUTANTS_GRAPHS_DIR,
    POLLUTANTS_MONTHLY_DIR,
    POLLUTANTS_TREND_DIR
]

# Add individual subdirectories
paths_to_create.extend(MFCC_INDIVIDUAL_FROM_AUDIO)
paths_to_create.extend(SPECTRAL_INDIVIDUAL_FROM_AUDIO)

for path in paths_to_create:
    os.makedirs(path, exist_ok=True)
