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

"""analyze-json.py: Given a collection of JSON documents (all nested within a 
JSON array), this script analyzes the object and array fanout, the type 
distribution, the number of nodes, and the depth of the given documents."""

import sys
from argparse import ArgumentParser
import json

# JSON         | Python
# -------------+--------
# object       | dict
# array        | list
# string       | str
# number(int)  | int
# number(real) | float
# true         | True
# false        | False
# null         | None

type_name = ["objects", " arrays", "   keys", " values"]
type_count = [0, 0, 0, 0]
depth = []
object_degree = []
array_degree = []

def analyze(x, level):
    # increment statistics on nodes with certain nesting level
    if len(depth) < level + 1:
        depth.append(0)

    if isinstance(x, dict): # OBJECT
        type_count[0] += 1
        depth[level] += 1
        
        object_degree.append(len(x.items()))
        # Increase depth for keys of a JSON.
        if len(depth) <= level + 1:
            depth.append(0)

        if x != {}:
            for k, v in x.items():
                type_count[2] += 1
                depth[level+1] += 1
                analyze(v, level + 2)
    elif isinstance(x, list): # ARRAY
        type_count[1] += 1
        depth[level] += 1
        
        array_degree.append(len(x))

        if x != []:
            for l in x:
                analyze(l, level + 1)
    else: # VALUE
        type_count[3] += 1
        depth[level] += 1

    return

def main():
    parser = ArgumentParser(description='Input parameters for JSON analysis.')
    parser.add_argument('-f', '--filename', type=str, required=True,
                        help='Filename/-path where the document is stored.')
    args = parser.parse_args()
    global type_count
    global depth
    global object_degree
    global array_degree

    records = 0
    nodes = []
    types = [[],[],[],[]]
    depth_min = []
    depth_avg = []
    depth_max = []
    obj_deg_min = []
    obj_deg_avg = []
    obj_deg_max = []
    arr_deg_min = []
    arr_deg_avg = []
    arr_deg_max = []

    with open(args.filename) as json_file:
        data = json.load(json_file)
        records = len(data)

        for d in data:
            analyze(d, 0)

            nodes.append(sum(type_count))
            for i in range(len(type_count)):
                types[i].append(type_count[i])

            # store depth data
            depth_max.append(len(depth)-1)

            # store object outdegree data
            obj_deg_min.append(min(object_degree, default=0))
            if len(object_degree) == 0:
                obj_deg_avg.append(0)
            else:
                obj_deg_avg.append(sum(object_degree)/len(object_degree))
            obj_deg_max.append(max(object_degree, default=0))

            # store array outdegree data
            arr_deg_min.append(min(array_degree, default=0))
            if len(array_degree) == 0:
                arr_deg_avg.append(0)
            else:
                arr_deg_avg.append(sum(array_degree)/len(array_degree))
            arr_deg_max.append(max(array_degree, default=0))

            type_count = [0, 0, 0, 0]
            depth = []
            object_degree = []
            array_degree = []

    print("GENERAL INFORMATION:")
    print("#record: " + str(records))
    print("#nodes per record: [" + str(min(nodes)) + ", " + str(max(nodes)) + 
            "]  -  avg = " + str(round(sum(nodes)/len(nodes), 2)))
    print()

    print("TYPE distribution:")
    for i in range(len(types)):
        print(str(type_name[i]) + ": [" + str(min(types[i])) + ", " + 
                str(max(types[i])) + "]  -  avg = " + 
                str(round(sum(types[i])/len(types[i]), 2)))
    print()

    print("DEPTH distribution:")
    print("maximum: [" + str(min(depth_max)) + ", " + str(max(depth_max)) + 
            "]  -  avg = " + str(round(sum(depth_max)/len(depth_max), 2)))
    print()

    print("OUTDEGREE distribution OBJECT:")
    print("minimum: [" + str(min(obj_deg_min)) + ", " + str(max(obj_deg_min)) + 
            "]  -  avg = " + str(round(sum(obj_deg_min)/len(obj_deg_min), 2)))
    print("average: [" + str(round(min(obj_deg_avg), 2)) + ", " + 
            str(round(max(obj_deg_avg), 2)) + 
            "]  -  avg = " + str(round(sum(obj_deg_avg)/len(obj_deg_avg), 2)))
    print("maximum: [" + str(min(obj_deg_max)) + ", " + str(max(obj_deg_max)) + 
            "]  -  avg = " + str(round(sum(obj_deg_max)/len(obj_deg_max), 2)))
    print()

    print("OUTDEGREE distribution ARRAY:")
    print("minimum: [" + str(min(arr_deg_min)) + ", " + str(max(arr_deg_min)) + 
            "]  -  avg = " + str(round(sum(arr_deg_min)/len(arr_deg_min), 2)))
    print("average: [" + str(round(min(arr_deg_avg), 2)) + ", " + 
            str(round(max(arr_deg_avg), 2)) + 
            "]  -  avg = " + str(round(sum(arr_deg_avg)/len(arr_deg_avg), 2)))
    print("maximum: [" + str(min(arr_deg_max)) + ", " + str(max(arr_deg_max)) + 
            "]  -  avg = " + str(round(sum(arr_deg_max)/len(arr_deg_max), 2)))
    print()

    return

if __name__ == '__main__':
    main()
