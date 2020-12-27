The Lakh Pianoroll Dataset (LPD) is a collection of 174,154
[multitrack pianorolls](representation) derived from the
[Lakh MIDI Dataset](http://colinraffel.com/projects/lmd/) (LMD).

## Getting the dataset

We provide multiple subsets and versions of the dataset (see
[here](comparisons)). The dataset is available [here](dataset).

## Using LPD

The multitrack pianorolls in LPD are stored in a special format for efficient
I/O and to save space. We recommend to load the data with
[Pypianoroll](https://salu133445.github.io/pypianoroll/) (The dataset is created
using Pypianoroll v0.3.0.). See [here](https://salu133445.github.io/pypianoroll/save_load.html)
to learn how the data is stored and how to load the data properly.

## License

Lakh Pianoroll Dataset is a derivative of
[Lakh MIDI Dataset](http://colinraffel.com/projects/lmd/) by
[Colin Raffel](http://colinraffel.com), used under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Lakh Pianoroll Dataset is licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) by
[Hao-Wen Dong](https://salu133445.github.io) and
[Wen-Yi Hsiao](https://github.com/wayne391).

Please cite the following papers if you use Lakh Pianoroll Dataset in a
published work.

- Hao-Wen Dong, Wen-Yi Hsiao, Li-Chia Yang, and Yi-Hsuan Yang,
  "__MuseGAN: Multi-track Sequential Generative Adversarial Networks for
  Symbolic Music Generation and Accompaniment__,"
  in _Proceedings of the 32nd AAAI Conference on Artificial Intelligence_
  (AAAI), 2018.

- Colin Raffel,
  "__Learning-Based Methods for Comparing Sequences, with Applications to
  Audio-to-MIDI Alignment and Matching__,"
  _PhD Thesis_, 2016.

## Related projects

- [MuseGAN](https://salu133445.github.io/musegan/)
- [LeadSheetGAN](https://liuhaumin.github.io/LeadsheetArrangement/)
