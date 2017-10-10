"""
Numpy:
======
NumPy, which stands for Numerical Python, is a library consisting of multidimensional array objects and a collection of 
routines  for processing those arrays.

"""


#List vs numpy Example

"""
numpy arrays take lesser momory over lists. since they take lesser memory thy are faster in execution

"""

import numpy as np #import numpy module
import sys         #import sys module



s = range(1000) # creating a list with 1000 items
print(sys.getsizeof(5) * len(s)) # will print memory occopied by s list i.e 24000


d = np.arange(1000)
print(d.size * d.itemsize)     # will print memory occopied by d numpy array i.e 8000


"""
in the above example both 's' list and 'd' numpy array have same data but their memory is different.
"""
