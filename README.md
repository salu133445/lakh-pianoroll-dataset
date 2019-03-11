# Source Code for Deriving Lakh Pianoroll Dataset (LPD)

> The derived dataset using the default settings is available
[here](https://salu133445.github.io/lakh-pianoroll-dataset/dataset).

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
   ./scripts/derive_lpd.sh
   ```

## Derive the labels for the LPD

> The derived labels can be found at `data/labels.tar.gz`.

1. Download the labels with the following script.

   ```sh
   ./scripts/download_labels.sh
   ```

2. Derive the labels with the following script.

   ```sh
   ./scripts/derive_labels.sh
   ```

## Synthesize audio files for the LPD

1. Install [GNU Parallel](https://www.gnu.org/software/parallel/) to run the
   synthesizer in parallel mode.
2. Synthesize audio files from multitrack pianorolls with the following script.

   ```sh
   ./scripts/batch_synthesize.sh ./data/lpd/lpd/lpd_cleansed/ \
     ./data/synthesized/lpd_cleansed 20
   ```

   (The above command will synthesize all the multitrack pianorolls in
   the _LPD-cleansed_ subset with 20 parallel jobs.)
