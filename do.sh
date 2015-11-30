#!/bin/bash

# Make shared library
gcc -c -Wall -Werror -fpic functions.c 
gcc -shared -o functions.so functions.o 

# Run Python example with ctypes
python example_ctypes.py