"""This file synthesizes a multitrack pianoroll (.npz) to a .wav file."""
import os.path
import argparse
import scipy.io.wavfile
import pypianoroll
from utils import make_sure_path_exists

def parse_args():
    """Parse and return the command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('dst', help="path to save the synthesized audio")
    parser.add_argument('src',
                        help="path to the source pianoroll file (in .npz)")
    parser.add_argument('--fs', type=int, default=44100,
                        help="sampling rate in Hz (default to 44100)")
    parser.add_argument('--tempo', type=float,
                        help="tempo in bpm (default to follow the MIDI file)")
    args = parser.parse_args()
    return args.dst, args.src, args.fs, args.tempo

def main():
    """Main function."""
    dst, src, fs, tempo = parse_args()
    make_sure_path_exists(os.path.dirname(dst))
    multitrack = pypianoroll.Multitrack(src)
    pm = multitrack.to_pretty_midi(tempo)
    waveform = pm.fluidsynth()
    scipy.io.wavfile.write(dst, fs, waveform)

if __name__ == "__main__":
    main()
