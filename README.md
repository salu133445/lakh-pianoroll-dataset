# Source Code for Deriving Lakh Pianoroll Dataset (LPD)

> *If you want to use LPD directly, the one derived with the default settings is
available [here](https://salu133445.github.io/lakh-pianoroll-dataset/dataset).*

## Prerequisites

- Download [Lakh MIDI Dataset](http://colinraffel.com/projects/lmd/) (LMD)

## Shell script

- `run.sh`: derive all datasets and id lists

*Please set the variables `LMD_ROOT` and `LPD_ROOT` and variables in
`config.py` to proper values before running the script.*

## Python code

- `config.py`: define configuration variables
- `converter.py`: used to derive *LPD-full*
- `merger_5.py`: used to derive *LPD-5-full*
- `merger_17.py`: used to derive *LPD-17-full*
- `matcher.py`: used to derive `matched_ids.txt`
- `cleanser.py`: used to derive `cleansed_ids.txt`
- `collector.py`: used to derive the matched and cleansed versions
