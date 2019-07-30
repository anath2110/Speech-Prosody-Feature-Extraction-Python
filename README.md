# prosodyMonsterPython
Extracting only low-level prosody features from speech audios.
Low-level features: 6 (absolute pitch in log Hz, relative pitch which is z-normalized pitch,energy, cepstral flux,speaking frames from pitch and speaking frames from energy.
This is a simplified version of the "monster" code used in "Python_stance-midlevel" repository.
Can be used both for monos and stereos but only .wav files(for now).
Includes codes to get the means and standard deviation of the extracted features.
Also, code for normalizing the features is included.
