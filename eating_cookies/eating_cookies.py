#!/usr/bin/python

import sys

# base cases n < 2 return 1, n< 0 return 0

def cookie_helper(n, index, cache):
  cache[index] += (cache[index - 3] + cache[index - 2] + cache [index - 1])
  if index == n:
    return cache
  return cookie_helper(n, index + 1, cache)

def eating_cookies(n, cache=None):
  if n == 0: return 1
  if n == 1: return 1
  initCache = [0] * (n + 1)
  initCache[0] = 1
  initCache[1] = 1
  return cookie_helper(n, 2, initCache)[-1]

print(eating_cookies(10))



# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')