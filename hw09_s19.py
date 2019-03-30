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
    graph.graphFromTable(xvals,data,labels,name='Bee traffic for '+csv_fp, xlabel='t (seconds)', ylabel='moving bees')

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
    '''
    gap is measured as abs(upward_est - downward_est)
    return: 5-tuple as follows:
    0 - path to csv with smallest gap
    1 - upward est
    2 - downward est
    3 - lateral est
    4 - gap
    '''
    smallest_gap = None
    smallest_gap_fp = None
    smallest_gap_up_est = None
    smallest_gap_down_est = None
    smallest_gap_lat_est = None
    fnames = generate_file_names('.csv',csv_dir)
    for fp in fnames:
        fd = read_csv_file(fp)
        up_est,down_est,lat_est = bee_traffic_stats(fd)
        gap = abs(up_est - down_est)
        if smallest_gap == None:
            smallest_gap = gap
            smallest_gap_fp = fp

            smallest_gap_up_est = up_est
            smallest_gap_down_est = down_est
            smallest_gap_lat_est = lat_est
        elif gap < smallest_gap:
            smallest_gap = gap
            smallest_gap_fp = fp

            smallest_gap_up_est = up_est
            smallest_gap_down_est = down_est
            smallest_gap_lat_est = lat_est
    return (smallest_gap_fp, smallest_gap_up_est, smallest_gap_down_est, smallest_gap_lat_est, smallest_gap)
    

def find_largest_up_down_gap_file(csv_dir):#my dev csv_dir is './bee_traffic_estimates'
    '''
    gap is measured as abs(upward_est - downward_est)
    return: 5-tuple as follows:
    0 - path to csv with largest gap
    1 - upward est
    2 - downward est
    3 - lateral est
    4 - gap
    '''
    largest_gap = None
    largest_gap_fp = None
    largest_gap_up_est = None
    largest_gap_down_est = None
    largest_gap_lat_est = None
    fnames = generate_file_names('.csv',csv_dir)
    for fp in fnames:
        fd = read_csv_file(fp)
        up_est,down_est,lat_est = bee_traffic_stats(fd)
        gap = abs(up_est - down_est)
        if largest_gap == None:
            largest_gap = gap
            largest_gap_fp = fp

            largest_gap_up_est = up_est
            largest_gap_down_est = down_est
            largest_gap_lat_est = lat_est
        elif gap > largest_gap:
            largest_gap = gap
            largest_gap_fp = fp

            largest_gap_up_est = up_est
            largest_gap_down_est = down_est
            largest_gap_lat_est = lat_est
    return (largest_gap_fp, largest_gap_up_est, largest_gap_down_est, largest_gap_lat_est, largest_gap)

############################

def find_max_up_file(csv_dir):
    '''
    return: 4-tuple as follows:
    0 - path to csv with max up
    1 - upward est
    2 - downward est
    3 - lateral est
    '''
    max_up = None
    max_up_fp = None
    max_up_up_est = None
    max_up_down_est = None
    max_up_lat_est = None
    fnames = generate_file_names('.csv',csv_dir)
    for fp in fnames:
        fd = read_csv_file(fp)
        up_est,down_est,lat_est = bee_traffic_stats(fd)
        if max_up == None:
            max_up = up_est
            max_up_fp = fp

            max_up_up_est = up_est
            max_up_down_est = down_est
            max_up_lat_est = lat_est
        elif up_est > max_up:
            max_up = up_est
            max_up_fp = fp

            max_up_up_est = up_est
            max_up_down_est = down_est
            max_up_lat_est = lat_est
    return (max_up_fp, max_up_up_est, max_up_down_est, max_up_lat_est)

def find_min_up_file(csv_dir):
    min_up = None
    min_up_fp = None
    min_up_up_est = None
    min_up_down_est = None
    min_up_lat_est = None
    fnames = generate_file_names('.csv',csv_dir)
    for fp in fnames:
        fd = read_csv_file(fp)
        up_est,down_est,lat_est = bee_traffic_stats(fd)
        if min_up == None:
            min_up = up_est
            min_up_fp = fp

            min_up_up_est = up_est
            min_up_down_est = down_est
            min_up_lat_est = lat_est
        elif up_est < min_up:
            min_up = up_est
            min_up_fp = fp

            min_up_up_est = up_est
            min_up_down_est = down_est
            min_up_lat_est = lat_est
    return (min_up_fp, min_up_up_est, min_up_down_est, min_up_lat_est)

