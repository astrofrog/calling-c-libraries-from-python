from _example_cython import dostuff_cython

# Call cython wrapper
output = dostuff_cython(b"myfile.fits")

# Print the output
print("Output={0}".format(output))