#!/bin/bash

# The MIT License (MIT)
# Copyright (c) 2021 Thomas Huetter.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# The raw JSON datasets are fetched from repositories (see directory `raw-data`)
# and converted into bracket notation which serves as the input data for the
# algorithms (see directory `input-data`). Further, the characteristics of the
# datasets are analyzed.

start_time=$SECONDS
echo "This process takes approximately one hour for all datasets. One might 
consider to exclude datasets that are not needed."

# Create raw data directory in case it does not exist.
echo "Download raw data (1/3)"
mkdir -p raw-data
cd raw-data

# Clone raw data from the data repositories. Downloading GBs of data may take a 
# while.
git clone https://frosch.cosy.sbg.ac.at/datasets/json/arxiv.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/cards.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/clothing.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/dblp.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/denf.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/device.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/face.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/fenf.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/movies.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/nasa.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/nba.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/reads.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/recipes.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/reddit.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/schema.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/smsen.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/smszh.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/spotify.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/standev.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/stantrain.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/trees.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/twitter.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/twitter2.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/virus.git

# Create input data directories in case they do not exist.
echo "Prepare input data (2/3)"
cd ..
mkdir -p input-data/arxiv
mkdir -p input-data/cards
mkdir -p input-data/clothing
mkdir -p input-data/dblp
mkdir -p input-data/denf
mkdir -p input-data/device
mkdir -p input-data/face
mkdir -p input-data/fenf
mkdir -p input-data/movies
mkdir -p input-data/nasa
mkdir -p input-data/nba
mkdir -p input-data/reads
mkdir -p input-data/recipes
mkdir -p input-data/reddit
mkdir -p input-data/schema
mkdir -p input-data/smsen
mkdir -p input-data/smszh
mkdir -p input-data/spotify
mkdir -p input-data/standev
mkdir -p input-data/stantrain
mkdir -p input-data/trees
mkdir -p input-data/twitter
mkdir -p input-data/twitter2
mkdir -p input-data/virus

# Convert the raw JSON data into the bracket notation input data format. Sort 
# the sibling order to apply the JediOrder upper bound on ordered siblings.
echo " * Processing arxiv ...\c"
python scripts/json2bracket.py -f raw-data/arxiv/arxiv.json -c -s > input-data/arxiv/arxiv.bracket
echo " Done"
echo " * Processing cards ...\c"
python scripts/json2bracket.py -f raw-data/cards/cards.json -c -s > input-data/cards/cards.bracket
echo " Done"
echo " * Processing clothing ...\c"
python scripts/json2bracket.py -f raw-data/clothing/clothing.json -c -s > input-data/clothing/clothing.bracket
echo " Done"
echo " * Processing dblp ...\c"
python scripts/json2bracket.py -f raw-data/dblp/dblp.json -c -s > input-data/dblp/dblp.bracket
echo " Done"
echo " * Processing denf ...\c"
python scripts/json2bracket.py -f raw-data/denf/denf.json -c -s > input-data/denf/denf.bracket
echo " Done"
echo " * Processing device ...\c"
python scripts/json2bracket.py -f raw-data/device/device.json -c -s > input-data/device/device.bracket
echo " Done"
echo " * Processing face ...\c"
python scripts/json2bracket.py -f raw-data/face/face.json -c -s > input-data/face/face.bracket
echo " Done"
echo " * Processing fenf ...\c"
python scripts/json2bracket.py -f raw-data/fenf/fenf.json -c -s > input-data/fenf/fenf.bracket
echo " Done"
echo " * Processing movies ...\c"
python scripts/json2bracket.py -f raw-data/movies/movies.json -c -s > input-data/movies/movies.bracket
echo " Done"
echo " * Processing nasa ...\c"
python scripts/json2bracket.py -f raw-data/nasa/nasa.json -c -s > input-data/nasa/nasa.bracket
echo " Done"
echo " * Processing nba ...\c"
python scripts/json2bracket.py -f raw-data/nba/nba.json -c -s > input-data/nba/nba.bracket
echo " Done"
echo " * Processing reads ...\c"
python scripts/json2bracket.py -f raw-data/reads/reads.json -c -s > input-data/reads/reads.bracket
echo " Done"
echo " * Processing recipes ...\c"
python scripts/json2bracket.py -f raw-data/recipes/recipes.json -c -s > input-data/recipes/recipes.bracket
echo " Done"
echo " * Processing reddit ...\c"
python scripts/json2bracket.py -f raw-data/reddit/reddit.json -c -s > input-data/reddit/reddit.bracket
echo " Done"
echo " * Processing schema ...\c"
python scripts/json2bracket.py -f raw-data/schema/schema.json -c -s > input-data/schema/schema.bracket
echo " Done"
echo " * Processing smsen ...\c"
python scripts/json2bracket.py -f raw-data/smsen/smsen.json -c -s > input-data/smsen/smsen.bracket
echo " Done"
echo " * Processing smszh ...\c"
python scripts/json2bracket.py -f raw-data/smszh/smszh.json -c -s > input-data/smszh/smszh.bracket
echo " Done"
echo " * Processing spotify ...\c"
python scripts/json2bracket.py -f raw-data/spotify/spotify.json -c -s > input-data/spotify/spotify.bracket
echo " Done"
echo " * Processing standev ...\c"
python scripts/json2bracket.py -f raw-data/standev/standev.json -c -s > input-data/standev/standev.bracket
echo " Done"
echo " * Processing stantrain ...\c"
python scripts/json2bracket.py -f raw-data/stantrain/stantrain.json -c -s > input-data/stantrain/stantrain.bracket
echo " Done"
echo " * Processing trees ...\c"
python scripts/json2bracket.py -f raw-data/trees/trees.json -c -s > input-data/trees/trees.bracket
echo " Done"
echo " * Processing twitter ...\c"
python scripts/json2bracket.py -f raw-data/twitter/twitter.json -c -s > input-data/twitter/twitter.bracket
echo " Done"
echo " * Processing twitter2 ...\c"
python scripts/json2bracket.py -f raw-data/twitter2/twitter2.json -c -s > input-data/twitter2/twitter2.bracket
echo " Done"
echo " * Processing virus ...\c"
python scripts/json2bracket.py -f raw-data/virus/virus.json -c -s > input-data/virus/virus.bracket
echo " Done"