###########################

def find_max_down_file(csv_dir):
    max_down = None
    max_down_fp = None
    max_down_up_est = None
    max_down_down_est = None
    max_down_lat_est = None
    fnames = generate_file_names('.csv',csv_dir)
    for fp in fnames:
        fd = read_csv_file(fp)
        up_est,down_est,lat_est = bee_traffic_stats(fd)
        if max_down == None:
            max_down = down_est
            max_down_fp = fp

            max_down_up_est = up_est
            max_down_down_est = down_est
            max_down_lat_est = lat_est
        elif down_est > max_down:
            max_down = down_est
            max_down_fp = fp

            max_down_up_est = up_est
            max_down_down_est = down_est
            max_down_lat_est = lat_est
    return (max_down_fp, max_down_up_est, max_down_down_est, max_down_lat_est)

def find_min_down_file(csv_dir):
    min_down = None
    min_down_fp = None
    min_down_up_est = None
    min_down_down_est = None
    min_down_lat_est = None
    fnames = generate_file_names('.csv',csv_dir)
    for fp in fnames:
        fd = read_csv_file(fp)
        up_est,down_est,lat_est = bee_traffic_stats(fd)
        if min_down == None:
            min_down = down_est
            min_down_fp = fp

            min_down_up_est = up_est
            min_down_down_est = down_est
            min_down_lat_est = lat_est
        elif down_est < min_down:
            min_down = down_est
            min_down_fp = fp

            min_down_up_est = up_est
            min_down_down_est = down_est
            min_down_lat_est = lat_est
    return (min_down_fp, min_down_up_est, min_down_down_est, min_down_lat_est)

############################

def find_max_lat_file(csv_dir):
    max_lat = None
    max_lat_fp = None
    max_lat_up_est = None
    max_lat_down_est = None
    max_lat_lat_est = None
    fnames = generate_file_names('.csv',csv_dir)
    for fp in fnames:
        fd = read_csv_file(fp)
        up_est,down_est,lat_est = bee_traffic_stats(fd)
        if max_lat == None:
            max_lat = lat_est
            max_lat_fp = fp

            max_lat_up_est = up_est
            max_lat_down_est = down_est
            max_lat_lat_est = lat_est
        elif lat_est > max_lat:
            max_lat = lat_est
            max_lat_fp = fp

            max_lat_up_est = up_est
            max_lat_down_est = down_est
            max_lat_lat_est = lat_est
    return (max_lat_fp, max_lat_up_est, max_lat_down_est, max_lat_lat_est)

def find_min_lat_file(csv_dir):
    min_lat = None
    min_lat_fp = None
    min_lat_up_est = None
    min_lat_down_est = None
    min_lat_lat_est = None
    fnames = generate_file_names('.csv',csv_dir)
    for fp in fnames:
        fd = read_csv_file(fp)
        up_est,down_est,lat_est = bee_traffic_stats(fd)
        if min_lat == None:
            min_lat = lat_est
            min_lat_fp = fp

            min_lat_up_est = up_est
            min_lat_down_est = down_est
            min_lat_lat_est = lat_est
        elif lat_est < min_lat:
            min_lat = lat_est
            min_lat_fp = fp

            min_lat_up_est = up_est
            min_lat_down_est = down_est
            min_lat_lat_est = lat_est
    return (min_lat_fp, min_lat_up_est, min_lat_down_est, min_lat_lat_est)


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
    csv_dir = './bee_traffic_estimates'
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
    print('-------------')

    find_smallest_up_down_gap_file('./bee_traffic_estimates')
    print('-------------')

    fp, u, d, l, gap = find_smallest_up_down_gap_file('./bee_traffic_estimates')
    print(fp, u, d, l, gap)
    plot_bee_traffic(fp)
    print('-------------')

    fp, u, d, l, gap = find_largest_up_down_gap_file('./bee_traffic_estimates')
    print(fp, u, d, l, gap)
    plot_bee_traffic(fp)
    print('-------------')

    fp, u, d, l = find_max_up_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)

    fp, u, d, l = find_min_up_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)

    fp, u, d, l = find_max_down_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)

    fp, u, d, l = find_min_down_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)

    fp, u, d, l = find_max_lat_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)

    fp, u, d, l = find_min_lat_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)