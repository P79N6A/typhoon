import csv
import os
import random

def read_list(path_in):
    with open(path_in) as fin:
        items = []
        while True:
            line = fin.readline()
            if not line:
                break
            line = [i.strip() for i in line.strip().split('\t')]
            line_len = len(line)
            # check the data format of .lst file
            if line_len < 3:
                print('lst should have at least has three parts, but only has %s parts for %s' % (line_len, line))
                continue
            items.append([line[2], line[1]])
        return items

def make_list(lis, file_dir):
    with open(file_dir, 'w') as fout:
        for i, item in enumerate(lis):
            line = str(i) + '\t' + item[0] + '\t' + item[1] + '\n'
            fout.write(line)

if __name__ == "__main__":
    root_dir = '/mnt/cephfs_wj/vc/wangxiyu/data/unified_vulgar/'
    train_read = csv.reader(open(os.path.join(root_dir, 'train.csv'), 'r'))

    dice = {}
    dice['mtvhuoshan'] = []
    dice['xigua'] = []
    dice['banciyuan'] = []
    dice['tongyong'] = []
    dice['general'] = []

    for line in train_read:
        dir = line[0]
        dir_name = dir.split('/')[-1]

        if dir_name in ['83b27ca6-7f0e-412d-8189-f794238151fd',
                        '0d8c024c-a08d-4e31-b6e1-cc701ff9625b',
                        '580aa6d7-d19a-4176-9784-632a35a29574',
                        'b004490e-1008-4a3f-8eb8-bbd04956bdc6',
                        '1558240e-c77c-4920-b7c6-1b0d15c4c35c']:
            lis_id = 'mtvhuoshan'
        elif dir_name in ['3de2c856-6174-420e-b704-180e9361bb55']:
            lis_id = 'xigua'
        elif dir_name in ['c72c0000-a717-445b-850e-651afa60d2dc']:
            lis_id = 'banciyuan'
        elif dir_name in ['7e1ba7df-6061-4a97-94f7-0c1ea6a09611']:
            lis_id = 'tongyong'

        for file_name in os.listdir(dir):
            if file_name.endswith('.lst'):
                dice['general'] += read_list(os.path.join(dir, file_name))

    random.shuffle(dice['general'])

    for id, value in dice.items():
        if id == 'general':
            file_dir = os.path.join(root_dir, id + '.lst')
            make_list(value, file_dir)
            print id, len(value)
