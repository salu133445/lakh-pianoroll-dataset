# Source Code for Deriving Lakh Pianoroll Dataset (LPD)

> *If you want to use LPD directly, the one derived with the default settings is
available [here](https://salu133445.github.io/lakh-pianoroll-dataset/dataset).*

1. Download Lakh MIDI Dataset (LMD) from its
   [demo page](http://colinraffel.com/projects/lmd/).

2. Set the variables `LMD_ROOT` and `LPD_ROOT` in `run.sh` and variables in
   `config.py` to proper values.
3. Derive all subsets and versions of LPD, `matched_ids.txt` and
   `cleansed_ids.txt`:

    sh run.sh
