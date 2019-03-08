"""This file derives the labels in the MSD AllMusic Style Dataset (MASD)
provided in the Million Song Dataset Benchmarks (see
http://www.ifs.tuwien.ac.at/mir/msd/)."""
import os.path
import argparse
from utils import make_sure_path_exists
from constants import LABEL_NUM_MAP, CLEANSED_LABELS

def parse_args():
    """Return the parsed command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('result_dir', help="path to save the ID lists")
    parser.add_argument('src', help="path to the labels")
    parser.add_argument('subset_ids_path',
                        help="path to the ID list of the target subset")
    args = parser.parse_args()
    return args.result_dir, args.src, args.subset_ids_path

def main():
    """Main function."""
    result_dir, src, subset_ids_path = parse_args()

    # Parse the label of each song
    id_label_masd = {}
    with open(src) as f:
        for line in f:
            if line.startswith('#'):
                continue
            id_label_masd[line.split()[0]] = LABEL_NUM_MAP[line.split()[1]]

    # Load the IDs of the songs in the subset
    with open(subset_ids_path) as f:
        subset_ids = [line.rstrip('\n').split()[1] for line in f]

    # Loop over all the songs in the subset
    collected = {}
    for msd_id in subset_ids:
        label = id_label_masd.get(msd_id)
        if label is None:
            continue
        collected[msd_id] = label

    # Save the ID label pairs to a file
    make_sure_path_exists(result_dir)
    filepath = os.path.join(result_dir, 'masd_labels.txt')
    with open(filepath, 'w') as f:
        f.write("# msd_id, label_num\n")
        for msd_id in collected:
            f.write("{}    {}\n".format(msd_id, collected[msd_id]))
    print("Labels successfully saved.")

    # Save the cleansed ID label pairs to a file
    cleansed = {}
    for msd_id in collected:
        if collected[msd_id] in CLEANSED_LABELS:
            cleansed[msd_id] = CLEANSED_LABELS.index(collected[msd_id])
    filepath = os.path.join(result_dir, 'masd_labels_cleansed.txt')
    with open(filepath, 'w') as f:
        f.write("# msd_id, label_num\n")
        for msd_id in cleansed:
            f.write("{}    {}\n".format(msd_id, cleansed[msd_id]))
    print("Cleansed labels successfully saved.")

if __name__ == "__main__":
    main()
