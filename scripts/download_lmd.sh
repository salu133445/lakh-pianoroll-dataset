#!/bin/bash
# This script downloads the Lakh MIDI Dataset (LMD;
# see https://colinraffel.com/projects/lmd/).
# Usage: download_lmd.sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
DST="${DIR}/../data/lmd/"
mkdir -p "$DST"
wget -P "$DST" "http://hog.ee.columbia.edu/craffel/lmd/lmd_full.tar.gz"
wget -P "$DST" "http://hog.ee.columbia.edu/craffel/lmd/match_scores.json"
tar zxf "$DST/lmd_full.tar.gz" -C "$DST"
