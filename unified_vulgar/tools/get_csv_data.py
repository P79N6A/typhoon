import multiprocessing as mp

dir = '/Users/ounozomiyo/Desktop/vulgar/xigua+general.txt'
general_dir = '/Users/ounozomiyo/Desktop/vulgar/general.txt'

dir1 = '/Users/ounozomiyo/Desktop/vulgar/xigua.txt'

result = open(dir1, "w")

ids = []

with open(general_dir) as f:
    for line in f.readlines():
        ids.append(line.split('\t')[0])

def process(line):
    id = line.split('\t')[0]
    if id not in ids:
        result.write(line)

if __name__ == "__main__":
    lines = []

    with open(dir) as f:
        for line in f.readlines():
            lines.append(line)

    p = mp.Pool(10)
    p.map(process, lines)
    p.close()
    p.join()