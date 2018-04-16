# Dataset

## LPD

[lpd-full](https://drive.google.com/uc?id=1md7aRHa7KZQhmzNBaFm0zp_SP-cHJZpP&export=download)
contains 174,154 multi-track piano-rolls derived from MIDI files in the
[Lakh MIDI Dataset](http://colinraffel.com/projects/lmd/) (LMD).

## LPD-matched

[lpd-matched](https://drive.google.com/uc?id=1UjOCRr5VOr8AbcbsOxmUBX1ExKvLvVlu&export=download)
contains 115,160 multi-track piano-rolls derived from MIDI files of 30,886 songs
in *lmd-matched*. These files are matched to entries in the Million Song Dataset
(MSD). To make use of the metadata provided by MSD, we refer users to the
[demo page](http://colinraffel.com/projects/lmd/) of LMD.

A list of all file ids (and the matched MSD ids) in the matched subset is
also available ([matched_ids.txt](https://drive.google.com/uc?id=1UjOCRr5VOr8AbcbsOxmUBX1ExKvLvVlu&export=download)).

## LPD-cleansed

[lpd-cleansed](https://drive.google.com/uc?id=1akX1l_pHq83IWBWjbSAdrnykyov30ZRb&export=download)
contains 21,425 multi-track piano-rolls collected from *lpd-matched* with the
following rules.

- Remove those having more than one time signature change events
- Remove those having a time signature other than 4/4
- Remove those whose first beat not starting from time zero
- Keep only one file that has the highest confidence score in matching for each
  song\*

A list of all file ids (and the matched MSD ids) in the cleansed subset is
also available ([cleansed_ids.txt](https://drive.google.com/uc?id=1k_BHTAToq0KcUSHN6icb1JJv7gKgHnq7&export=download)).

\* *The matching confidence scores come with the LMD, which is the confidence of
whether the MIDI file match any entry in the MSD.*

## MIDI Info Dictionary

[midis.json](https://drive.google.com/uc?id=18kAwcriMi46s4TG0SQudkL-iBW6EGlKi&export=download)
contains useful information lost during the conversion from LMD to LPD. It was
used to create *lpd-cleansed*.

- `first_beat_time`: the actual timing of the first beat
- `num_time_signature_change`: the number of time signature change events
- `constant_time_signature`: the *only* time signature used (`None` if it
  changes within a song)
- `constant_tempo`: the *only* tempo (in bpm) used (`None` if it changes within
  a song)

---

## LPD-5

In LPD-5, the tracks are merged into five common categories: **Bass**,
**Drums**, **Piano**, **Guitar** and **Strings** according to the program
numbers provided in the MIDI files.

> *Note that instruments out of the five categories are considered as part of
the strings.*

- [lpd-5-full](https://drive.google.com/uc?id=1RGrbulxEoYvN7sKngo7CFku6f3l8RsDD&export=download)
  contains 174,154 five-track piano-rolls derived from *lpd-full*.

- [lpd-5-matched](https://drive.google.com/uc?id=1ms5C_3mWN4BHoE8ulQAaelyR-krFneAq&export=download)
  contains 115,160 five-track piano-rolls derived from *lpd-matched*.

- [lpd-5-cleansed](https://drive.google.com/uc?id=1XJ648WDMjRilbhs4hE3m099ZQIrJLvUB&export=download)
  contains 21,425 five-track piano-rolls derived from *lpd-cleansed*.

---

## LPD-17

In LPD-17, the tracks are merged into drums and sixteen instrument families
according to the program numbers provided in the MIDI files and the
specification of
[General MIDI Level 1](https://www.midi.org/specifications/item/gm-level-1-sound-set).
The seventeen tracks are **Drums**, **Piano**, **Chromatic Percussion**,
**Organ**, **Guitar**, **Bass**, **Strings**, **Ensemble**, **Brass**, **Reed**,
**Pipe**, **Synth Lead**, **Synth Pad**, **Synth Effects**, **Ethnic**,
**Percussive** and **Sound Effects**.

- [lpd-17-full](https://drive.google.com/uc?id=1Os88DJb28_z-z8c6-AJXu6FS6XSSjXR-&export=download)
  contains 174,154 seventeen-track piano-rolls derived from *lpd-full*.

- [lpd-17-matched](https://drive.google.com/uc?id=1vRaZLdyZ92pdrM-bvcNMV-fzwQZlMQn7&export=download)
  contains 115,160 seventeen-track piano-rolls derived from *lpd-matched*.

- [lpd-17-cleansed](https://drive.google.com/uc?id=1bveCxJmTfPvkKXmRlffron_fBdKsfQxW&export=download)
  contains 21,425 seventeen-track piano-rolls derived from *lpd-cleansed*.
