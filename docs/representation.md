# Representation

## Pianoroll

Pianoroll is a music storing format which represents a music piece by a
score-like matrix. The vertical and horizontal axes represent note pitch and
time, respectively. The values represent the velocities of the notes.

The time axis can either be in _absolute timing_ or in _symbolic timing_. For
absolute timing, the actual timing of note occurrence is used. For symbolic
timing, the tempo information is removed and thereby each beat has the same
length.

In LPD, we use symbolic timing and the temporal resolution is set to 24 per beat
in order to cover common temporal patterns such as triplets and 32th notes. The
note pitch has 128 possibilities, covering from C-1 to G9. For example, a bar in
4/4 time with only one track can be represented as a 96 x 128 matrix.

> Note that during the conversion from MIDI files to pianorolls, an additional
minimal-length (of one time step) pause is added between two consecutive
(without a pause) notes of the same pitch to distinguish them from one single
note.

![pianoroll-example](figs/pianoroll-example.png)
<p class="caption">Example pianoroll</p>

## Multitrack Pianoroll

We represent a multitrack music piece with a _multitrack pianoroll_, which is a
set of pianorolls where each pianoroll represents one specific track in the
original music piece. That is, a _M_-track music piece will be converted into a
set of _M_ pianorolls. For instance, a bar in 4/4 time with _M_ tracks can be
represented as a 96 x 128 x _M_ tensor.

<img src="figs/pianoroll-example-5tracks.png" alt="pianoroll-example-5tracks" style="max-width:400px;">
<p class="caption">Example five-track pianorolls</p>

> The above pianoroll visualizations are produced using
[Pypianoroll](https://salu133445.github.io/pypianoroll/).
