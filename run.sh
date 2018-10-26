#!/bin/bash
# Derive Lakh Pianoroll Dataset (LPD) from Lakh MIDI Dataset (LMD)
# Usage: ./run.sh

LMD_ROOT=/home/salu133445/NAS/salu133445/lmd/
LPD_ROOT=/home/salu133445/NAS/salu133445/lpd/

python src/converter.py ${LMD_ROOT}lmd_full/ ${LPD_ROOT}lpd/lpd_full/ \
  --midi-info-path ${LPD_ROOT}midi_info.json

python src/merger_5.py ${LPD_ROOT}lpd/lpd_full/ ${LPD_ROOT}lpd_5/lpd_5_full/
python src/merger_17.py ${LPD_ROOT}lpd/lpd_full/ ${LPD_ROOT}lpd_17/lpd_17_full/

python src/matcher.py ${LPD_ROOT}matched_ids.txt ${LPD_ROOT}lpd/lpd_full/ \
  ${LMD_ROOT}match_scores.json
python src/cleanser.py ${LPD_ROOT}cleansed_ids.txt ${LPD_ROOT}lpd/lpd_full/ \
  ${LMD_ROOT}match_scores.json ${LPD_ROOT}midi_info.json

for version in lpd lpd_5 lpd_17; do
  for subset in matched cleansed; do
    python src/collector.py ${LPD_ROOT}${version}/${version}_full/ \
      ${LPD_ROOT}${version}/${version}_${subset}/ ${LPD_ROOT}${subset}_ids.txt
  done
done
