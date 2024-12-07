import time
import os
import copy

def read_input(file_path):
    with open(file_path, 'r') as input_file:
        return [[[char, False,False,False,False,False] for char in list(line)] for line in input_file.read().splitlines()]


def find_start(grid):
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if col[0]=="^": start=[row_idx,col_idx]
    return(start)

def patrol(grid):
    direction="^"
    patrol=True
    p=find_start(grid)
    g=copy.deepcopy(grid)
    loop=False
    visited=0
    i=0
    while patrol:
        while direction=="^" and patrol:
            if g[p[0]][p[1]][2]==True: loop=True; patrol=False
            g[p[0]][p[1]][1]=True;g[p[0]][p[1]][2]=True
            if p[0]==0: patrol=False
            elif g[p[0]-1][p[1]][0]=="#": direction=">"
            else: p[0]-=1
        while direction==">" and patrol:
            if g[p[0]][p[1]][3]==True: loop=True; patrol=False
            g[p[0]][p[1]][1]=True;g[p[0]][p[1]][3]=True
            if p[1]==len(g[p[0]])-1: patrol=False
            elif g[p[0]][p[1]+1][0]=="#": direction="v"
            else: p[1]+=1
        while direction=="v" and patrol:
            if g[p[0]][p[1]][4]==True: loop=True; patrol=False
            g[p[0]][p[1]][1]=True;g[p[0]][p[1]][4]=True
            if p[0]==len(g)-1: patrol=False
            elif g[p[0]+1][p[1]][0]=="#": direction="<"
            else: p[0]+=1
        while direction=="<" and patrol:
            if g[p[0]][p[1]][5]==True: loop=True; patrol=False
            g[p[0]][p[1]][1]=True;g[p[0]][p[1]][5]=True
            if p[1]==0: patrol=False
            elif g[p[0]][p[1]-1][0]=="#": direction="^"
            else: p[1]-=1
    visited = sum(cell[1] for row in g for cell in row)
    return visited,loop

def add_obstruction(grid):
    g = copy.deepcopy(grid)
    result=[]
    for row_idx, row in enumerate(g):
        for col_idx, col in enumerate(row):
            cell=col[0]
            if cell=="^"or cell=="#" : pass
            else:
                col[0]="#"
                result.append(patrol(g))
                col[0]="."
    loop = sum(1 for _, status in result if status)

    return loop

def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    start_time = time.time()
    grid = read_input("data.txt")

    print("Total position visited:", patrol(grid)[0])
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")

    print("Obstruction:", add_obstruction(grid))
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")
if __name__ == "__main__":
    main()