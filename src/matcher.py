"""This script writes the IDs of songs that have been matched to Million Song
Dataset (MSD) to a file.
"""
import argparse
import os.path
import json

def parse_args():
    """Return the parsed command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help="path to save the resulting list")
    parser.add_argument('src', help="root path to the source dataset")
    parser.add_argument('match_scores_path',
                        help="path to the match scores file")
    args = parser.parse_args()
    return args.filepath, args.src, args.match_scores_path

def main():
    """Main function."""
    filepath, src, match_scores_path = parse_args()

    with open(match_scores_path) as f:
        match_score_dict = json.load(f)

    with open(filepath, 'w') as f:
        for msd_id in match_score_dict:
            for midi_md5 in match_score_dict[msd_id]:
                npz_path = os.path.join(src, midi_md5[0], midi_md5 + '.npz')
                if os.path.isfile(npz_path):
                    f.write("{}    {}\n".format(midi_md5, msd_id))

    print("Matched ID list successfully saved.")

if __name__ == "__main__":
    main()
