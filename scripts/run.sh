#!/bin/bash
# This script derives the Lakh Pianoroll Dataset (LPD) from the Lakh MIDI
# Dataset (LMD).
# Usage: run.sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
SRC_DIR="$DIR/../src/"

# Define the root directories of the LMD dataset and the resulting LPD dataset
LMD_ROOT="$DIR/../data/lmd/"
LPD_ROOT="$DIR/../data/lpd/"

# Convert MIDI files to multitrack pianorolls
python "$SRC_DIR/converter.py" "$LMD_ROOT/lmd_full/" "$LPD_ROOT/lpd/lpd_full/" \
  --midi-info-path "$LPD_ROOT/midi_info.json"

# Merge multitrack pianorolls to 5-track or 17-track pianorolls
python "$SRC_DIR/merger_5.py" "$LPD_ROOT/lpd/lpd_full/" \
  "$LPD_ROOT/lpd_5/lpd_5_full/"
python "$SRC_DIR/merger_17.py" "$LPD_ROOT/lpd/lpd_full/" \
  "$LPD_ROOT/lpd_17/lpd_17_full/"

# Find out the ids of songs matched to MSD (according to LMD-matched)
python "$SRC_DIR/matcher.py" "$LPD_ROOT/matched_ids.txt" \
  "$LPD_ROOT/lpd/lpd_full/" "$LMD_ROOT/match_scores.json"

# Find out the ids of songs to be collected into the cleansed dataset
python "$SRC_DIR/cleanser.py" "$LPD_ROOT/cleansed_ids.txt" \
  "$LPD_ROOT/lpd/lpd_full/" "$LMD_ROOT/match_scores.json" \
  "$LPD_ROOT/midi_info.json"

# Collect corresponding songs to different collecteions
for version in "lpd" "lpd_5" "lpd_17"; do
  for subset in "matched" "cleansed"; do
    python "$SRC_DIR/collector.py" "$LPD_ROOT/$version/${version}_full/" \
      "$LPD_ROOT/$version/${version}_$subset/" "$LPD_ROOT/${subset}_ids.txt"
  done
done
