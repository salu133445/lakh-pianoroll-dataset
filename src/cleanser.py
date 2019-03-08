"""This script cleanses a dataset and write the qualified IDs to a file.

Cleansing Rules
---------------

- Remove those having more than one time signature change events
- Remove those having a time signature other than 4/4
- Remove those whose first beat not starting from time zero
- Keep only one file that has the highest confidence score in matching for
  each song

"""
import argparse
import os.path
import json
from config import CONFIG

def parse_args():
    """Return the parsed command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help="path to save the resulting list")
    parser.add_argument('src', help="root path to the source dataset")
    parser.add_argument('match_scores_path',
                        help="path to the match scores file")
    parser.add_argument('midi_info_path', help="path to the MIDI info file")

    args = parser.parse_args()
    return args.filepath, args.src, args.match_scores_path, args.midi_info_path

def midi_filter(midi_info):
    """Return True for qualified MIDI files and False for unwanted ones."""
    if midi_info['first_beat_time'] > 0.0:
        return False
    if midi_info['constant_time_signature'] not in CONFIG['time_signatures']:
        return False
    return True

def main():
    """Main function."""
    filepath, src, match_scores_path, midi_info_path = parse_args()
    with open(match_scores_path) as f:
        match_score_dict = json.load(f)
    with open(midi_info_path) as f:
        midi_info = json.load(f)

    with open(filepath, 'w') as f:
        for msd_id in match_score_dict:
            midi_md5s = sorted(match_score_dict[msd_id],
                               key=match_score_dict[msd_id].get, reverse=True)
            for midi_md5 in midi_md5s:
                npz_path = os.path.join(src, midi_md5[0], midi_md5 + '.npz')
                if os.path.isfile(npz_path):
                    if midi_filter(midi_info[midi_md5]):
                        f.write("{}    {}\n".format(midi_md5, msd_id))
                    break

    print("Cleansed ID list successfully saved.")

if __name__ == "__main__":
    main()
