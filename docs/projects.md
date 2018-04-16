# Related Projects

## MuseGAN &mdash; An AI for Music Generation

<a href="https://salu133445.github.io/musegan/">
<img src="figs/musegan_logo.png" alt="musegan_logo" width="200" height="200" />
</a>

Collaborators: Wen-Yi Hsiao, Li-Chia Yang<br>
Advisor: Yi-Hsuan Yang

[MuseGAN](https://salu133445.github.io/musegan/) is a project on music
generation. In essence, we aim to generate polyphonic music of multiple tracks
(instruments) with harmonic and rhythmic structure, multi-track interdependency
and temporal structure. To our knowledge, our work represents the first approach
that deal with these issues altogether.

The models are trained with
[Lakh Pianoroll Dataset](https://salu133445.github.io/musegan/dataset) (LPD), a
new [multi-track piano-roll](https://salu133445.github.io/musegan/data) dataset,
in an unsupervised approach. The proposed models are able to generate music
either from scratch, or by accompanying a track given by user. Specifically, we
use the model to generate pop song phrases consisting of bass, drums, guitar,
piano and strings tracks.

Listen to some of the best phrases.
([more results](https://salu133445.github.io/musegan/results))

{% include audio_player.html filename="best_samples.mp3" %}

*To learn more about MuseGAN, please visit our
[demo page](https://salu133445.github.io/musegan/).*

- Hao-Wen Dong\*, Wen-Yi Hsiao\*, Li-Chia Yang and Yi-Hsuan Yang,
  "**MuseGAN: Multi-track Sequential Generative Adversarial Networks for
  Symbolic Music Generation and Accompaniment**,"
  in *AAAI Conference on Artificial Intelligence* (AAAI), 2018.
  [[website](https://salu133445.github.io/musegan/)]
  [[arxiv](http://arxiv.org/abs/1709.06298)]
  [[slides](https://salu133445.github.io/musegan/pdf/musegan-aaai2018-slides.pdf)]

- Hao-Wen Dong\*, Wen-Yi Hsiao\*, Li-Chia Yang and Yi-Hsuan Yang,
  "**MuseGAN: Demonstration of a Convolutional GAN Based Model for Generating
  Multi-track Piano-rolls**,"
  in *ISMIR Late-Breaking and Demo Session*, 2017.
  (non-peer reviewed two-page extended abstract)
  [[paper](https://salu133445.github.io/musegan/pdf/musegan-ismir2017-lbd-paper.pdf)]
  [[poster](https://salu133445.github.io/musegan/pdf/musegan-ismir2017-lbd-poster.pdf)]

\* *These authors contributed equally to this work.*
