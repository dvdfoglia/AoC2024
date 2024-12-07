def read_input(file_path):
    with open(file_path, 'r') as input_file:
        return [list(map(int, line.split())) for line in input_file.read().splitlines()]

def is_safe(report):
    increase = False
    decrease = False
    for y in range(1, len(report)):
        difference = abs(report[y] - report[y-1])
        if difference > 3 or difference == 0:
            return False
        if report[y] > report[y-1]:
            if decrease:
                return False
            increase = True
        else:
            if increase:
                return False
            decrease = True
    return True

def is_safe_dampener(report):
    if is_safe(report):
        return True
    for j in range(len(report)):
        modified_report = report[:j] + report[j+1:]
        if is_safe(modified_report):
            return True
    return False

data = read_input("data.txt")

part1 = sum(1 for report in data if is_safe(report))
print("Reports safe part 1:", part1)

part2 = sum(1 for report in data if is_safe_dampener(report))
print("Reports safe part 2:", part2)
