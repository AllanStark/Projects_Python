# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
text = open.file(final señales.txt)
#print 'Testing:', __file__ #Current file check
pritn 'Testing', text
print 'Exists:', os.access(__file__, os.F_OK) #verify acces to file
print 'Readable:', os.access(__file__, os.R_OK)#verify acces to read
print 'Writable:', os.access(__file__, os.W_OK)# verify acces to write
print 'Executable:', os.access(__file__, os.X_OK)#verify acces to execute


#https://pymotw.com/2/os/index.html