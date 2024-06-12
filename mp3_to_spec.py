import os
import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np

# Define the source directory (mp3-clipped) and the target directory (spectrogram)
source_dir = './data/mp3-clipped'
target_dir = './data/spectrogram'

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Function to convert mp3 to mel spectrogram and save it
def mp3_to_mel_spectrogram(file_path, target_folder):
    # Load the audio file
    y, sr = librosa.load(file_path)
    
    # Generate the mel spectrogram
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    
    # Convert to decibels
    S_dB = librosa.power_to_db(S, ref=np.max)
    
    # Plot and save the spectrogram
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel', fmax=8000)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequency spectrogram')
    plt.tight_layout()
    
    # Generate spectrogram filename
    base_filename = os.path.basename(file_path)
    spectrogram_filename = f"{os.path.splitext(base_filename)[0]}.png"
    spectrogram_path = os.path.join(target_folder, spectrogram_filename)
    
    # Save the figure
    plt.savefig(spectrogram_path)
    plt.close()

# Iterate over all mp3 files in the source directory and convert them to mel spectrograms
for filename in os.listdir(source_dir):
    if filename.endswith(".mp3"):
        file_path = os.path.join(source_dir, filename)
        mp3_to_mel_spectrogram(file_path, target_dir)