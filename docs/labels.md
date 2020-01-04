# Labels

We derived the labels for the Lakh Pianoroll Dataset (LPD) from three different
sources: the Last&#46;fm Dataset, the Million Song Dataset (MSD) Benchmarks and
the Tagtraum genre annotations. Note that these labels are derived based on the
mapping between the Lakh MIDI Dataset (LMD) and the MSD, which may contain
incorrect pairs (see [here](https://colinraffel.com/projects/lmd/)).

> Please refer to the original sources for the license information.

## Last&#46;fm Dataset

- [id_lists_lastfm.tar.gz](https://drive.google.com/uc?export=download&id=1mpsoxU2fU1AjKopkcQ8Q8V6wYmVPbnPO):
  we derived the ID lists for most common labels in the Last&#46;fm Dataset (see
  [here](http://millionsongdataset.com/lastfm/)).

## Million Song Dataset Benchmarks

- [id_lists_amg.tar.gz](https://drive.google.com/uc?export=download&id=1hp9b_g1hu_dkP4u8h46iqHeWMaUoI07R):
  we derived the ID lists for all the labels in the MSD AllMusic Top Genre
  Dataset (TopMAGD) provided in the Million Song Dataset Benchmarks (see
  [here](http://www.ifs.tuwien.ac.at/mir/msd/)).
- [masd_labels.txt](https://drive.google.com/uc?export=download&id=1CKZ2KUrhHKLZqXl9nLwevVnl9i7VW607):
  we also derived the labels from the MSD AllMusic Style Dataset (MASD) provided
  in the Million Song Dataset Benchmarks. Each entry has at most one label.
- [masd_labels_cleansed.txt](https://drive.google.com/uc?export=download&id=11upPUgx1IVl-N8MaHVJtYiJCSme64Th7):
  this is a cleansed version of *masd_labels.txt*, where less common labels are
  discarded.

## Tagtraum genre annotations

- [id_lists_tagtraum.tar.gz](https://drive.google.com/uc?export=download&id=19RC9YTjJ3hGIH87zDWdNIYIL_trs30Q4):
  we derived the ID lists for all the labels in the Tagtraum genre annotations
  (see [here](http://www.tagtraum.com/msd_genre_datasets.html)).
