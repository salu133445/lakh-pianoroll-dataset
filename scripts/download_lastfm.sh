#!/bin/bash
# This script downloads the labels for Million Song Dataset (MSD) from Last.fm
# Dataset (see https://labrosa.ee.columbia.edu/millionsong/lastfm).
# Usage: download_lastfm.sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
DST="${DIR}/../data/lastfm/"
mkdir -p "$DST"
wget -P "$DST" "http://labrosa.ee.columbia.edu/millionsong/sites/default/files/lastfm/lastfm_train.zip"
wget -P "$DST" "http://labrosa.ee.columbia.edu/millionsong/sites/default/files/lastfm/lastfm_test.zip"
wget -P "$DST" "http://labrosa.ee.columbia.edu/millionsong/sites/default/files/lastfm/lastfm_unique_tags.txt"
unzip "$DST/*.zip" -d "$DST"
