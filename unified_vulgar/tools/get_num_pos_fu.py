#encoding: utf-8
import csv

dir = '/Users/ounozomiyo/Desktop/company/data/unified_vulgar/test/down/火山低俗-训练集-0803.txt'

pos_num = 0
fu_num = 0

with open(dir) as f:
    for line in f.readlines():
        if line.split('\t')[1] == '1':
            pos_num += 1
        else:
            fu_num += 1
print pos_num, fu_num