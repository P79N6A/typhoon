import sys
try: 
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break 
        lines = line.split()
        li1 = set(list(lines[0]))
        li2 = set(list(lines[1]))
        if li1==li2:
            print("true")
        else:
            print("false")
except: 
    pass