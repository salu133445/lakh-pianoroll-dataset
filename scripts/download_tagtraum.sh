#!/bin/bash
# This script downloads the labels for Million Song Dataset (MSD) from Tagtraum
# genre annotations (see http://www.tagtraum.com/msd_genre_datasets.html).
# Usage: download_tagtraum.sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
DST="${DIR}/../data/tagtraum/"
mkdir -p "$DST"
wget -P "$DST" "http://www.tagtraum.com/genres/msd_tagtraum_cd1.cls.zip"
wget -P "$DST" "http://www.tagtraum.com/genres/msd_tagtraum_cd2.cls.zip"
wget -P "$DST" "http://www.tagtraum.com/genres/msd_tagtraum_cd2c.cls.zip"
unzip "$DST/*.zip" -d "$DST"
