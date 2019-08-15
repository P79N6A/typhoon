#encoding: utf-8
import csv

csv_dir = '/Users/ounozomiyo/Desktop/公司/data/fk_img_lab/test_output_random.csv'
write_dir = '/Users/ounozomiyo/Desktop/公司/data/fk_img_lab/test_face_random.csv'
csv_file = csv.reader(open(csv_dir, "r"))

write = csv.writer(open(write_dir, 'w'))

for line in csv_file:
    if line[2] == '0':
        write.writerow(['https://p0.pstatp.com/origin/' + line[0]])

print "suss!!!"