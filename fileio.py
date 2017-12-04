file = open('input.txt', 'w')
total = 0.0
count = 0
for line in file:
    line = file.readline()
    if not line:
        break
    total += float(line)
    count += 1
file.close()
file = open('output.txt', 'w')
file.write('%f\n' % (total/count))
file.close()