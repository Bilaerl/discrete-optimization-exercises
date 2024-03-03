#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0 for i in range(item_count)]
    memo = [[0 for i in range(item_count+1)] for j in range(capacity+1)]

    # Dynamic programming
    for j, item in enumerate(items, start=1):
        for k in range(capacity+1):
            if item.weight > k:
                v = memo[k][j-1]
            
            else:
                v_item_taken = item.value + memo[k-item.weight][j-1]
                v_item_not_taken = memo[k][j-1]

                v = max(v_item_taken, v_item_not_taken)
            
            memo[k][j] = v
    
    value = memo[capacity][item_count]

    # getting selected items
    k = capacity
    j = item_count

    while j:
        if memo[k][j] != memo[k][j-1]:
            # use j-1 here due to python index starting at 0
            taken[j-1] = 1
            k = k-items[j-1].weight

        j = j-1
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

