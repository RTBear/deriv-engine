#!/usr/bin/python

#########################################
# module: hw07_s19.py
# YOUR NAME
# YOUR A#
#########################################

import math
import numpy as np
import argparse
import cv2
import sys
import os
import re

## uses these command line options if you want to run your program
## in a command window.
#ap = argparse.ArgumentParser()
#ap.add_argument('-id', '--imgdir', required = True, help = 'image directory')
#ap.add_argument('-ft', '--ftype', required = True, help = 'file type (e.g., .png)')
#args = vars(ap.parse_args())

def generate_file_names(ftype, rootdir):
    '''
    recursively walk dir tree beginning from rootdir
    and generate full paths to all files that end with ftype.
    sample call: generate_file_names('.jpg', /home/pi/images/')
    '''
    for path, dirlist, filelist in os.walk(rootdir):
        for file_name in filelist:
            if not file_name.startswith('.') and \
               file_name.endswith(ftype):
                yield os.path.join(path, file_name)
        for d in dirlist:
            generate_file_names(ftype, d)

def read_img_dir(ftype, imgdir):
    ## your code here
    pass

def grayscale(i, imglst):
    ## your code here
    pass

def split_merge(i, imglst):
    ## your code here
    pass

def amplify(i, imglst, c, amount):
    ## your code here
    pass

## here is main for you to test your implementations.
## remember to destroy all windows after you are done.
if __name__ == '__main__':
    #il = read_img_dir(args['ftype'], args['imgdir'])
    #verify_img_list(il)
    #grayscale(0, il)
    #split_merge(0, il)
    #amplify(0, il, 'b', 200)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    pass
    


 
