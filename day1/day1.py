def readInput(f):
    input = open(f,'r')
    i = input.read().split()
    input.close()
    return (i)

i = readInput("data.txt")
col1 = []
col2 = []
for x in range(len(i)):
    if (x+1) % 2 == 1:
        col1.append(int(i[x]))
    else:
        col2.append(int(i[x]))
col1.sort()
col2.sort()

distance=0
similarity=0

for x in range(len(col1)):
    if col1[x]>=col2[x]:
        distance+=col1[x]-col2[x]
    else:
        distance+=col2[x]-col1[x]
    ### Part2
    c=0
    for y in range(len(col2)):
        if col1[x]==col2[y]:
            c+=1
    similarity+=col1[x]*c

print(distance, similarity)
