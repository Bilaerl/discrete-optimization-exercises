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
    memo = [0 for j in range(capacity+1)]

    # Dynamic programming
    for item in items:
        k = capacity
        while k:
            if item.weight > k:
                v = memo[k]
            
            else:
                v_item_taken = item.value + memo[k-item.weight]
                v_item_not_taken = memo[k]

                v = max(v_item_taken, v_item_not_taken)
            
            memo[k] = v
            k -= 1
    
    value = memo[capacity]

    # getting selected items
    # need to work on this, its probably not selecting the right items
    k = capacity
    j = item_count

    while j:
        item = items[j-1]
        if memo[k] == memo[k - item.weight] + item.value:
            taken[j-1] = 1
            k = k - item.weight
        
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

