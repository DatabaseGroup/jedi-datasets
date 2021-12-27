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

"""generate-json.py: Based on multiple input parameters this script generates 
random JSON documents. In case that the diff parameter is set, a certain number 
of edit operations are applied to each JSON document. Both documents, the 
original and the edited one, are stored along with their distance value, 
introduced by the edits."""

from argparse import ArgumentParser
import urllib.request
import sys
import json
import random
import string

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

def random_string(string_length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

def get_size_json(doc):
    """Returns the size of the corresponding tree of the given JSON."""

    size = 0
    if isinstance(doc, dict): # OBJECT
        # Count the node of the object and all its keys.
        size += 1 + len(doc.keys())
        # Add the sizes of all values.
        for key, val in doc.items():
            size += get_size_json(val)
    elif isinstance(doc, list): # ARRAY
        # Count the node of the array and all its array order nodes.
        size += 1 + len(doc)
        # Add the sizes of all values.
        for val in doc:
            size += get_size_json(val)
    else: # VALUE
        # Add node for the value.
        size += 1

    return size


def perform_edit(doc, nr):
    """Given a JSON document doc, this function performs a random edit 
    operation at a certain node with a given number nr."""

    # Count the cost of the performed edit operation.
    cost = 0

    # The given JSON document can either be an object, an array, or a value.
    ### OBJECT
    if isinstance(doc, dict):
        # If nr is 0, the target node has been found.
        if nr == 0:
            max_edit = 2
            # If the object is empty, allow only insert operations.
            if len(doc.keys()) == 0:
                max_edit = 0
            # Randomly choose edit operation.
            edit = random.randint(0, max_edit)

            # Perform chosen edit operation.
            ### Insert a key-value pair.
            if edit == 0:
                key = random_string(random.randint(1, 10))
                value = generate_json(0, 3, 0, 4, 0, 3)
                # Random (small) values to generate a new JSON value for the 
                # new key.
                doc[key] = value
                # Cost for inserting a key and its value.
                cost += 1 + get_size_json(value)
                print("  A.1 insert key-value pair with key " + str(key) + 
                    " and value " + str(value) + "; cost=" + 
                    str(1 + get_size_json(value)))
            ### Delete a key-value pair.
            elif edit == 1:
                key = random.choice(list(doc.keys()))
                c = 1 + get_size_json(doc[key])
                value = doc.pop(key)
                cost += 1
                print("  A.2 delete key-value pair with key " + str(key) + 
                    " and value " + str(value)  + "; cost=1")
            ### Rename a key.
            elif edit == 2:
                old_key = random.choice(list(doc.keys()))
                new_key = random_string(random.randint(1, 10))
                doc[new_key] = doc.pop(old_key)
                cost += 1
                print("  A.3 rename key from " + str(old_key) + " to " + 
                    str(new_key) + "; cost=1")
            ### Nest a child by one level (object or array).
            elif edit == 3:
                # Randomly chose a key where the object is nested at.
                key = random.choice(list(doc.keys()))
                value = doc[key]
                # Decide whether to nest with an array or an object.
                nest = random.randint(0, 1)
                if nest == 0: # NEST IN OBJECT
                    obj = {}
                    obj[random_string(random.randint(1, 10))] = value
                    doc[key] = obj
                    cost += 2
                    print("  A.3.1 object value " + str(value) + 
                        " is nested in object; cost=2")
                elif nest == 1: # NEST IN ARRAY
                    doc[key] = [value]
                    cost += 1
                    print("  A.3.2 object value " + str(value) + 
                        " is nested in array; cost=1")
        # If nr is greater than 0, recursively look for the target node.
        # Or edit key.
        else:
            nr -= 1
            for key, val in doc.items():
                ### Nest the value of this key by one level (object or array).
                if nr == 0:
                    # Randomly chose a key where the object is nested at.
                    value = doc[key]
                    # Decide whether to nest with an array or an object.
                    nest = random.randint(0, 1)
                    if nest == 0: # NEST IN OBJECT
                        obj = {}
                        obj[random_string(random.randint(1, 10))] = value
                        doc[key] = obj
                        cost += 2
                        print("  D.1.1 object value " + str(value) + 
                            " is nested in object; cost=2")
                    elif nest == 1: # NEST IN ARRAY
                        doc[key] = [value]
                        cost += 1
                        print("  D.1.2 object value " + str(value) + 
                            " is nested in array; cost=1")
                    break
                else:
                    nr -= 1 # Remove number for key.
                    doc[key], c = perform_edit(val, nr)
                    cost += c
                    nr -= get_size_json(doc[key])
    
    ### ARRAY
    elif isinstance(doc, list):
        if nr == 0:
            max_edit = 3
            # If the array is empty, insert a value.
            if len(doc) == 0:
                max_edit = 0
            # If the array size is one, the order cannot be exchanged.
            elif len(doc) == 1:
                max_edit = 2
            edit = random.randint(0, max_edit)

            ### Insert value.
            if edit == 0:
                value = generate_json(0, 3, 0, 4, 0, 3)
                pos = random.randint(0, len(doc))
                doc.insert(pos, value)
                cost += get_size_json(value)
                print("  B.1 add value " + str(value) + " at position " + 
                    str(pos) + "; cost=" + str(get_size_json(value)))
            ### Delete value.
            elif edit == 1:
                pos = random.randint(0, len(doc)-1)
                # The costs are deleting the array order node and the value.
                c = 1 + get_size_json(doc[pos])
                cost += c
                doc.pop(pos)
                print("  B.2 delete value at position " + str(pos) + 
                    "; cost=" + str(c))
            elif edit == 2: # change order
                exchange = random.sample(range(len(doc)), 2)
                temp = doc[exchange[0]]
                doc[exchange[0]] = doc[exchange[1]]
                doc[exchange[1]] = temp
                cost += 2
                print("  B.3 exchange order; " + str(exchange[0]) + " to " + 
                    str(exchange[1]) + "; cost=2")
        else: # Otherwise, find node recursively.
            nr -= 1
            for eid in range(len(doc)):
                ### Nest this value by one level (object or array).
                if nr == 0:
                    value = doc[eid]
                    # Decide whether to nest with an array or an object.
                    nest = random.randint(0, 1)
                    if nest == 0: # NEST IN OBJECT
                        obj = {}
                        obj[random_string(random.randint(1, 10))] = value
                        doc[eid] = obj
                        cost += 2
                        print("  E.1.1 array value " + str(value) + 
                            " is nested in object; cost=2")
                    elif nest == 1: # NEST IN ARRAY
                        doc[eid] = [value]
                        cost += 1
                        print("  E.1.2 array value " + str(value) + 
                            " is nested in array; cost=1")
                    break
                else:
                    nr -= 1 # Remove number for array order node.
                    doc[eid], c = perform_edit(doc[eid], nr)
                    cost += c
                    nr -= get_size_json(doc[eid])
    
    ### VALUE
    else:
        # Change value to a new value.
        if nr == 0:
            old = doc
            doc = generate_json(0, 0, 0, 0, 0, 1)
            cost += 1
            print("  C.1 change value from " + str(old) + " to " + str(doc) + 
                "; cost=1")

    return doc, cost


def modify_json(doc, edits):
    """Given an original JSON document, this function performs a given number 
    of edit operations on it."""

    # Sum up the cost of all edits.
    sum_cost = 0

    # Pick edits many nodes from the original JSON document.
    doc_size = get_size_json(doc)
    # If the given JSON has less nodes than edits, use at most document size 
    # many.
    if edits > doc_size:
        edits = doc_size
    # Generate set of nodes that should be edited. Sort such that nodes with 
    # the highest numbers are processed first.
    edit_nodes = sorted(random.sample(range(doc_size), edits), reverse=True)

    # Perform edits many edit operations.
    for e in edit_nodes:
        doc, cost = perform_edit(doc, e)
        sum_cost += cost

    return doc, sum_cost


def generate_json(minofan, maxofan, minafan, maxafan, minnest, maxnest, 
        nostr=False, nonum=False, nobool=False, nonull=False):
    """Generate a random json document based on the given specification."""

    # Create initial JSON document
    json_doc = None

    # Randomly creates either an object (0), an array (1), or a value (2).
    insert_type = random.random()

    # If maximum level of nesting is reached, return a basic value.
    if maxnest == 1:
        insert_type = 1.0
    
    if insert_type <= 0.35: # OBJECT
        json_doc = {}
        # Generate fanout many children for this JSON object. The fanout is 
        # bounded by the given parameters and has a mode at 20%.
        keys = []
        for x in range(round(random.triangular(minofan, maxofan, 
                minofan+((maxofan-minofan)*0.2)))):
            keys.append(random_string(random.randint(1, 10)))
        for key in keys:
            # Generate a random JSON value with reduced nesting depth.
            json_doc[key] = generate_json(minofan, maxofan, minafan, maxafan, 
                minnest, maxnest-1, nostr, nonum, nobool, nonull)
    elif insert_type > 0.35 and insert_type <= 0.45: # ARRAY
        json_doc = []
        # Generate fanout many elements for this JSON array.
        nr_elements = round(random.triangular(minafan, maxafan, 
            minafan+((maxafan-minafan)*0.2)))
        for e in range(nr_elements):
            json_doc.append(generate_json(minofan, maxofan, minafan, maxafan, 
                minnest, maxnest-1, nostr, nonum, nobool, nonull))
    elif insert_type > 0.45 and insert_type <= 1.0: # VALUE
        # Randomly creates either a string (0), a number (1), a boolean (2), or 
        # null (3).
        insert_value = random.random()
        if insert_value <= 0.4: # STRING
            json_doc = random_string(random.randint(1, 10))
        elif insert_value > 0.4 and insert_value <= 0.8: # NUMBER
            json_doc = random.randint(0, 100)
        elif insert_value > 0.8 and insert_value <= 0.95: # BOOLEAN
            if random.randint(0, 1) == 0:
                json_doc = False
            else:
                json_doc = True
        elif insert_value > 0.95 and insert_value <= 1.0: # NULL
            json_doc = None

    return json_doc


def main():
    # Read command line arguments.
    parser = ArgumentParser(description='Input parameters for json generator')
    parser.add_argument('--minofan', type=int, default=0,
                        help='Minimum number of key-value pairs of an object.')
    parser.add_argument('--maxofan', type=int, default=4,
                        help='Maximum number of key-value pairs of an object.')
    parser.add_argument('--minafan', type=int, default=0,
                        help='Minimum number of values of an array.')
    parser.add_argument('--maxafan', type=int, default=6,
                        help='Maximum number of values of an array.')
    parser.add_argument('--minnest', type=int, default=0,
                        help='Minimum number of nested JSON values.')
    parser.add_argument('--maxnest', type=int, default=4,
                        help='Maximum number of nested JSON values.')
    parser.add_argument('--nostr', default=False, action='store_false',
                        help='Set flag to disable string values.')
    parser.add_argument('--nonum', default=False, action='store_false',
                        help='Set flag to disable numerical values.')
    parser.add_argument('--nobool', default=False, action='store_false',
                        help='Set flag to disable boolean values.')
    parser.add_argument('--nonull', default=False, action='store_false',
                        help='Set flag to disable null values.')
    parser.add_argument('--seed', type=int, default=0,
                        help='Set random seed (default=0).')
    parser.add_argument('--diff', type=int, default=0,
                        help='Create two versions of each JSON and set the \
                        maximum number of edits between them (default=0).')
    parser.add_argument('--collection', type=int, default=1,
                        help='Create a collection with argument many records.')
    parser.add_argument('--filename', type=str, default="",
                        help='Filename/-path where the collection is stored.')
    parser.add_argument('--print', action='store_true',
                        help='Print the generated collection.')
    args = parser.parse_args()

    # Set the seed for the random number generator.
    seed = args.seed
    if(args.seed == 0): # If no seed is given, create random seed.
        seed = random.randrange(sys.maxsize)
    random.seed(seed)
    

    # Print input parameters.
    print("+--------------------------------------------+")
    print("| GENERATE JSON:                             |")
    print("+--------------------------------------------+")
    print("|        Filename/-path: " + str(args.filename))
    print("|       Collection size: " + str(args.collection))
    print("| Minimum object fanout: " + str(args.minofan))
    print("| Maximum object fanout: " + str(args.maxofan))
    print("|  Minimum array fanout: " + str(args.minafan))
    print("|  Maximum array fanout: " + str(args.maxafan))
    print("|       Minimum nesting: " + str(args.minnest))
    print("|       Maximum nesting: " + str(args.maxnest))
    print("|      No string values: " + str(args.nostr))
    print("|     No numeric values: " + str(args.nonum))
    print("|     No boolean values: " + str(args.nobool))
    print("|        No null values: " + str(args.nonull))
    print("|           Random seed: " + str(seed))
    print("+--------------------------------------------+")


    # Open specified file that stores the generated data.
    if args.filename != "":
        outfile = open(args.filename, 'w')

    # Generate a collection of given size with random JSON documents.
    for x in range(args.collection):
        if args.print:
            print("Generate " + str(x) + ". JSON document...")
        json_doc = generate_json(args.minofan, args.maxofan, 
            args.minafan, args.maxafan, args.minnest, args.maxnest, 
            args.nostr, args.nonum, args.nobool, args.nonull)
        if args.filename != "":
            json.dump(json_doc, outfile)
            outfile.write("\n")
        if args.print:
            print(json.dumps(json_doc))
        if args.diff > 0:
            diff, distance = modify_json(json_doc, args.diff)
            if args.filename != "":
                json.dump(diff, outfile)
                outfile.write("\n" + str(distance) + "\n")
            if args.print:
                print()
                print(json.dumps(diff))
                print(str(distance))
                print()

    # Close specified file that stores the generated data.
    if args.filename != "":
        outfile.close()

    return

if __name__ == '__main__':
    main()
