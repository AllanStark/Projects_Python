# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import filecmp
import os
def print_diff_files(dcmp):
     for name in dcmp.diff_files:
         print "diff_file %s found in %s and %s" % (name, dcmp.left,
               dcmp.right)
     for sub_dcmp in dcmp.subdirs.values():
         print_diff_files(sub_dcmp)
dcmp = filecmp.dircmp('C:\\Users\\Sorek\\Desktop\\d', 'C:\\Users\\Sorek\\Music') .report()
print_diff_files(dcmp)
# # Determine the items that exist in both directories
# d1_contents = set(os.listdir('C:\\Users\\Sorek\\Desktop\\d'))
# d2_contents = set(os.listdir('C:\\Users\\Sorek\\Music'))
# common = list(d1_contents & d2_contents)
# common_files = [ f for f in common if os.path.isfile(os.path.join('C:\\Users\\Sorek\\Desktop\\d', f))]
# print 'Common files:', common_files

# # Compare the directories
# match, mismatch, errors = filecmp.cmpfiles('C:\\Users\\Sorek\\Desktop\\d', 
#                                            'C:\\Users\\Sorek\\Music', 
#                                            common_files)
# print 'Match:', match
# print 'Mismatch:', mismatch
# print 'Errors:', errorsSS

#https://pymotw.com/2/filecmp/index.html

#Using dircmp to compare 2 dirs
# import filecmp

#filecmp.dircmp('C:\\Users\\Sorek\\Desktop\\d', 'C:\\Users\\Sorek\\Music').report()

#For more detail and recursive comparison using report_full_closure()

#filecmp.dircmp('C:\\Users\\Sorek\\Desktop\\d', 'C:\\Users\\Sorek\\Music').report_full_closure()
#filecmp.dircmp('C:\\Users\\Sorek\\Desktop\\d', 'C:\\Users\\Sorek\\Music').report_partial_closure()


# # Determine the items that exist in both directories
# d1_contents = set(os.listdir('C:\\Users\\Sorek\\Desktop\\d'))
# d2_contents = set(os.listdir('C:\\Users\\Sorek\\Music'))
# common = list(d1_contents & d2_contents)
# common_files = [ f for f in common if os.path.isfile(os.path.join('C:\\Users\\Sorek\\Desktop\\d', f))]
# print 'Common files:', common_files

# # Compare the directories
# match, mismatch, errors = filecmp.cmpfiles('C:\\Users\\Sorek\\Desktop\\d', 
#                                            'C:\\Users\\Sorek\\Music', 
#                                            common_files)
# print 'Match:', match
# print 'Mismatch:', mismatch
# print 'Errors:', errorsSS

#https://pymotw.com/2/filecmp/index.html

#Using dircmp to compare 2 dirs
# import filecmp

#filecmp.dircmp('C:\\Users\\Sorek\\Desktop\\d', 'C:\\Users\\Sorek\\Music').report()

#For more detail and recursive comparison using report_full_closure()

#filecmp.dircmp('C:\\Users\\Sorek\\Desktop\\d', 'C:\\Users\\Sorek\\Music').report_full_closure()
#filecmp.dircmp('C:\\Users\\Sorek\\Desktop\\d', 'C:\\Users\\Sorek\\Music').report_partial_closure()

# https://docs.python.org/2/library/filecmp.html