from midi2audio import FluidSynth

def midi_to_wav(midi_file, wav_file, sound_font=None, sampling_rate=44100):
    # Create FluidSynth object with a specified sample rate and optional sound font
    if sound_font:
        fluidsynth = FluidSynth(sound_font, sample_rate=sampling_rate)
    else:
        fluidsynth = FluidSynth(sample_rate=sampling_rate)
    
    # Generate audio waveform using FluidSynth and save to wav_file
    fluidsynth.midi_to_audio(midi_file, wav_file)
    
    print(f"Saved WAV file to {wav_file}")

# Example usage
midi_file = '/home/aayush/Documents/noise-to-music/data/lofi/4th Rendez Vous.midi'
wav_file = 'output_audio_file.wav'
sound_font = '/home/aayush/Downloads/Touhou.sf2'  # Specify the path to your sound font file, if you have one
midi_to_wav(midi_file, wav_file, sound_font=sound_font, sampling_rate=44100)