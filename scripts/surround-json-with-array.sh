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

# Given a file with JSON documents per line, this script surrounds all documents
# with an array, and adds a comma between each document.

# check whether a parameter was passed
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

# Rename original dataset.
mv $1.json $1_org.json

# Surround with array brackets and add a comma after each line 
# expect the last one.
# Source: https://stackoverflow.com/questions/35021524/how-can-i-add-a-comma
#         -at-the-end-of-every-line-except-the-last-line/35021663

sed '1s/^/[/;$!s/$/,/;$s/$/]/' $1_org.json > $1.json