# Python code

- `config.py`: define configuration variables
- `utils.py`: define some handy utility functions

## Derive Lakh Pianoroll Dataset (LPD) from Lakh MIDI Dataset (LMD)

- `converter.py`: derive _LPD-full_ from _LMD-full_
- `merger_5.py`: derive _LPD-5-full_ from _LPD-full_
- `merger_17.py`: derive _LPD-17-full_ from _LPD-full_
- `matcher.py`: derive `matched_ids.txt`
- `cleanser.py`: derive `cleansed_ids.txt`
- `collector.py`: create different subsets of _LPD-full_ with the matched and
  the cleansed ID lists

## Derive the labels for the LPD

- `derive_id_lists_lastfm.py`: derive the ID lists for different labels in the
  Last.fm Dataset
- `derive_id_lists_amg.py`: derive the ID lists for different labels in the MSD
  AllMusic Top Genre Dataset (TopMAGD) provided in the Million Song Dataset
  Benchmarks
- `derive_labels_amg.py`: derive the labels in the MSD AllMusic Style Dataset
  (MASD) provided in the Million Song Dataset Benchmarks
- `derive_id_lists_tagtraum.py`: derive the ID lists for different labels in
  the Tagtraum genre annotations

## Synthesize audio files for the LPD

- `npz_to_audio.py`: synthesize a multitrack pianoroll (.npz) to a .wav file
