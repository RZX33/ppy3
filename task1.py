line = input('Input numbers').split(',')
max = int(line[0])
min = int(line[0])
for i in range(0, len(line)):
    if int(line[i]) > max:
        max=int(line[i])
    if int(line[i]) < min:
        min=int(line[i])
print(min,' ', max)