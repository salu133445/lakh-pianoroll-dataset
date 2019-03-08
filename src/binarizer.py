"""This script binarizes a collection of multitrack pianorolls.
"""
import os.path
import argparse
from pypianoroll import Multitrack
from utils import make_sure_path_exists, change_prefix, findall_endswith
from config import CONFIG
if CONFIG['multicore'] > 1:
    import joblib

def parse_args():
    """Return the parsed command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('src', help="root path to the source dataset")
    parser.add_argument('dst', help="root path to the destination dataset")
    args = parser.parse_args()
    return args.src, args.dst

def binarizer(filepath, src, dst):
    """Load and binarize a multitrack pianoroll and save the resulting
    multitrack pianoroll to the destination directory."""
    # Load and binarize the multitrack pianoroll
    multitrack = Multitrack(filepath)
    multitrack.binarize()

    # Save the binarized multitrack pianoroll
    result_path = change_prefix(filepath, src, dst)
    make_sure_path_exists(os.path.dirname(result_path))
    multitrack.save(result_path)

def main():
    """Main function."""
    src, dst = parse_args()
    make_sure_path_exists(dst)

    if CONFIG['multicore'] > 1:
        joblib.Parallel(n_jobs=CONFIG['multicore'], verbose=5)(
            joblib.delayed(binarizer)(npz_path, src, dst)
            for npz_path in findall_endswith('.npz', src))
    else:
        for npz_path in findall_endswith('.npz', src):
            binarizer(npz_path, src, dst)

    print("Dataset successfully binarized.")

if __name__ == "__main__":
    main()
