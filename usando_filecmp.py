# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from filecmp import dircmp
def ArchivosComunes(dcmp):
     for nombre in dcmp.diff_files:
         print "diff_file %s encontrado en %s y en %s" % (nombre, dcmp.left,
               dcmp.right)
     for sub_dcmp in dcmp.subdirs.values():
         ArchivosComunes(sub_dcmp)

dcmp = dircmp('C:\\Users\\Sorek\\Desktop\\d', 'C:\\Users\\Sorek\\Music') 
ArchivosComunes(dcmp)