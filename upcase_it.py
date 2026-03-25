#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    removed_file_name = (sys.argv[1:])
    output = " ".join(removed_file_name).upper()
    print(output)

    
