import sys
ss = []
try:
	while True:
		line = sys.stdin.readline().strip()
		if line == '':break
		lines = line.split(" ")
		for a in lines:ss.append(a)
except: 
    pass
print(len(set(ss)))