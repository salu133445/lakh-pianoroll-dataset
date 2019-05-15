# Labels

We derived the labels for the Lakh Pianoroll Dataset (LPD) from three different
sources: the Last&#46;fm Dataset, the Million Song Dataset (MSD) Benchmarks and
the Tagtraum genre annotations. Note that these labels are derived based on the
mapping between the Lakh MIDI Dataset (LMD) and the MSD, which may contain
incorrect pairs (see [here](https://colinraffel.com/projects/lmd/)).

> Please refer to the original sources for the license information.

## Last&#46;fm Dataset

- [id_lists_lastfm.tar.gz](https://drive.google.com/uc?id=1mkmQjOifUHISszMsVTDHNuxd7H8Fo5Cs&export=download):
  we derived the ID lists for most common labels in the Last&#46;fm Dataset (see 
  [here](http://millionsongdataset.com/lastfm/)).

## Million Song Dataset Benchmarks

- [id_lists_amg.tar.gz](https://drive.google.com/uc?id=1Rv1uAAkcebzYnmYdZYeaBkdK6Q2YtF7c&export=download):
  we derived the ID lists for all the labels in the MSD AllMusic Top Genre
  Dataset (TopMAGD) provided in the Million Song Dataset Benchmarks (see
  [here](http://www.ifs.tuwien.ac.at/mir/msd/)).
- [masd_labels.txt](https://drive.google.com/uc?id=1OqcBgW_4x6FRF5qjvWXCknBbdhM6Tk1D&export=download):
  we also derived the labels from the MSD AllMusic Style Dataset (MASD) provided
  in the Million Song Dataset Benchmarks. Each entry has at most one label.
- [masd_labels_cleansed.txt](https://drive.google.com/uc?id=1mPcUpfCTjdbZ-m5Va9Z7jaUhXC3wMr3G&export=download):
  this is a cleansed version of _masd_labels.txt_, where less common labels are
  discarded.

## Tagtraum genre annotations

- [id_lists_tagtraum.tar.gz](https://drive.google.com/uc?id=1Gjb4OFnbQ8CFnhrtJvjNneOQqBh9XhAq&export=download):
  we derived the ID lists for all the labels in the Tagtraum genre annotations
  (see [here](http://www.tagtraum.com/msd_genre_datasets.html)).
