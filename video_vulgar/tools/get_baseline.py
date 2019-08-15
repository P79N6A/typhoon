import csv
import os

if __name__ == "__main__":
    dir1 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/huangchao_random.csv'

    dir2 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/url_score_random.csv'

    read1 = csv.reader(open(dir1, 'r'))
    read2 = csv.reader(open(dir2, 'r'))

    dir4 = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/url_score_random_baseline.csv'
    write_jinshen_pre = csv.writer(open(dir4, 'w'))

    score = {}
    for line in read1:
        id = line[0].split('/')[-1]
        score[id] = float(line[1])

    print len(score.keys())

    for line in read2:
        if line[0] in score.keys():
            print score[line[0]]
            write_jinshen_pre.writerow([line[0], line[1], score[line[0]], line[3]])
        else:
            print line[0]
