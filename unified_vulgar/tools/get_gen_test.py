import csv
import os


if __name__ == "__main__":
    input_pos = ['huoshan_pos', 'xigua_pos', 'M_pos', 'T_pos', 'danciyuan_pos']
    input_random = ['huoshan_fu', 'xigua_fu', 'M_fu', 'T_fu', 'danciyuan_fu']

    dir = '/mnt/cephfs/lab/wangxiyu/data/gen/'

    test_lis = []

    for files_name in input_pos:
        file_dir = os.path.join(dir, files_name)
        for name in os.listdir(file_dir):
            file = os.path.join(file_dir, name)
            id = name.split('.')[0]
            test_lis.append([id, files_name, 1, file])

    for files_name in input_random:
        file_dir = os.path.join(dir, files_name)
        for name in os.listdir(file_dir):
            file = os.path.join(file_dir, name)
            id = name.split('.')[0]
            test_lis.append([id, files_name, 0, file])

    print len(test_lis)

    output_test = os.path.join(dir, 'gen_test.csv')

    write_test = csv.writer(open(output_test, 'w'))

    for line in test_lis:
        write_test.writerow(line)