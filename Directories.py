# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
Program that show how to create and manipulate files and directories
'''

import os
#to assign the name of directory
dir_name = 'pythonProjectdds'
#os.makedirs() creates a dir
print 'Creating', dir_name
os.makedirs(dir_name)
#Assign name to a new text file and is included into the directory
file_name = os.path.join(dir_name, 'porejemplo.txt')
#to show the new file_name = porejemplo.txt
print 'Creating', file_name
#opening the file_name with writting permission
f = open(file_name, 'wt')
try:
    f.write('Este es un ejemplo que anade esta linea al texto')#to write the file
finally:
    f.close() #to close file

print 'Listing', dir_name #to show name of directory
print os.listdir(dir_name) #show files into the directory

#To clean and remove files
# print 'Cleaning up'
# os.unlink(file_name)
# os.rmdir(dir_name)

# https://pymotw.com/2/os/index.html