# Labels

We derived the labels for the Lakh Pianoroll Dataset (LPD) from three different
sources: the Last&#46;fm Dataset, the Million Song Dataset (MSD) Benchmarks and
the Tagtraum genre annotations. Note that these labels are derived based on the
mapping between the Lakh MIDI Dataset (LMD) and the MSD, which may contain
incorrect pairs (see [here](https://colinraffel.com/projects/lmd/)).

> All the labels below can be downloaded as a ZIP file [here](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/Ebyo4GUGkIhKop7TAIw98agB1qZ8NVerIvT5W9Nry9Cn5Q?e=xjgOiR). Please refer to the original sources for the license information.

## Last&#46;fm Dataset

- [id_lists_lastfm.tar.gz](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EbVdGIKAuC9Hn5BTkCLhIzMBRaF-X91EvI77ZSTs9aO2lA?e=rgxLjm):
  we derived the ID lists for most common labels in the Last&#46;fm Dataset (see
  [here](http://millionsongdataset.com/lastfm/)).

## Million Song Dataset Benchmarks

- [id_lists_amg.tar.gz](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EbqjoeUiIj9DhODGZOIVBIMBTK1PhDN86rRb29_iTmfhuQ):
  we derived the ID lists for all the labels in the MSD AllMusic Top Genre
  Dataset (TopMAGD) provided in the Million Song Dataset Benchmarks (see
  [here](http://www.ifs.tuwien.ac.at/mir/msd/)).
- [masd_labels.txt](https://ucsdcloud-my.sharepoint.com/:t:/g/personal/h3dong_ucsd_edu/Ec1B0IGvabhJgzvhfskjKlQBcQQuePIGOpmM67O5twpbxg?e=yZpCdz):
  we also derived the labels from the MSD AllMusic Style Dataset (MASD) provided
  in the Million Song Dataset Benchmarks. Each entry has at most one label.
- [masd_labels_cleansed.txt](https://ucsdcloud-my.sharepoint.com/:t:/g/personal/h3dong_ucsd_edu/EWait2PjXF9Pk7T_8D_zu0ABfDi-kWCBOI1M7PqLsMvLIA?e=Mcwz2I):
  this is a cleansed version of *masd_labels.txt*, where less common labels are
  discarded.

## Tagtraum genre annotations

- [id_lists_tagtraum.tar.gz](https://ucsdcloud-my.sharepoint.com/:u:/g/personal/h3dong_ucsd_edu/EaPOfwt7maBHkxAAtKv5U58BdRSJp3c-_5TS18opcskkCA?e=D1Dhts):
  we derived the ID lists for all the labels in the Tagtraum genre annotations
  (see [here](http://www.tagtraum.com/msd_genre_datasets.html)).
