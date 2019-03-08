"""This script converts a collection of MIDI files to multitrack pianorolls.
"""
import os
import json
import argparse
import warnings
import pretty_midi
from pypianoroll import Multitrack
from utils import make_sure_path_exists, change_prefix, findall_endswith
from config import CONFIG
if CONFIG['multicore'] > 1:
    import joblib

warnings.filterwarnings('ignore')

def parse_args():
    """Return the parsed command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('src', help="root path to the source dataset")
    parser.add_argument('dst', help="root path to the destination dataset")
    parser.add_argument('--midi-info-path', dest='midi_info_path',
                        help="path to save the MIDI info dictionary")
    args = parser.parse_args()
    return args.src, args.dst, args.midi_info_path

def get_midi_info(pm):
    """Return useful information from a MIDI object."""
    if pm.time_signature_changes:
        pm.time_signature_changes.sort(key=lambda x: x.time)
        first_beat_time = pm.time_signature_changes[0].time
    else:
        first_beat_time = pm.estimate_beat_start()

    tc_times, tempi = pm.get_tempo_changes()

    if len(pm.time_signature_changes) == 1:
        time_sign = '{}/{}'.format(pm.time_signature_changes[0].numerator,
                                   pm.time_signature_changes[0].denominator)
    else:
        time_sign = None

    midi_info = {
        'first_beat_time': first_beat_time,
        'num_time_signature_change': len(pm.time_signature_changes),
        'constant_time_signature': time_sign,
        'constant_tempo': tempi[0] if len(tc_times) == 1 else None
    }

    return midi_info

def converter(filepath, src, dst):
    """Convert a MIDI file to a multi-track piano-roll and save the
    resulting multi-track piano-roll to the destination directory. Return a
    tuple of `midi_md5` and useful information extracted from the MIDI file.
    """
    try:
        midi_md5 = os.path.splitext(os.path.basename(filepath))[0]
        multitrack = Multitrack(beat_resolution=CONFIG['beat_resolution'],
                                name=midi_md5)

        pm = pretty_midi.PrettyMIDI(filepath)
        multitrack.parse_pretty_midi(pm)
        midi_info = get_midi_info(pm)

        result_dir = change_prefix(os.path.dirname(filepath), src, dst)
        make_sure_path_exists(result_dir)
        multitrack.save(os.path.join(result_dir, midi_md5 + '.npz'))

        return (midi_md5, midi_info)

    except:
        return None

def main():
    """Main function."""
    src, dst, midi_info_path = parse_args()
    make_sure_path_exists(dst)
    midi_info = {}

    if CONFIG['multicore'] > 1:
        kv_pairs = joblib.Parallel(n_jobs=CONFIG['multicore'], verbose=5)(
            joblib.delayed(converter)(midi_path, src, dst)
            for midi_path in findall_endswith('.mid', src))
        for kv_pair in kv_pairs:
            if kv_pair is not None:
                midi_info[kv_pair[0]] = kv_pair[1]
    else:
        for midi_path in findall_endswith('.mid', src):
            kv_pair = converter(midi_path, src, dst)
            if kv_pair is not None:
                midi_info[kv_pair[0]] = kv_pair[1]

    if midi_info_path is not None:
        with open(midi_info_path, 'w') as f:
            json.dump(midi_info, f)

    print("{} files have been successfully converted".format(len(midi_info)))

if __name__ == "__main__":
    main()
