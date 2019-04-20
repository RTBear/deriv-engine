#!/usr/bin/python

import argparse
import cv2
import sys
import os
import re
## use import pickle in Py3.
import cPickle as pickle
from matplotlib import pyplot as plt


################################
# module: hist_image_index.py
# Ryan Mecham
# A01839282
################################

# save data to a pickle (.pck) file
def save(obj, file_name):
    with open(file_name, 'wb') as fp:
        pickle.dump(obj, fp)

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

## indexing dictionary.
HIST_INDEX = {}

def hist_index_img(imgp, color_space, bin_size=8):
    print imgp
    img = cv2.imread(imgp)
    ranges = [0,256,0,256,0,256]
    
    if color_space == 'hsv':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        ranges = [0,181,0,256,0,256]
        
    channels = [0,1,2] #ie all the channels
    histSize = [bin_size]*3#for all 3 channels
    
    input_hist = cv2.calcHist(img, channels, None, histSize, ranges)
    norm_hist = cv2.normalize(input_hist, input_hist).flatten()
    
    # plt.plot(norm_hist)
    # plt.xlim(0,255)
    # plt.show()
    HIST_INDEX[imgp] = norm_hist
    return norm_hist

def hist_index_img_dir(imgdir, color_space, bin_size, pick_file):
    print(imgdir)
    fnames = generate_file_names('',imgdir) #'' for any file type in directory (should only contain images)
    for fp in fnames:
        hist_index_img(fp,color_space,bin_size)
    save(HIST_INDEX, pick_file)
    

## ========================= Image Indexing Tests =====================
    
## change these as you see fit.
## IMGDIR is the directory where the images to be indexed are saved.
## PICDIR is the directory where pickled dictionaries are saved.
IMGDIR = './images/'
PICDIR = './pickles/'

def test_01():
    global HIST_INDEX
    HIST_INDEX = {}
    hist_index_img_dir(IMGDIR, 'rgb', 8, PICDIR + 'rgb_hist8.pck')

def test_02(): 
    global HIST_INDEX
    HIST_INDEX = {}
    hist_index_img_dir(IMGDIR, 'rgb', 16, PICDIR + 'rgb_hist16.pck')

def test_03():
    global HIST_INDEX
    HIST_INDEX = {}
    hist_index_img_dir(IMGDIR, 'hsv', 8, PICDIR + 'hsv_hist8.pck')

def test_04():
    global HIST_INDEX
    HIST_INDEX = {}
    hist_index_img_dir(IMGDIR, 'hsv', 16, PICDIR + 'hsv_hist16.pck')


if __name__ == '__main__':
    pass
    test_01()
    test_02()
    test_03()
    test_04()


    # hist_index_img('./images/16_07_02_14_21_00_orig.png','rgb',8)
    # hist_index_img('./images/16_07_02_14_21_00_orig.png','hsv',8)
