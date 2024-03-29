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
            #dy = I(c,r-1) - I(c,r+1)
            #dx = I(c+1,r) - I(c-1,r)
            #||G|| = sqrt(dy^2 + dx^2) is gradient's magnitude at I(c,r)
            #theta = arctan(dy/dx) is the gradients orientation

            #up get up pixel and compute luminosity
            px_up = rgb_img.getpixel((i,j-1))
            gs_px_up = luminosity(px_up)

            #right
            px_right = rgb_img.getpixel((i+1,j))
            gs_px_right = luminosity(px_right)

            #down
            px_down = rgb_img.getpixel((i,j+1))
            gs_px_down = luminosity(px_down)

            #left
            px_left = rgb_img.getpixel((i-1,j))
            gs_px_left = luminosity(px_left)

            #compute gradient
            dy = gs_px_up - gs_px_down
            dx = gs_px_right - gs_px_left
            gradient = math.sqrt(dy ** 2 + dx ** 2)

            if gradient >= magn_thresh:
                is_edge_pixel = True

            if is_edge_pixel:
                edge_img_px[i, j] = (255)
            else:
                edge_img_px[i, j] = (0)
    return edge_img


###################### Problem 2 (1 point) #####################

def cosine_sim(img1, img2):
    assert img1.size == img2.size

    numerator = 0
    denom_left = 0
    denom_right = 0
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            numerator += img1.getpixel((i,j)) * img2.getpixel((i,j))
            denom_left += img1.getpixel((i,j)) ** 2
            denom_right += img2.getpixel((i,j)) ** 2

    # for i in range(img1.size[0]):
        # for j in range(img1.size[1]):

    s_denom_left = math.sqrt(denom_left)
    s_denom_right = math.sqrt(denom_right)

    c_sim = numerator / (s_denom_left * s_denom_right)

    return c_sim

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

    s = 0
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            s += (img1.getpixel((i,j)) - img2.getpixel((i,j))) ** 2

    e_sum = math.sqrt(s)

    return e_sum

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

    s1 = set(np.array(img1).flatten().tolist())
    s2 = set(np.array(img2).flatten().tolist())

    j_sim = float(len(set.intersection(s1,s2))) / len(set.union(s1,s2))

    return j_sim

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
    # img = Image.open('img/output11885.jpg')
    # print(img.getpixel((15,10)))
    # print(img.size)
    # px = img.load()
    # print(px[15,10])

    # edge_img = gd_detect_edges(img)
    # edge_img.show()

    test_cosine_sim('img/1b_bee_01_ed.png', 'img/1b_bee_01_ed.png')
    # test_cosine_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
    test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
    print('-----------')

    test_euclid_sim('img/1b_bee_01_ed.png', 'img/1b_bee_01_ed.png')
    test_euclid_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
    print('-----------')

    test_jaccard_sim('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
    test_jaccard_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
    test_jaccard_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')