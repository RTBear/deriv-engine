#!/usr/bin/python

####################################
# module: hw09_s19.py
# Ryan Mecham
# A01839282
####################################

import numpy as np
import os
import csv
import graph
import scipy.integrate


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

def display_csv_file(csv_file_path):
    fd = {}
    with open(csv_file_path, 'r') as instream:
        reader = csv.reader(instream, delimiter = ",")
        for row in reader:
            print(row)

def read_csv_file(csv_file_path):
    fd = {}
    with open(csv_file_path, 'r') as instream:
        reader = csv.reader(instream, delimiter = ",")
        reader.next() #to skip the header
        for row in reader:
            secs, up, down, lat = int(row[0]), float(row[1]), \
                                     float(row[2]), float(row[3])
            fd[secs] = (up, down, lat)
        return fd

def plot_bee_traffic(csv_fp):
    fd = read_csv_file(csv_fp)#fd for file dictionary
    labels = ['upward','downward','lateral']
    xvals = [x for x in fd]
    up = [fd[i][0] for i in fd]
    down = [fd[i][1] for i in fd]
    lateral = [fd[i][2] for i in fd]
    data = [up,down,lateral]
    graph.graphFromTable(xvals,data,labels,name='Bee traffic for '+csv_fp)

def sr_approx(f, a, b, n):#alias for simpson_approx
    return simpson_approx(f, a, b, n)

def sp_approx(f, a, b, n):#alias for simpson_approx
    return simpson_approx(f, a, b, n)

def simpson_approx(f, a, b, n):
    dx = (b - a) / float(n)
    # print('dx',dx)
    subdivisions = np.linspace(a,b,n+1)
    # print('--dx',subdivisions[1] - subdivisions[0])
    # print(subdivisions, len(subdivisions))

    inner_sum = 0

    for i,x in enumerate(subdivisions):
        if i == 0 or i == n:#start or end
            mult = 1
        else:
            if i%2 == 0:#even x
                mult = 2
            else:
                mult = 4
        inner_sum += mult*f(x)
    approx = (dx/3.0) * inner_sum
    return approx

def bee_traffic_estimate(t, md='u', fd={}):
    assert md == 'u' or md == 'd' or md == 'l'
    vals = fd.get(int(t))
    if vals is None:
        return None
    elif md == 'u':
        return vals[0]
    elif md == 'd':
        return vals[1]
    elif md == 'l':
        return vals[2]

def make_bee_traffic_estimator(fd, md):
    assert md == 'u' or md == 'd' or md == 'l'
    return lambda t: bee_traffic_estimate(t, md=md, fd=fd)

def bee_traffic_stats(fd):
    up_bte = make_bee_traffic_estimator(fd, 'u')
    down_bte = make_bee_traffic_estimator(fd, 'd')
    lat_bte = make_bee_traffic_estimator(fd, 'l')
    return(sr_approx(up_bte, 5, 28, 23),sr_approx(down_bte, 5, 28, 23),sr_approx(lat_bte, 5, 28, 23))

def find_smallest_up_down_gap_file(csv_dir):
    ## your code here
    pass

def find_largest_up_down_gap_file(csv_dir):
    ## your code here
    pass

############################

def find_max_up_file(csv_dir):
    ## your code here
    pass

def find_min_up_file(csv_dir):
    ## your code here
    pass

###########################

def find_max_down_file(csv_dir):
    ## your code here
    pass

def find_min_down_file(csv_dir):
    ## your code here
    pass

############################

def find_max_lat_file(csv_dir):
    ## your code here
    pass

def find_min_lat_file(csv_dir):
    ## your code here
    pass


def testFunc(csv_fp):
    FD = read_csv_file(csv_fp)
    up_bte = make_bee_traffic_estimator(FD, 'u')
    down_bte = make_bee_traffic_estimator(FD, 'd')
    lat_bte = make_bee_traffic_estimator(FD, 'l')
    print(sr_approx(up_bte, 5, 28, 23))
    print(sr_approx(down_bte, 5, 28, 23))
    print(sr_approx(lat_bte, 5, 28, 23))

if __name__ == '__main__':
    csv_fp = './bee_traffic_estimates/192_168_4_5-2018-07-01_08-00-10.csv'
    # plot_bee_traffic(csv_fp)
    test = sr_approx(lambda x: x**2, 0, 2, 10)
    print(test)
    test = sr_approx(lambda x: x**3, 1, 5, 100)
    print(test)

    # x = np.linspace(1, 5, 100) #verify simpson approximation
    # y = np.array([i**3 for i in x])
    # print(scipy.integrate.simps(y, x))
    print('-------------')
    testFunc('./bee_traffic_estimates/192_168_4_5-2018-07-01_08-00-10.csv')
    print('-------------')
    testFunc('./bee_traffic_estimates/192_168_4_5-2018-07-01_08-30-10.csv')
    print('-------------')
    testFunc('./bee_traffic_estimates/192_168_4_5-2018-07-01_16-30-10.csv')
    print('-------------')

    fd = read_csv_file('./bee_traffic_estimates/192_168_4_5-2018-07-02_16-30-10.csv')
    print(bee_traffic_stats(fd))
    print('-------------')

    fd = read_csv_file('./bee_traffic_estimates/192_168_4_5-2018-07-01_14-00-10.csv')
    print(bee_traffic_stats(fd))
    print('-------------')

    fd = read_csv_file('./bee_traffic_estimates/192_168_4_5-2018-07-01_18-00-10.csv')
    print(bee_traffic_stats(fd))
