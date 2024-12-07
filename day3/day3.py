import re
def read_input(file_path):
    with open(file_path, 'r') as input_file:
        return input_file.read()

def part1(mul):
    res=0
    for x in mul:
        t=1
        for y in x.replace('mul(','').replace(')','').split(','):
            t*=int(y)
        res+=t
    return(res)

data=read_input("data.txt")
print('Part1',part1(re.findall(r'mul\([0-9]+,[0-9]+\)',data)))
# Part2
data=(re.findall(r'[a-z\']*\([0-9,]*\)',data))
enable=True
res=0
for x in data:
    print(x)
    if x=="don't()": enable=False
    if x=='do()': enable=True
    if enable and 'mul(' in x:
        t=1
        for y in x.replace('mul(','').replace(')','').replace("'","").split(','):
            t*=int(y)
        res+=t
print('Part2',res)
