#!/usr/bin/python

import argparse
import cv2
import sys
import os
## use import pickle in Py3
import cPickle as pickle
from matplotlib import pyplot as plt
from os.path import basename

from hist_image_index import hist_index_img

################################
# module: hist_image_index.py
# Ryan Mecham
# A01839282
################################


def compute_hist_sim(inhist_vec, hist_index, hist_sim, topn=3):

    img_sims = [] #then just sort and return img_sims[:topn]

    for fp, hist in hist_index.items():
        if hist_sim == 'correl':
            sim = cv2.compareHist(inhist_vec, hist, cv2.HISTCMP_CORREL)
        elif hist_sim == 'chisqr':
            sim = cv2.compareHist(inhist_vec, hist, cv2.HISTCMP_CHISQR)
        elif hist_sim == 'bhatta':
            sim = cv2.compareHist(inhist_vec, hist, cv2.HISTCMP_BHATTACHARYYA)
        elif hist_sim == 'inter':
            sim = cv2.compareHist(inhist_vec, hist, cv2.HISTCMP_INTERSECT)
            # sim = cv2.compareHist(hist, base_img_hist, cv2.HISTCMP_INTERSECT)
        else:
            raise Exception('invalid hist_sim', hist_sim)
        img_sims.append((fp,sim))

    if hist_sim == 'correl':
        img_sims = sorted(img_sims, key=lambda x: x[1], reverse=True)#default sort is ascending, higher is more similar
    elif hist_sim == 'chisqr':
        img_sims = sorted(img_sims, key=lambda x: x[1])#default sort is ascending, lower is more similar
    elif hist_sim == 'bhatta':
        img_sims = sorted(img_sims, key=lambda x: x[1])#default sort is ascending, lower is more similar 
    elif hist_sim == 'inter':
        img_sims = sorted(img_sims, key=lambda x: x[1], reverse=True)#default sort is ascending, higher is more similar
    else:
            raise Exception('invalid hist_sim', hist_sim)
    return img_sims[:topn] #closest topn images
    

def show_images(input_image, match_list):
    plt.figure(0)
    plt.title('Input Image') 
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    # plt.show()
    # print match_list
    for i, item in enumerate(match_list):
        fp, sim = item
        img = cv2.imread(fp)
        plt.figure(i+1)
        plt.title('Matched image ' + str(i+1) + ': ' + fp + '; Sim = ' + str(sim)) 
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

'''
imgpath: path to image to compare against
bin_size: 8 or 16 (the one used for hist_index)
hist_index: historgram dictionary (created in hist_image_index.py)
hist_sim: histogram similarity metric can be one of: ('correl', 'chisqr', 'inter', 'bhatta') for (correlation, chi square, intersection, bhattacharrya) respectively
'''
def find_sim_rgb_images(imgpath, bin_size, hist_index, hist_sim):

    base_img_hist = hist_index_img(imgpath, 'rgb', bin_size)

    return compute_hist_sim(base_img_hist, hist_index, hist_sim, 3)
    

def find_sim_hsv_images(imgpath, bin_size, hist_index, hist_sim):
    
    base_img_hist = hist_index_img(imgpath, 'hsv', bin_size)

    return compute_hist_sim(base_img_hist, hist_index, hist_sim, 3)


def load_hist_index(pick_path):
    with open(pick_path, 'rb') as histfile:
        return pickle.load(histfile)

## change the paths as you see fit and add calls to show_images()
## after you implement it.


## ============= Image Retrieval Tests ===========================

## change these as you see fit.
## IMGDIR is the directory for test images
## PICDIR is the directory where the pickle files are stored.
IMGDIR = './hist-test/'
PICDIR = './pickles/'

'''
My Py shell output:
images/123461762.JPG --> 2.69072864504
images/123465049.JPG --> 2.63319342056
images/123472255.JPG --> 2.43531483644
'''
def test_01():
    hist_index = load_hist_index(PICDIR + 'rgb_hist8.pck')
    print PICDIR
    print len(hist_index)
    assert len(hist_index) == 318
    imgpath = IMGDIR + 'food_test/img01.JPG'
    inimg = cv2.imread(imgpath)
    top_matches = find_sim_rgb_images(imgpath,8, hist_index, 'inter')
    for imagepath, sim in top_matches:
        print(imagepath + ' --> ' + str(sim))
    show_images(inimg, top_matches)
    del hist_index

