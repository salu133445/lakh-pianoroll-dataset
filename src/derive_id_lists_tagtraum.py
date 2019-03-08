"""This file derives the ID lists for different labels in the Tagtraum genre
annotations (see http://www.tagtraum.com/msd_genre_datasets.html)."""
import os.path
import argparse
from utils import make_sure_path_exists

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
    tag_dict = {}
    with open(src) as f:
        for line in f:
            if line.startswith('#'):
                continue
            elif len(line.split()) == 2:
                tag_dict[line.split()[0]] = line.split()[1]
            elif len(line.split()) > 2:
                tag_dict[line.split()[0]] = '-'.join(line.split()[1:])

    tags = set(tag_dict.values())
    id_lists = {tag: [] for tag in tags}

    # Load the IDs of the songs in the subset
    with open(subset_ids_path) as f:
        subset_ids = [line.rstrip('\n').split()[1] for line in f]

    # Loop over all the songs in the subsets
    for msd_id in subset_ids:
        tag = tag_dict.get(msd_id)
        if tag is None:
            continue
        # Add the ID to the corresponding tag
        id_lists[tag].append(msd_id)

    # Save the ID lists to files
    make_sure_path_exists(result_dir)
    for tag in tags:
        filename = 'id_list_{}.txt'.format(tag)
        with open(os.path.join(result_dir, filename), 'w') as f:
            for msd_id in id_lists[tag]:
                f.write(msd_id + '\n')

    print("ID lists for Tagtraum genre annotations successfully saved.")

if __name__ == "__main__":
    main()
