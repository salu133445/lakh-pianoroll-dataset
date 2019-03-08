"""This script creates a subset of a dataset according to an ID list.
"""
import argparse
import os.path
import shutil
from utils import make_sure_path_exists, msd_id_to_dirs
from config import CONFIG
if CONFIG['multicore'] > 1:
    import joblib

def parse_args():
    """Return the parsed command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('src', help="root path to the source dataset")
    parser.add_argument('dst', help="root path to the destination dataset")
    parser.add_argument('id_list_path', help="path to the ID list file")
    args = parser.parse_args()
    return args.src, args.dst, args.id_list_path

def collector(midi_md5, msd_id, src, dst):
    """Copy a multitrack pianoroll to the destination directory."""
    npz_path = os.path.join(src, midi_md5[0], midi_md5 + '.npz')
    result_path = os.path.join(dst, msd_id_to_dirs(msd_id), midi_md5 + '.npz')
    make_sure_path_exists(os.path.dirname(result_path))
    shutil.copyfile(npz_path, result_path)

def main():
    """Main function."""
    src, dst, id_list_path = parse_args()
    make_sure_path_exists(dst)

    with open(id_list_path) as f:
        id_list = [line.split() for line in f]

    if CONFIG['multicore'] > 1:
        joblib.Parallel(n_jobs=CONFIG['multicore'], verbose=5)(
            joblib.delayed(collector)(midi_md5, msd_id, src, dst)
            for midi_md5, msd_id in id_list)
    else:
        for midi_md5, msd_id in id_list:
            collector(midi_md5, msd_id, src, dst)

    print("Subset successfully collected for: {}".format(id_list_path))

if __name__ == "__main__":
    main()