'''
My Py shell output:
>>> test_02()
images/123472992.JPG --> 1.04123155377
images/123465793.JPG --> 0.778828541127
images/123465726.JPG --> 0.775194820913
'''
def test_02():
    hist_index = load_hist_index(PICDIR + 'hsv_hist8.pck')
    assert len(hist_index) == 318
    imgpath = IMGDIR + 'food_test/img03.JPG'
    inimg = cv2.imread(imgpath)
    top_matches = find_sim_hsv_images(imgpath,
		                                        8, hist_index, 'inter')
    for imagepath, sim in top_matches:
        print(imagepath + ' --> ' + str(sim))
    show_images(inimg, top_matches)
    del hist_index

'''
My Py shell output:
images/123465245.JPG --> 15.8357133494
images/17_02_21_22_17_56_orig.png --> 21.0158345761
images/17_02_21_22_17_55_orig.png --> 21.401725557
'''
def test_03():
    hist_index = load_hist_index(PICDIR + 'rgb_hist8.pck')
    assert len(hist_index) == 318
    imgpath = IMGDIR + 'food_test/img04.JPG'
    inimg = cv2.imread(imgpath)
    top_matches = find_sim_rgb_images(imgpath,
		                                        8, hist_index, 'chisqr')
    for imagepath, sim in top_matches:
        print(imagepath + ' --> ' + str(sim))
    show_images(inimg, top_matches)
    del hist_index

'''
My Py shell output:
images/17_02_21_22_14_24_orig.png --> 0.0952925097908
images/17_02_21_22_14_14_orig.png --> 0.190314746298
images/17_02_21_22_20_56_orig.png --> 0.282203709903
'''
def test_04():
    hist_index = load_hist_index(PICDIR + 'rgb_hist16.pck')
    assert len(hist_index) == 318
    imgpath = IMGDIR + 'car_test/img22.png'
    inimg = cv2.imread(imgpath)
    top_matches = find_sim_rgb_images(imgpath,
		                                        16, hist_index, 'bhatta')
    for imagepath, sim in top_matches:
        print(imagepath + ' --> ' + str(sim))
    show_images(inimg, top_matches)
    del hist_index

'''
My Py shell output:
images/123472992.JPG --> 0.948968044156
images/123459060.JPG --> 0.957500781094
images/123465726.JPG --> 0.957573532491

Matching car_test/img023.png in HSV space on bhatta doesn't produce
good results.
''' 
def test_05():
    hist_index = load_hist_index(PICDIR + 'hsv_hist16.pck')
    assert len(hist_index) == 318
    imgpath = IMGDIR + 'car_test/img02.png'
    inimg = cv2.imread(imgpath)
    top_matches = find_sim_hsv_images(imgpath,
		                                        16, hist_index, 'bhatta')
    for imagepath, sim in top_matches:
        print(imagepath + ' --> ' + str(sim))
    show_images(inimg, top_matches)
    del hist_index

'''
My Py shell output:
images/16_07_02_14_21_01_orig.png --> 0.0601641627891
images/16_07_02_14_21_06_orig.png --> 0.0626254148808
images/16_07_02_14_21_02_orig.png --> 0.0641319684534

Matching car_test/img023.png in RGB space on bhatta produces
excellent matches.
'''
def test_06():
    hist_index = load_hist_index(PICDIR + 'rgb_hist16.pck')
    assert len(hist_index) == 318
    imgpath = IMGDIR + 'car_test/img02.png'
    inimg = cv2.imread(imgpath)
    top_matches = find_sim_rgb_images(imgpath,
		                                        16, hist_index, 'bhatta')
    for imagepath, sim in top_matches:
        print(imagepath + ' --> ' + str(sim))
    show_images(inimg, top_matches)
    del hist_index


    
 
if __name__ == '__main__':
    pass
    test_01()
    test_02()
    test_03()
    test_04()