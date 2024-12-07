import time
import os
import itertools as it
import operator
ops = {
    "+": operator.add,
    "*": operator.mul,
    "||": lambda a, b: int(str(a) + str(b)), 
}

def read_input(file_path):
    with open(file_path, 'r') as input_file:
        return [[int(value) for value in line.split()] for line in input_file.read().replace(":", "").splitlines()]


def evaluate(e):
    part1 = 0
    part2 = 0
    for eq in e:
        perm_n = len(eq) - 2
        perm = it.product(ops.keys(), repeat=perm_n)
        for p in perm:
            res = eq[1]
            for n in range(2, len(eq)):
                res = ops[p[n - 2]](res, eq[n])
            if res == eq[0]:
                if "||" in p: 
                    part2 += res
                else:
                    part1 += res
                break 
    return part1, part2

def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    start_time = time.time()
    equations = read_input("data.txt")
    results=evaluate(equations)
    result_p1=results[0]
    result_p2=sum(results)

    print("Part1",result_p1)
    print("Part2",result_p2)

    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    main()