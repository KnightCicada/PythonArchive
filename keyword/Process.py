readPath = 'onions.txt'
writePath = 'add.txt'
lines_seen = set()
outFile = open(writePath, 'a+', encoding='utf-8')
f = open(readPath, 'r', encoding='utf-8')
for line in f:
    if line not in lines_seen:
        outFile.write(line)
        lines_seen.add(line)
