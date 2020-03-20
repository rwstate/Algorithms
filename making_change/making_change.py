#!/usr/bin/python

import sys

# find all the combinations a given list of integers such that their sum is equal to a given integer
#                                      ^arg2^                                             ^arg1^
# create a helper function that takes arguments total, count, current change
# 
# 
# 1 - 1p
# 5 - 1n, 5p = 2 = 1 + num new coins
# 10 - 10p, 1n 5p, 2n, 1d = 4 =
# 15 - 15p, 10p 1n, 5p 1d, 1n 1d,5p 2n, 3n = 6
# 20 - 2d, 1d 2n, 1d 10p, 1d 1n 5p, 4n, 3n 5p, 2n 10p, 1n 15p, 20p = 9

# print(cache)

def helper(coins, cache):
  print(cache, coins)
  if len(coins) == 0:
    return cache[-1]
  for i in range(coins[0], len(cache)):
    cache[i] += cache[i - coins[0]]
  return helper(coins[1:], cache)
  

def making_change(amount, denominations):
  initCache = [0] * (amount + 1)
  initCache[0] = 1
  return helper(denominations, initCache)

print(making_change(200, [1, 5, 10, 25, 50]))

# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")