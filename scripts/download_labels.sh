#!/bin/bash
# This script downloads the labels for Million Song Dataset (MSD) from Last.fm
# Dataset, Million Song Dataset Benchmarks and Tagtraum genre annotations.
# Usage: download_all.sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
"${DIR}/download_lastfm.sh"
"${DIR}/download_amg.sh"
"${DIR}/download_tagtraum.sh"
