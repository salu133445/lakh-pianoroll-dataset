# Lakh Pianoroll Dataset

The Lakh Pianoroll Dataset (LPD) is a collection of 174,154
[multi-track piano-rolls](data) derived from the MIDI files in
[Lakh MIDI Dataset](http://colinraffel.com/projects/lmd/) (LMD).

## Getting the dataset

We provide multiple subsets and versions of the dataset, where the differences
are summarized as follows.

### Comparison of different subsets

| subset   | size    | matched to MSD | one entry per song |
|:--------:|:-------:|:--------------:|:------------------:|
| full     | 174,154 |       X        |         X          |
| matched  | 115,160 |       O        |         X          |
| cleansed | 24,474  |       O        |         O          |

### Comparison of different versions

| version | number of tracks | tracks                              |
|:-------:|:----------------:|:-----------------------------------:|
| LPD     |        -         | -                                   |
| LPD-5   |        5         | Bass, Drums, Piano, Guitar, Strings |
| LPD-17  |        17        | Drums, Piano, Chromatic Percussion, Organ, Guitar,<br> Bass, Strings, Ensemble, Brass, Reed, Pipe, Synth Lead,<br> Synth Pad, Synth Effects, Ethnic, Percussive, Sound Effects |

## Using LPD

The multi-track piano-rolls in LPD are stored in a special format for
efficient I/O and to save space. We recommend to load the data with
[Pypianoroll](https://salu133445.github.io/pypianoroll/)\*. See
[here](https://salu133445.github.io/pypianoroll/save_load.html) to learn how
the data is stored and how to load the data properly.

\* *The dataset is created using Pypianoroll (v0.3.0).*

## License

Lakh Pianoroll Dataset is a derivative of
[Lakh MIDI Dataset](http://colinraffel.com/projects/lmd/) by
[Colin Raffel](http://colinraffel.com), used under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Lakh Pianoroll Dataset is licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) by
[Hao-Wen Dong](https://salu133445.github.io/) and
[Wen-Yi Hsiao](https://github.com/wayne391).

Please cite the following papers if you use Lakh Pianoroll Dataset in a
published work.

- Hao-Wen Dong, Wen-Yi Hsiao, Li-Chia Yang and Yi-Hsuan Yang, "MuseGAN:
  Multi-track Sequential Generative Adversarial Networks for Symbolic Music
  Generation and Accompaniment," in *AAAI Conference on Artificial Intelligence*
  (AAAI), 2018.

- Colin Raffel, "Learning-Based Methods for Comparing Sequences, with
  Applications to Audio-to-MIDI Alignment and Matching," *PhD Thesis*, 2016.
