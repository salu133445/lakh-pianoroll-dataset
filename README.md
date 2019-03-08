# Source Code for Deriving Lakh Pianoroll Dataset (LPD)

> If you want to use LPD directly, the one derived with the default settings is
available [here](https://salu133445.github.io/lakh-pianoroll-dataset/dataset).

1. Download Lakh MIDI Dataset (LMD) with the following script.

   ```sh
   ./scripts/download_lmd.sh
   ```

   (Or, download it manually [here](http://colinraffel.com/projects/lmd/).)
2. Set the variables `LMD_ROOT` and `LPD_ROOT` in `run.sh` and variables in
   `config.py` to proper values.
3. Derive all subsets and versions of LPD, `matched_ids.txt` and
   `cleansed_ids.txt` with the following script.

   ```sh
   ./scripts/run.sh
   ```

## Derive the ID lists for different labels

1. Download the labels with the following script.

   ```sh
   ./scripts/download_labels.sh
   ```

2. Derive the ID lists with the following script.

   ```sh
   ./scripts/derive_id_lists.sh
   ```
