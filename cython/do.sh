#!/bin/bash

# Make shared library
gcc -c -Wall -Werror -fpic functions.c 
gcc -shared -o libfunctions.so functions.o 

# Build cython module
python setup.py build_ext --inplace

# Run cython example
python example_cython.py