# Create input data directories in case they do not exist.
echo "Analyze data (3/3)"
mkdir -p analysis/

# Analyze datasets.
echo " * Analyze arxiv ...\c"
python scripts/analyze-json.py -f raw-data/arxiv/arxiv.json > analysis/arxiv.txt
echo " Done"
echo " * Analyze cards ...\c"
python scripts/analyze-json.py -f raw-data/cards/cards.json > analysis/cards.txt
echo " Done"
echo " * Analyze clothing ...\c"
python scripts/analyze-json.py -f raw-data/clothing/clothing.json > analysis/clothing.txt
echo " Done"
echo " * Analyze dblp ...\c"
python scripts/analyze-json.py -f raw-data/dblp/dblp.json > analysis/dblp.txt
echo " Done"
echo " * Analyze denf ...\c"
python scripts/analyze-json.py -f raw-data/denf/denf.json > analysis/denf.txt
echo " Done"
echo " * Analyze device ...\c"
python scripts/analyze-json.py -f raw-data/device/device.json > analysis/device.txt
echo " Done"
echo " * Analyze face ...\c"
python scripts/analyze-json.py -f raw-data/face/face.json > analysis/face.txt
echo " Done"
echo " * Analyze fenf ...\c"
python scripts/analyze-json.py -f raw-data/fenf/fenf.json > analysis/fenf.txt
echo " Done"
echo " * Analyze movies ...\c"
python scripts/analyze-json.py -f raw-data/movies/movies.json > analysis/movies.txt
echo " Done"
echo " * Analyze nasa ...\c"
python scripts/analyze-json.py -f raw-data/nasa/nasa.json > analysis/nasa.txt
echo " Done"
echo " * Analyze nba ...\c"
python scripts/analyze-json.py -f raw-data/nba/nba.json > analysis/nba.txt
echo " Done"
echo " * Analyze reads ...\c"
python scripts/analyze-json.py -f raw-data/reads/reads.json > analysis/reads.txt
echo " Done"
echo " * Analyze recipes ...\c"
python scripts/analyze-json.py -f raw-data/recipes/recipes.json > analysis/recipes.txt
echo " Done"
echo " * Analyze reddit ...\c"
python scripts/analyze-json.py -f raw-data/reddit/reddit.json > analysis/reddit.txt
echo " Done"
echo " * Analyze schema ...\c"
python scripts/analyze-json.py -f raw-data/schema/schema.json > analysis/schema.txt
echo " Done"
echo " * Analyze smsen ...\c"
python scripts/analyze-json.py -f raw-data/smsen/smsen.json > analysis/smsen.txt
echo " Done"
echo " * Analyze smszh ...\c"
python scripts/analyze-json.py -f raw-data/smszh/smszh.json > analysis/smszh.txt
echo " Done"
echo " * Analyze spotify ...\c"
python scripts/analyze-json.py -f raw-data/spotify/spotify.json > analysis/spotify.txt
echo " Done"
echo " * Analyze standev ...\c"
python scripts/analyze-json.py -f raw-data/standev/standev.json > analysis/standev.txt
echo " Done"
echo " * Analyze stantrain ...\c"
python scripts/analyze-json.py -f raw-data/stantrain/stantrain.json > analysis/stantrain.txt
echo " Done"
echo " * Analyze trees ...\c"
python scripts/analyze-json.py -f raw-data/trees/trees.json > analysis/trees.txt
echo " Done"
echo " * Analyze twitter ...\c"
python scripts/analyze-json.py -f raw-data/twitter/twitter.json > analysis/twitter.txt
echo " Done"
echo " * Analyze twitter2 ...\c"
python scripts/analyze-json.py -f raw-data/twitter2/twitter2.json > analysis/twitter2.txt
echo " Done"
echo " * Analyze virus ...\c"
python scripts/analyze-json.py -f raw-data/virus/virus.json > analysis/virus.txt
echo " Done"

elapsed=$(( SECONDS - start_time ))
echo "Datasets were downloaded and pre-processed in" $elapsed "seconds."