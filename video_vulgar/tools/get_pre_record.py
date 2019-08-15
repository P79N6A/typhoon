import csv
import os


def get_pre(thres, image_pos, image_sroce):

    pos_num = 0
    fu_num = 0
    for image in image_sroce.keys():
        if image_sroce[image] >= thres:
            if image in image_pos:
                pos_num += 1
            else:
                fu_num += 1

    return pos_num*1.0/(pos_num + fu_num)

if __name__ == "__main__":
    dir1 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/vular_jinshen.csv'
    dir2 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/biaozhu_result.csv'
    dir3 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/random.csv'

    dir4 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/jinshen_per_recall.csv'

    read1 = csv.reader(open(dir1, 'r'))
    read2 = csv.reader(open(dir2, 'r'))
    read3 = csv.reader(open(dir3, 'r'))

    write_jinshen_pre = csv.writer(open(dir4, 'w'))

    image_pos = []

    image_sroce = {}

    for read in read2:
        print read[0].split('.')[0]
        image_pos.append(read[0].split('.')[0])

    for read in read3:
        image_sroce[read[0]] = float(read[1])

    for line in read1:
        thres = float(line[0])
        pre = get_pre(thres, image_pos, image_sroce)
        write_jinshen_pre.writerow([line[0], line[1], line[2], pre])