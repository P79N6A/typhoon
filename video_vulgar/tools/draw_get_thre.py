import matplotlib.pyplot as plt
import csv


file_dir = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/jinshen_nopad.csv'
file = csv.reader(open(file_dir, 'r'))

x = []
y = []

for line in file:
    x.append(float(line[1]))
    y.append(float(line[2]))



fig, ax_label = plt.subplots()

ax_label.scatter(x, y, c='r')

for i, txt in enumerate(x):
    ax_label.annotate(' ', (x[i], y[i]))
plt.show()