import time
import os
from itertools import combinations

def read_input(file_path):
    with open(file_path, 'r') as input_file:
        return [list(line) for line in input_file.read().splitlines()]

def find_antenna(grid):
    positions={}
    for l_idx, l in enumerate(grid):
        for c_idx, c in enumerate(l):
            if c != ".":
                if c not in positions:
                    positions[c]=[(l_idx,c_idx)]
                else:
                    positions[c].append((l_idx,c_idx))
    return positions

def find_antinodes(antenna,l,part2):
    antinodes={}
    for k in antenna:
        for comb in (combinations(antenna[k],2)):
            if part2:
                for an in comb:
                    if k not in antinodes:
                        antinodes[k]=[an]
                    else: 
                        antinodes[k].append(an)
            dist_x=comb[0][0]-comb[1][0]
            dist_y=comb[0][1]-comb[1][1]
            for dir in ["+","-"]:
                c=0
                while True:
                    c=c+1
                    if dir == "+": an=(comb[0][0]+(dist_x*c),comb[0][1]+(dist_y*c))
                    if dir == "-": an=(comb[1][0]-(dist_x*c),comb[1][1]-(dist_y*c))
                    if is_valid(an,l):
                        if k not in antinodes:
                            antinodes[k]=[an]
                        else: 
                            antinodes[k].append(an)
                    else: break
                    if not part2: break
    return antinodes

def is_valid(antinode,l):
    if antinode[0]>=0 and antinode[0]<l[0] and antinode[1]>=0 and antinode[1]<l[1]: 
        return True
    else: 
        return False
    
def unique(antinodes):
    res=[]
    for k in antinodes:
        for v in antinodes[k]:
            if v not in res:
                res.append(v)
    return res

def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    start_time = time.time()
    grid = read_input("data.txt")
    limit=(len(grid),len(grid[0]))
    antennas=find_antenna(grid)
    
    antinodes=find_antinodes(antennas,limit,False)
    print("Part1",len(unique(antinodes)))

    antinodes=find_antinodes(antennas,limit,True)
    print("Part2",len(unique(antinodes)))


    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    main()