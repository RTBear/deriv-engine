#!/usr/bin/python

#########################################
# module: hw07_s19.py
# Ryan Mecham
# A01839282
#########################################

import argparse
import math
import os
import re
import sys

import cv2
import numpy as np

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
    fnames = generate_file_names(ftype, imgdir)
    image_files = []

    for f in fnames:
        image_files.append((f, cv2.imread(f)))

    return image_files

def grayscale(i, imglst):
    cv2.imshow(imglst[i][0],imglst[i][1])
    cv2.imshow('Grayscaled', cv2.cvtColor(imglst[i][1], cv2.COLOR_BGR2GRAY))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def split_merge(i, imglst):
    cv2.imshow(imglst[i][0],imglst[i][1])

    blue_channel, green_channel, red_channel = cv2.split(imglst[i][1])
    zero_channel = np.zeros((len(imglst[i][1]),len(imglst[i][1][0])))

    red_filter = np.dstack((zero_channel,zero_channel,red_channel))
    blue_filter = np.dstack((blue_channel,zero_channel,zero_channel))
    green_filter = np.dstack((zero_channel,green_channel,zero_channel))

    cv2.imshow('Red', red_filter.astype('uint8'))#cv2 wants type 'uint8' and each filter is 'float64' by default
    cv2.imshow('Blue', blue_filter.astype('uint8'))
    cv2.imshow('Green', green_filter.astype('uint8'))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def amplify(i, imglst, c, amount):
    assert c == 'b' or c == 'g' or c == 'r'
    cv2.imshow(imglst[i][0],imglst[i][1])

    if c == 'b':
        amp_index = 0 
    elif c == 'g':
        amp_index = 1 
    elif c == 'r':
        amp_index = 2 

    amp = imglst[i][1][:,:,:]
    amp[:,:,amp_index] += amount

    cv2.imshow('Amplified',amp)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


## here is main for you to test your implementations.
## remember to destroy all windows after you are done.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ftype', default='.jpg', nargs='?', help='filetype of images')#nargs='?' means 0 or 1 args
    parser.add_argument('--imgdir', default='.', nargs='?', help='path to image directory')

    args = parser.parse_args()

    print 'ftype:',args.ftype
    print 'imgdir:',args.imgdir

    il = read_img_dir(args.ftype, args.imgdir)
    # print il[0]
    print len(il), il[0][1].shape

    #verify_img_list(il)
    # grayscale(0, il)
    # split_merge(0, il)
    # amplify(0, il, 'b', 200)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
