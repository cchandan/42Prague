#!/usr/bin/python3

import sys

index_counter = -1

if len(sys.argv) < 2:
    print("none")
else:
    for i in range(len(sys.argv)):
        print(sys.argv[index_counter])
        index_counter -= 1
