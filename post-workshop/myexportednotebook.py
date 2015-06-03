# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

import numpy as np
import matplotlib.pyplot as plt
import sys

def bs_to_float(v):
    if v == 'b':
        return 0
    elif v == 's':
        return 1
    raise Exception('bs_to_float is expecting the value to be b or s')

assert bs_to_float("b") == 0
assert bs_to_float("s") == 1

the_index_of_the_label_column = -1
converter_dictionary = { the_index_of_the_label_column: bs_to_float }

# in bash: thefilename = $1
print sys.argv
thefilename = sys.argv[1]

data = np.loadtxt(thefilename, delimiter=',',
                  skiprows=1, converters=converter_dictionary)

n_signal = np.sum(data[:, -1])
print "There are", n_signal, "'signal' data points"


is_row_undefined = np.any(data == -999, axis=1)

is_row_defined = is_row_undefined == False

defined_data = data[ is_row_defined ]

centralized_data = defined_data - defined_data.mean(axis=0)
centralized_data = centralized_data / centralized_data.std(axis=0)

cmatrix = np.matrix(centralized_data)
cov = cmatrix.T * cmatrix


plt.imshow(cov, interpolation='nearest')
#plt.ion()
#plt.hold()

if len(sys.argv) > 2:
    plt.savefig(sys.argv[2])
else:
    plt.show()

#plt.imshow(cov, interpolation='nearest')
#plt.show()



