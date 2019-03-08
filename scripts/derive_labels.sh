#!/bin/bash
# This script derives the ID lists for different labels in the Last.fm Dataset,
# Million Song Dataset Benchmarks and Tagtraum genre annotations.
# Usage: derive_id_lists.sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
SRC_DIR="$DIR/../src/"
DATA_DIR="$DIR/../data/"
RESULT_DIR="$DATA_DIR/labels/"
LPD_ROOT="$DATA_DIR/lpd/"

python "$SRC_DIR/derive_id_lists_lastfm.py" "$RESULT_DIR/lastfm/" \
  "$DATA_DIR/lastfm/" "$LPD_ROOT/cleansed_ids.txt"
python "$SRC_DIR/derive_id_lists_amg.py" "$RESULT_DIR/amg/" \
  "$DATA_DIR/amg/msd-topMAGD-genreAssignment.cls" "$LPD_ROOT/cleansed_ids.txt"
python "$SRC_DIR/derive_id_lists_tagtraum.py" "$RESULT_DIR/tagtraum/" \
  "$DATA_DIR/tagtraum/msd_tagtraum_cd2c.cls" "$LPD_ROOT/cleansed_ids.txt"
python "$SRC_DIR/derive_labels_amg.py" "$RESULT_DIR/amg/" \
  "$DATA_DIR/amg/msd-MASD-styleAssignment.cls" "$LPD_ROOT/cleansed_ids.txt"
