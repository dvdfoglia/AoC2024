import time
import os

def read_input(file_path):
    with open(file_path, 'r') as input_file:
        return [int(value) for value in list(input_file.read())]

def map_block(diskmap):
    map={}
    map["."]=[]
    sector=0
    for b_idx,b in enumerate(diskmap):
        if b_idx%2==0:
            map[b_idx//2]=[]
            for i in range(0,b): map[b_idx//2].append(sector); sector+=1
        else:
            for i in range(0,b): map["."].append(sector); sector+=1
    return map

def defrag_map(map):
    empty=0
    for k in reversed(map):
        if map[k]==".": break
        for a in reversed(range(len(map[k]))):
            if empty>len(map["."])-1 or map["."][empty]>map[k][a]: break
            map[k][a], map["."][empty] = map["."][empty], map[k][a]
            empty+=1

    return map

def optimize_map(map):
    for file_id in reversed(map.keys()):
        if file_id == ".":
            continue
        file_positions = list(map[file_id])
        file_size = len(file_positions)
        
        free_spaces = map["."]
        for i in range(len(free_spaces) - file_size + 1):
            contiguous_free_space = free_spaces[i:i + file_size]
            if contiguous_free_space == list(range(contiguous_free_space[0], contiguous_free_space[0] + file_size)):
                if contiguous_free_space[0] < file_positions[0]:
                    for j in range(file_size):
                        map[file_id][j] = contiguous_free_space[j]
                        map["."].remove(contiguous_free_space[j])
                
                    for old_position in file_positions:
                        map["."].append(old_position)
                    break
    return map

def checksum_map(map):
    checksum=0
    for k in map:
        if k!=".":
            checksum+=k*sum(map[k])
    return checksum

def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    start_time = time.time()
    diskmap = read_input("data.txt")
    blockmap=map_block(diskmap)
    part1=checksum_map(defrag_map(blockmap))
    
    print("Part1",part1)

    blockmap=map_block(diskmap)
    part2=(checksum_map(optimize_map(blockmap)))
    print("Part2",part2)


    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    main()