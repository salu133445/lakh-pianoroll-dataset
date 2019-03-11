#!/bin/bash
# This script synthesizes a multitrack pianoroll (in .npz) to an mp3 file.
# Usage:
#   synthesize.sh [-b bit_rate] [-f sampling_rate] [-k] [-t tempo] [-y] [dst] \
#     [src]
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
SRC_DIR="$DIR/../src/"

function usage {
  echo "Usage:"
  echo "  synthesize.sh [-b bit_rate] [-f sampling_rate] [-k] [-t tempo] \\"
  echo "    [dst] [src]"
  echo "Options:"
  echo "  -b bit_rate         bit rate in bit/sec (default to 192k)"
  echo "  -f sampling_rate    sampling rate in Hz (default to 44100)"
  echo "  -h                  display help"
  echo "  -k                  keep the intermediately-created .wav file"
  echo "  -t tempo            tempo in bpm (default to follow the MIDI file)"
  echo "  -y                  overwrite output file if it exists"
  exit 1
}

if [[ $# -eq 0 ]]
then
  usage
fi

SRC="${@: -1}"
DST="${@:(-2):1}"
BR="192k"
FS=44100
KEEP=false
TEMPO=0
YES=false
while [[ $# -gt 0 ]]
do
  key="$1"
  case $key in
    -b|--br|--bit_rate)
      BR="$2"
      shift 2
      ;;
    -f|--fs|--sampling_rate)
      FS="$2"
      shift 2
      ;;
    -k|--keep|--keep_wav)
      KEEP=true
      shift
      ;;
    -t|--tempo)
      TEMPO="$2"
      shift 2
      ;;
    -h|--help)
      usage
      ;;
    -y)
      YES=true
      shift
      ;;
    *)
      shift
      ;;
  esac
done

if [ "$TEMPO" -gt 0 ]; then
  python2 "$SRC_DIR/npz_to_audio.py" "${DST%.mp3}.wav" "$SRC" --fs "$FS" \
    --tempo "$TEMPO"
else
  python2 "$SRC_DIR/npz_to_audio.py" "${DST%.mp3}.wav" "$SRC" --fs "$FS"
fi

if $YES; then
  ffmpeg -y -i "${DST%.mp3}.wav" -vn -ar "$FS" -ab "$BR" -f mp3 "$DST"
else
  ffmpeg -i "${DST%.mp3}.wav" -vn -ar "$FS" -ab "$BR" -f mp3 "$DST"
fi

if ! $KEEP; then
  rm -rf "${DST%.mp3}.wav"
fi
