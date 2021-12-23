#!/usr/bin/env python3

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

"""get-query-trees.py: Extract the IDs of query trees from a given JSON document
collection. The query trees are selected based on the quantiles and the 
according thresholds of size 5%, 10%, 20% and 30%."""

import sys
import math
from argparse import ArgumentParser
import subprocess
import statistics

def main(argv):
    # Read command line arguments.
    parser = ArgumentParser(description='Input parameters for query tree \
        extraction')
    parser.add_argument('-i', '--inputfiles', nargs='+', type=str, default=[],
        required=True, help='<Required> Filename/-path where the experimental \
        results are stored.')
    parser.add_argument('-q','--quantiles', type=int, default=0,
        required=True, help='<Required> Give number of quantiles.')
    parser.add_argument('-t','--thresholds', type=int, default=0,
        required=True, help='<Required> Give number of thresholds per \
        quantiles.')
    parser.add_argument('-a','--algorithms', type=int, default=0,
        help='Used algorithms for lookup queries.')
    args = parser.parse_args()

    cargs = ""
    for file in args.inputfiles:
        # Using readlines()
        lines = open(file, 'r').readlines()

        sizes = []
        line_count = 1
        # Strips the newline character
        for line in lines:
            count = 1
            for char in range(1, len(line)):
                if line[char] == "{" and line[char-1] != "\\":
                    count += 1

            sizes.append((count, line_count))
            line_count += 1

        quantiles = statistics.quantiles([x[0] for x in sizes])
        print(quantiles)
        small_query = 0
        medium_query = 0
        large_query = 0

        for (size, idx) in sorted(sizes):
            if small_query == 0 and size >= quantiles[0]:
                small_query = (size, idx)
            elif medium_query == 0 and size >= quantiles[1]:
                medium_query = (size, idx)
            elif large_query == 0 and size >= quantiles[2]:
                large_query = (size, idx)
        print(str(small_query[1]) + "\t(" + str(small_query[0]) + ")\t" + 
                str(math.ceil(small_query[0]*0.05)) + " " + 
                str(math.ceil(small_query[0]*0.1)) + " " + 
                str(math.ceil(small_query[0]*0.2)) + " " + 
                str(math.ceil(small_query[0]*0.3)))
        print(str(medium_query[1]) + "\t(" + str(medium_query[0]) + ")\t" + 
                str(math.ceil(medium_query[0]*0.05)) + " " + 
                str(math.ceil(medium_query[0]*0.1)) + " " + 
                str(math.ceil(medium_query[0]*0.2)) + " " + 
                str(math.ceil(medium_query[0]*0.3)))
        print(str(large_query[1]) + "\t(" + str(large_query[0]) + ")\t" + 
            str(math.ceil(large_query[0]*0.05)) + " " + 
            str(math.ceil(large_query[0]*0.1)) + " " + 
            str(math.ceil(large_query[0]*0.2)) + " " + 
            str(math.ceil(large_query[0]*0.3)))
        

if __name__ == '__main__':
    main(sys.argv)
