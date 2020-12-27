# Dataset

## LPD

[lpd-full](https://drive.google.com/uc?id=19FJwmNxWUmR3UutCDhZtbKVnEBVHU-2q)
contains 174,154 multitrack pianorolls derived from the
[Lakh MIDI Dataset](http://colinraffel.com/projects/lmd/) (LMD).

## LPD-matched

[lpd-matched](https://drive.google.com/uc?id=1ULUOJKcrgbTXc0QOyPQkjVqVx4nQilTK)
contains 115,160 multitrack pianorolls derived from the matched version of LMD.
These files are matched to entries in the Million Song Dataset (MSD). To make
use of the metadata provided by MSD, we refer users to the
[demo page](http://colinraffel.com/projects/lmd/) of LMD.

[matched_ids.txt](https://drive.google.com/uc?id=1yTeqvZ1HM1PGVm_jHPU3Rxb8lh3ctzn8)
provides a list of all file IDs and the matched MSD IDs in the matched subset.

## LPD-cleansed

[lpd-cleansed](https://drive.google.com/uc?id=11rxrGaQbfTW-WC0k2GlR9YDAT-UxIb4O)
contains 21,425 multitrack pianorolls collected from _lpd-matched_ with the
following rules. Note that _lpd-cleansed_ contains songs from ALL genres, which
is different from the description on the paper.

- Remove those having more than one time signature change events
- Remove those having a time signature other than 4/4
- Remove those whose first beat not starting from time zero
- Keep only one file that has the highest confidence score in matching for each
  song\*

[cleansed_ids.txt](https://drive.google.com/uc?id=1EmCZQvc5Yqtz4y8TO5Ms_JpzDT6WRPEO)
provides a list of all file IDs and the matched MSD IDs in the cleansed subset.

\* _The matching confidence scores come with the LMD, which is the confidence of
whether the MIDI file match any entry in the MSD._

## MIDI Info Dictionary

[midi_info.json](https://drive.google.com/uc?id=1TxyTCN-yTZ_AlJUHchGIHdAM-XkbJBwf)
contains useful information lost during the conversion from LMD to LPD. It was
used to create _lpd-cleansed_.

- `first_beat_time`: the actual timing of the first beat
- `num_time_signature_change`: the number of time signature change events
- `constant_time_signature`: the _only_ time signature used (`None` if it
  changes within a song)
- `constant_tempo`: the _only_ tempo (in bpm) used (`None` if it changes within
  a song)

[midi_info_v2.json](https://drive.google.com/uc?id=1Ly5g6uis55_y-s017OPHLDsLdp4H4mU_)
has the same values for `first_beat_time`, `num_time_signature_change` and
`constant_time_signature`. However, `constant_tempo` is now a boolean value that
indicates whether the tempo is constant throughout the song. There is an
additional key `tempo` that stores the initial tempo value (in bpm).

---

## LPD-5

In LPD-5, the tracks are merged into five common categories: _Drums_, _Piano_,
_Guitar_, _Bass_ and _Strings_ according to the program numbers provided in the
MIDI files.

> Note that instruments out of the five categories are considered as part of the
strings except those in the _Percussive_, _Sound effects_ and _Synth Effects_
families (see [here](https://www.midi.org/specifications/item/gm-level-1-sound-set)).

- [lpd-5-full](https://drive.google.com/uc?id=1tZKMhYazSWapFTUt7H6abHSo-QKH9ATC)
  contains 174,154 five-track pianorolls derived from _lpd-full_.
- [lpd-5-matched](https://drive.google.com/uc?id=1EGSHxDr8qYLNVrv3Xn7SB1tqEdm16gBi)
  contains 115,160 five-track pianorolls derived from _lpd-matched_.
- [lpd-5-cleansed](https://drive.google.com/uc?id=1yz0Ma-6cWTl6mhkrLnAVJ7RNzlQRypQ5)
  contains 21,425 five-track pianorolls derived from _lpd-cleansed_.

---

## LPD-17

In LPD-17, the tracks are merged into drums and sixteen instrument families
according to the program numbers provided in the MIDI files and the
specification of
[General MIDI Level 1](https://www.midi.org/specifications/item/gm-level-1-sound-set).
The seventeen tracks are _Drums_, _Piano_, _Chromatic Percussion_, _Organ_,
_Guitar_, _Bass_, _Strings_, _Ensemble_, _Brass_, _Reed_, _Pipe_, _Synth Lead_,
_Synth Pad_, _Synth Effects_, _Ethnic_, _Percussive_ and _Sound Effects_.

- [lpd-17-full](https://drive.google.com/uc?id=1bJAC2SKhdKbKvpLL1V1l66cCgWX8eQEm)
  contains 174,154 seventeen-track pianorolls derived from _lpd-full_.
- [lpd-17-matched](https://drive.google.com/uc?id=1jMTzszQGq7fhGOQpfrO7MbPGjVzX-CjB)
  contains 115,160 seventeen-track pianorolls derived from _lpd-matched_.
- [lpd-17-cleansed](https://drive.google.com/uc?id=1ycvALTnMNWnXcwXDjS7YeNC6mQtANvMK)
  contains 21,425 seventeen-track pianorolls derived from _lpd-cleansed_.
