#Method --> 1

import os

os.system('ls')



#Method --> 2

from subprocess import call

call('ls')


# Method --> 3

>>> import subprocess
>>> cmd = subprocess.check_output('ls')
>>> print cmd

"""
Conclusion:

the subprocess module, which provides much flexibility when working with Unix commands through its different functions. 

"""

