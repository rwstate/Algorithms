#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

itemList = [
  [42, 81, 1],
  [42, 42, 2],
  [68, 56, 3],
  [68, 25, 4],
  [77, 14, 5],
  [57, 63, 6],
  [17, 75, 7],
  [19, 41, 8],
  [94, 19, 9],
  [34, 12, 10]
]

# given an array of coordinates and a value n, find the subset of the array with the largest sum(x) while sum(y) <= n
# calculate x/y for each coord, push to efficiency array
# sort efficiency array
# base case 1 : no coords left; return full set
# base case 2: y is greater than x; return subset
# add first value of efficiency to result array
# pass in set minus efficiency array

def knapsack_helper(subset, limit, indexes): 
  if len(subset) == 0:
    return []
  if subset[0][0] > float(limit):
    return indexes
  indexes.append(subset[0][2])
  return knapsack_helper(subset[1:], limit - subset[0][0], indexes)

def get_efficiency(e):
  return e[1] / e[0]

def knapsack_solver(items, capacity):
  items.sort(reverse=True, key=get_efficiency)
  return knapsack_helper(items, capacity, [])

print(knapsack_solver(itemList, 100))


# if __name__ == '__main__':
#   if len(sys.argv) > 1:
#     capacity = int(sys.argv[2])
#     file_location = sys.argv[1].strip()
#     file_contents = open(file_location, 'r')
#     items = []

#     for line in file_contents.readlines():
#       data = line.rstrip().split()
#       items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
#     file_contents.close()
#     print(knapsack_solver(items, capacity))
#   else:
#     print('Usage: knapsack.py [filename] [capacity]')