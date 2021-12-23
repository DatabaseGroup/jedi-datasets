#!/bin/bash

# The MIT License (MIT)
# Copyright (c) 2021 Thomas Hütter.
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

echo "This might take some minutes..."

# Create raw data directory in case it does not exist.
echo "Download raw data (1/2)"
mkdir -p raw-data
cd raw-data

# Clone raw data from the data repositories. Downloading GBs of data may take a 
# while.
git clone https://frosch.cosy.sbg.ac.at/datasets/json/arxiv.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/trees.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/reads.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/virus.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/dblp.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/nba.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/twitter.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/clothing.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/face.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/fda.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/cards.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/nasa.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/movies.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/reddit.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/recipes.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/schema.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/smsen.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/smszh.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/spotify.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/standev.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/stantrain.git
git clone https://frosch.cosy.sbg.ac.at/datasets/json/twitter2.git

# Create input data directories in case they do not exist.
echo "Prepare input data (2/2)"
cd ..
mkdir -p input-data/arxiv
mkdir -p input-data/trees
mkdir -p input-data/reads
mkdir -p input-data/virus
mkdir -p input-data/dblp
mkdir -p input-data/nba
mkdir -p input-data/twitter
mkdir -p input-data/clothing
mkdir -p input-data/face
mkdir -p input-data/fda
mkdir -p input-data/cards
mkdir -p input-data/nasa
mkdir -p input-data/movies
mkdir -p input-data/reddit
mkdir -p input-data/recipes
mkdir -p input-data/schema
mkdir -p input-data/smsen
mkdir -p input-data/smszh
mkdir -p input-data/spotify
mkdir -p input-data/standev
mkdir -p input-data/stantrain
mkdir -p input-data/twitter2

# Prepare the input data from the raw data.
python scripts/json2bracket.py -i raw-data/arxiv/arxiv.json -o input-data/arxiv/arxiv.bracket
python scripts/json2bracket.py -i raw-data/trees/trees.json -o input-data/trees/trees.bracket
python scripts/json2bracket.py -i raw-data/reads/reads.json -o input-data/reads/reads.bracket
python scripts/json2bracket.py -i raw-data/virus/virus.json -o input-data/virus/virus.bracket
python scripts/json2bracket.py -i raw-data/dblp/dblp.json -o input-data/dblp/dblp.bracket
python scripts/json2bracket.py -i raw-data/nba/nba.json -o input-data/nba/nba.bracket
python scripts/json2bracket.py -i raw-data/twitter/twitter.json -o input-data/twitter/twitter.bracket
python scripts/json2bracket.py -i raw-data/clothing/clothing.json -o input-data/clothing/clothing.bracket
python scripts/json2bracket.py -i raw-data/face/face.json -o input-data/face/face.bracket
python scripts/json2bracket.py -i raw-data/fda/fda.json -o input-data/fda/fda.bracket
python scripts/json2bracket.py -i raw-data/cards/cards.json -o input-data/cards/cards.bracket
python scripts/json2bracket.py -i raw-data/nasa/nasa.json -o input-data/nasa/nasa.bracket
python scripts/json2bracket.py -i raw-data/movies/movies.json -o input-data/movies/movies.bracket
python scripts/json2bracket.py -i raw-data/reddit/reddit.json -o input-data/reddit/reddit.bracket
python scripts/json2bracket.py -i raw-data/recipes/recipes.json -o input-data/recipes/recipes.bracket
python scripts/json2bracket.py -i raw-data/schema/schema.json -o input-data/schema/schema.bracket
python scripts/json2bracket.py -i raw-data/smsen/smsen.json -o input-data/smsen/smsen.bracket
python scripts/json2bracket.py -i raw-data/smszh/smszh.json -o input-data/smszh/smszh.bracket
python scripts/json2bracket.py -i raw-data/spotify/spotify.json -o input-data/spotify/spotify.bracket
python scripts/json2bracket.py -i raw-data/standev/standev.json -o input-data/standev/standev.bracket
python scripts/json2bracket.py -i raw-data/stantrain/stantrain.json -o input-data/stantrain/stantrain.bracket
python scripts/json2bracket.py -i raw-data/twitter2/twitter2.json -o input-data/twitter2/twitter2.bracket