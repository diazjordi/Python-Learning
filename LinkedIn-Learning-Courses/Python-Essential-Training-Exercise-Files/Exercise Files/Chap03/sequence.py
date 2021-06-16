#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ] #list
for i in x:
    print('i is {}'.format(i))

x = ( 1, 2, 3, 4, 5 ) #tuple
for i in x:
    print('i is {}'.format(i))

x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 } #dictionary
for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))