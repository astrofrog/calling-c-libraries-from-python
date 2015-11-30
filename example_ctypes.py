import ctypes
from ctypes import cdll, c_char_p

# Load the shared library
lib = cdll.LoadLibrary('functions.so')

# Create a filename as a C char
filename = c_char_p(b'my_file.fits')

# Call the C function
output = lib.dostuff(filename)

# Print the output
print("Output={0}".format(output))