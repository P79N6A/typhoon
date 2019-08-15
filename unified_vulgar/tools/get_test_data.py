import csv
import os

if __name__ == "__main__":

    biaoqian = {'huoshan_pos': 0,
                'xigua_pos': 0,
                'm_pos': 0,
                't_pos': 0}

    dir = '/Users/ounozomiyo/Desktop/company/data/unified_vulgar/test/pos_biaoqian.csv'

    pos_file = csv.reader(open(dir, 'r'))

    for line in pos_file:
        print line
