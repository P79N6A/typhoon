import matplotlib.pyplot as plt
import csv


file_dir = '/Users/ounozomiyo/Desktop/company/data/video_vulgar/test/url_score_pos.csv'
file = csv.reader(open(file_dir, 'r'))

scores = []

for line in file:
    #if int(line[3]) == 1:
    scores.append(float(line[2]))

x = []
y = []

for score in range(100):
    x.append(sum([1 for s in scores if s > score*0.01]))
    y.append(score*0.01)

fig, ax_label = plt.subplots()

ax_label.scatter(x, y, c='r')

for i, txt in enumerate(x):
    ax_label.annotate(' ', (x[i], y[i]))
plt.show()