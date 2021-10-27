# import os
#
# directory = "denis/home/Downloads"
# print(os.listdir(directory))
#

from os import listdir
from os.path import isfile, join
files = [f for f in listdir('/home') if isfile(join('/home', f))]
print(files)
