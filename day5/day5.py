import time

start_time = time.time()

def read_input(file_path):
    with open(file_path, 'r') as input_file:
        return input_file.read().split("\n\n")

def is_correct(update, rule):
    correct=[True,0,0]
    for page in update:
        if correct==[True,0,0]:
            if page==rule[1]: correct=[True,0,1]
        if correct==[True,0,1]:
            if page==rule[0]:
                correct=[False,0,1]
                break
    return correct[0]

def reorder_update(update, rules):
    updated = update.copy()
    changed = True
    while changed:
        changed = False
        for i in range(len(updated) - 1):
            for rule in rules:
                if updated[i] == rule[1] and updated[i+1] == rule[0]:
                    updated[i], updated[i+1] = updated[i+1], updated[i]
                    changed = True
                    break
    return updated

input_data = read_input("data.txt")
rules = [tuple(map(int,rule.split("|"))) for rule in input_data[0].splitlines()]
updates = [list(map(int,update.split(","))) for update in input_data[1].splitlines()]

part1 = 0
part2 = 0

for update in updates:
    correct = True
    for rule in rules:
        if not is_correct(update, rule):
            correct = False
            break
    
    if correct:
        part1 += update[len(update)//2]
    else:
        reordered = reorder_update(update, rules)
        part2 += reordered[len(reordered)//2]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

elapsed_time = time.time() - start_time
print(f"Elapsed time: {elapsed_time:.3f} seconds")