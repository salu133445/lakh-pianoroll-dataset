#!/bin/bash
# This script downloads the labels for Million Song Dataset (MSD) from Million
# Song Dataset Benchmarks (see http://www.ifs.tuwien.ac.at/mir/msd/).
# Usage: download_amg.sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
DST="${DIR}/../data/amg/"
mkdir -p "$DST"
wget -P "$DST" "http://www.ifs.tuwien.ac.at/mir/msd/partitions/msd-MAGD-genreAssignment.cls"
wget -P "$DST" "http://www.ifs.tuwien.ac.at/mir/msd/partitions/msd-topMAGD-genreAssignment.cls"
wget -P "$DST" "http://www.ifs.tuwien.ac.at/mir/msd/partitions/msd-MASD-styleAssignment.cls"
