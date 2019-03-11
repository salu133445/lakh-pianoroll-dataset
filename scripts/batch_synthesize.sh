#!/bin/bash
# This script synthesizes in parallel a batch of multitrack pianorolls (.npz) in
# a directory to mp3 files.
# Usage:
#   batch_synthesize.sh [-b bit_rate] [-f sampling_rate] [-k] [-t tempo] [-y] \
#     [dst] [src] [n_jobs]
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"

task(){
  relpath="${1#$3}"
  "$4/synthesize.sh" "${@:4}" "$2/${relpath%.npz}.mp3" "$1"
}

N_JOBS="${@: -1}"
SRC="${@: -2:1}"
DST="${@: -3:1}"

export -f task
find "$SRC" -maxdepth 99 -type f -name *.npz | parallel -j "$N_JOBS" task {} \
  "$DST" "$SRC" "$DIR" "${@:1:$#-3}"
