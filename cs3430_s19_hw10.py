#!/usr/bin/python

import math
from PIL import Image
import numpy as np

#######################################################
# module: cs3430_s19_hw10.py
# Ryan Mecham
# A01839282
########################################################

##################### Problem 1 (4 points) ####################

## a function to convert an rgb 3-tuple to a grayscale value.
def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

def save_gd_edges(input_fp, output_fp, magn_thresh=20):
    input_image  = Image.open(input_fp)
    output_image = gd_detect_edges(input_image, magn_thresh=magn_thresh)
    output_image.save(output_fp)
    del input_image
    del output_image

def gd_detect_edges(rgb_img, magn_thresh=20):
    ## your code here
    width, height = rgb_img.size
    edge_img = Image.new('L',(width,height))
    # edge_img_px = rgb_img.load()
    edge_img_px = edge_img.load()
    #loop through all pixels to get gradient (start at (1,1) and go to (n-1,n-1) so the 3x3 kernel doesn't go off edge of image)
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            is_edge_pixel = False
            #figure out if is edge pixel by computing gradient for kernel

            if is_edge_pixel or i > 10 and i < 20:
                edge_img_px[i, j] = (255)
            else:
                edge_img_px[i, j] = (0)
    print(edge_img_px)
    return edge_img


###################### Problem 2 (1 point) #####################

def cosine_sim(img1, img2):
    assert img1.size == img2.size
    ## your code here
    pass

'''
>>> test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_09_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_09_ed.png')
1.0
>>> test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
0.512202985103
>>> test_cosine_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
0.352152693884
>>> test_cosine_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
0.352152693884
'''
def test_cosine_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = cosine_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def euclid_sim(img1, img2):
    assert img1.size == img2.size
    ## your code here
    pass

'''
>>> test_euclid_sim('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
0.0
>>> test_euclid_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
16981.9278941
>>> test_euclid_sim('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
16981.9278941
'''
def test_euclid_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = euclid_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def jaccard_sim(img1, img2):
    assert img1.size == img2.size
    ## your code here
    pass

'''
>>> test_jaccard_sim('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
1.0
>>> test_jaccard_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
1.0
>>> test_jaccard_sim('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
1.0
>>> test_jaccard_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
0.934065934066
>>> test_jaccard_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
0.934065934066
'''
def test_jaccard_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = jaccard_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def test_01():
    save_gd_edges('img/1b_bee_01.png', 'img/1b_bee_01_ed.png', magn_thresh=20)
    save_gd_edges('img/1b_bee_10.png', 'img/1b_bee_10_ed.png', magn_thresh=20)
    save_gd_edges('img/2b_nb_10.png', 'img/2b_nb_10_ed.png', magn_thresh=20)
    save_gd_edges('img/2b_nb_21.png', 'img/2b_nb_21_ed.png', magn_thresh=20)
    save_gd_edges('img/elephant.jpg', 'img/elephant_ed.jpg', magn_thresh=20)
    save_gd_edges('img/output11885.jpg', 'img/output11885_ed.jpg', magn_thresh=20)
    save_gd_edges('img/2b_nb_09.png', 'img/2b_nb_09_ed.png', magn_thresh=20)
    save_gd_edges('img/output11884.jpg', 'img/output11884_ed.jpg', magn_thresh=20)

## testing the PIL/PILLOW installation
def test_02():
    img = Image.open('img/1b_bee_01.png').convert('LA')
    img2 = img.save('img/1b_bee_01_gray.png')
    del img
    del img2
    
if __name__ == '__main__':
    img = Image.open('img/1b_bee_01.png')
    print(img.getpixel((15,10)))
    print(img.size)
    px = img.load()
    print(px[15,10])

    edge_img = gd_detect_edges(img)
    edge_img.show()

