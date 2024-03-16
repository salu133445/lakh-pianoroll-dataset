# Dataset

## LPD

[lpd-full](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EdbL-YEk6n5PsBsUiy4WNCEBIF7i9ODsH709TI8BgeQc7g?e=jh9WEI)
contains 174,154 multitrack pianorolls derived from the
[Lakh MIDI Dataset](http://colinraffel.com/projects/lmd/) (LMD).

## LPD-matched

[lpd-matched](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/ETLEA8kl0TlBjl6ckYW_tfMB5X09pPLgNJnUgdHqXgjY0A?e=785xwp)
contains 115,160 multitrack pianorolls derived from the matched version of LMD.
These files are matched to entries in the Million Song Dataset (MSD). To make
use of the metadata provided by MSD, we refer users to the
[demo page](http://colinraffel.com/projects/lmd/) of LMD.

[matched_ids.txt](https://ucsdcloud-my.sharepoint.com/:t:/g/personal/h3dong_ucsd_edu/EacvvyoMWYREgAJQ4sZPsCwB31rdpyo-scvts-BWBx4xtg?e=aN0Jqm)
provides a list of all file IDs and the matched MSD IDs in the matched subset.

## LPD-cleansed

[lpd-cleansed](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EejJ_myDTa9Jsiswlk5DqHoByCaZygtKqDL2BYEXT6AD5w?e=JYe0j8)
contains 21,425 multitrack pianorolls collected from _lpd-matched_ with the
following rules. Note that _lpd-cleansed_ contains songs from ALL genres, which
is different from the description on the paper.

- Remove those having more than one time signature change events
- Remove those having a time signature other than 4/4
- Remove those whose first beat not starting from time zero
- Keep only one file that has the highest confidence score in matching for each
  song\*

[cleansed_ids.txt](https://ucsdcloud-my.sharepoint.com/:t:/g/personal/h3dong_ucsd_edu/EfmNwSfQ0yhIobAwvFY7kysBpmgTIuFXqL8klAeS6IN_zQ?e=Nxiy75)
provides a list of all file IDs and the matched MSD IDs in the cleansed subset.

\* _The matching confidence scores come with the LMD, which is the confidence of
whether the MIDI file match any entry in the MSD._

## MIDI Info Dictionary

[midi_info.json](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EVIrPx2DgztEuKCHEgfyoSkBQrIVbbHbShcxZD406_LCTQ?e=IVhn0r)
contains useful information lost during the conversion from LMD to LPD. It was
used to create _lpd-cleansed_.

- `first_beat_time`: the actual timing of the first beat
- `num_time_signature_change`: the number of time signature change events
- `constant_time_signature`: the _only_ time signature used (`None` if it
  changes within a song)
- `constant_tempo`: the _only_ tempo (in bpm) used (`None` if it changes within
  a song)

[midi_info_v2.json](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EeCuOWLxyRlIkRVHFdyURokBASAhkkoh9A82DEgBzc69cQ?e=jMpdcp)
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
families (see [here](https://en.wikipedia.org/wiki/General_MIDI#Program_change_events)).

- [lpd-5-full](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EWaJUNAZJv1Gs9Z_qGaZ23EBt9VEfPB12z2uyq05g75XSA?e=b1QgOP)
  contains 174,154 five-track pianorolls derived from _lpd-full_.
- [lpd-5-matched](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EYUdm4cUfaJHtbON5KSSJAkB96HLGgKC18MbvI1UbU4SMA?e=c0eWRw)
  contains 115,160 five-track pianorolls derived from _lpd-matched_.
- [lpd-5-cleansed](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/Ebu0hMewNeRPs7wIHB0SPyIBoFuC1-rAU5yUK5q2flt1BA?e=uDLp37)
  contains 21,425 five-track pianorolls derived from _lpd-cleansed_.

---

## LPD-17

In LPD-17, the tracks are merged into drums and sixteen instrument families
according to the program numbers provided in the MIDI files and the
specification of General MIDI (see [here](https://en.wikipedia.org/wiki/General_MIDI#Program_change_events)).
The seventeen tracks are _Drums_, _Piano_, _Chromatic Percussion_, _Organ_,
_Guitar_, _Bass_, _Strings_, _Ensemble_, _Brass_, _Reed_, _Pipe_, _Synth Lead_,
_Synth Pad_, _Synth Effects_, _Ethnic_, _Percussive_ and _Sound Effects_.

- [lpd-17-full](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EeGavVQ3QHtFg9PF6Kr-4-0BMzfIl5Tm4XEuhls_bCRHlQ?e=jUPrWH)
  contains 174,154 seventeen-track pianorolls derived from _lpd-full_.
- [lpd-17-matched](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/ESTv8JEAKTFJhQD2oWowlYcB8Kk4iw1rpM6Rn1PIILwMww?e=GjpQnW)
  contains 115,160 seventeen-track pianorolls derived from _lpd-matched_.
- [lpd-17-cleansed](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EdaJWG-GdP1Kng2FRuFAHJkB7RF1koJsm0-g2d5AaUhi-A?e=2Xp9fF)
  contains 21,425 seventeen-track pianorolls derived from _lpd-cleansed_.
