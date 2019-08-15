import csv
import os


if __name__ == "__main__":
    input_pos = ['huoshan_pos', 'xigua_pos', 'm_pos', 't_pos']
    input_random = ['huoshan_random', 'xigua_random', 'm_random', 't_random']

    dir = '/mnt/cephfs/lab/wangxiyu/data/gen/'

    url_pos = []
    url_random = []

    for file in input_pos:
        file_dir = os.path.join(dir, file+'/result.txt')
        with open(file_dir) as f:
            for i, l in enumerate(f.readlines()):
                if i < 200:
                    url = l.split('\t')[1]
                    vid = l.split('\t')[0]
                    url_pos.append([url, vid, file])
                else:
                    break
    print len(url_pos)

    for file in input_random:
        file_dir = os.path.join(dir, file + '/result.txt')
        with open(file_dir) as f:
            for i, l in enumerate(f.readlines()):
                if i < 2000:
                    url = l.split('\t')[1]
                    vid = l.split('\t')[0]
                    url_random.append([url, vid, file])
                else:
                    break

    print len(url_random)

    out_put_dir = os.path.join(dir, 'general')

    output_pos = os.path.join(out_put_dir, 'pos.csv')
    output_random = os.path.join(out_put_dir, 'random.csv')

    write_pos = csv.writer(open(output_pos, 'w'))
    write_random = csv.writer(open(output_random, 'w'))

    for url, vid, file in url_pos:
        write_pos.writerow([url, vid, file])

    for url, vid, file in url_random:
        write_random.writerow([url, vid, file])