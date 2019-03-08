"""This file derives the ID lists for different labels in the Last.fm Dataset
(see https://labrosa.ee.columbia.edu/millionsong/lastfm)."""
import json
import os.path
import argparse
from utils import make_sure_path_exists, msd_id_to_dirs

# Define the tags to be considered
TAGS = [
    'sad', 'Love', 'cool', 'electro', 'happy', 'indie', '70s', 'classic-rock',
    'Progressive-rock', 'Mellow', 'oldies', 'british', 'piano', 'electronica',
    'sexy', 'experimental', 'techno', 'funk', 'folk', 'psychedelic', 'hardcore',
    'Favorite', 'pop', '60s', 'downtempo', 'relax', 'amazing', 'blues', 'House',
    'catchy', 'Favourites', '80s', '00s', 'country', 'chillout', 'chill',
    'electronic', 'punk', 'Soundtrack', 'fun', 'favourite', 'lounge', 'reggae',
    'favorites', 'trance', 'american', 'cover', 'alternative', 'party',
    'Awesome', 'melancholy', 'acoustic', 'dance', 'Hip-Hop', 'soul', 'classic',
    'metal', 'guitar', 'rap', 'beautiful', 'loved', 'jazz', 'rock',
    'heard-on-Pandora', '90s', 'female', 'ambient', 'instrumental', 'rnb'
]

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

    id_lists = {tag: [] for tag in TAGS}

    # Load the IDs of the songs in the subset
    with open(subset_ids_path) as f:
        subset_ids = [line.rstrip('\n').split()[1] for line in f]

    # Loop over all the songs in the subsets
    for msd_id in subset_ids:
        for dataset in ('lastfm_train', 'lastfm_test'):
            filepath = os.path.join(
                src, dataset, msd_id_to_dirs(msd_id) + '.json')
            if os.path.exists(filepath):
                with open(filepath) as f:
                    data = json.load(f)
                # Loop over all the tags annotated to the song
                for tag_freq_pair in data['tags']:
                    if tag_freq_pair[0] in TAGS:
                        # Add the ID to the corresponding tag
                        id_lists[tag_freq_pair[0]].append(msd_id)

    # Save the ID lists to files
    make_sure_path_exists(result_dir)
    for tag in TAGS:
        filename = 'id_list_{}.txt'.format(tag.lower())
        with open(os.path.join(result_dir, filename), 'w') as f:
            for msd_id in id_lists[tag]:
                f.write(msd_id + '\n')

    print("ID lists for Last.fm Dataset successfully saved.")

if __name__ == "__main__":
    main()
