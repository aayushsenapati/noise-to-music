import os
from pydub import AudioSegment

# Define the source and target directories
source_dir = './data/mp3'
target_dir = './data/mp3-clipped'

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Function to split mp3 file into 5 sec clips
def split_mp3(file_path, target_folder):
    # Load the mp3 file
    audio = AudioSegment.from_mp3(file_path)
    
    # Calculate the number of 5 sec clips
    clip_duration = 5000  # 5000 milliseconds = 5 seconds
    number_of_clips = len(audio) // clip_duration
    
    # Split and export each clip
    for i in range(number_of_clips):
        start_time = i * clip_duration
        end_time = (i + 1) * clip_duration
        clip = audio[start_time:end_time]
        
        # Generate clip filename
        base_filename = os.path.basename(file_path)
        clip_filename = f"{os.path.splitext(base_filename)[0]}_part{i}.mp3"
        clip_path = os.path.join(target_folder, clip_filename)
        
        # Export clip
        clip.export(clip_path, format="mp3")

# Iterate over all mp3 files in the source directory and split them
for filename in os.listdir(source_dir):
    if filename.endswith(".mp3"):
        file_path = os.path.join(source_dir, filename)
        split_mp3(file_path, target_dir)