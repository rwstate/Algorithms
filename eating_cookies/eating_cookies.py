#!/usr/bin/python

import sys

# base cases n < 2 return 1, n< 0 return 0

def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  if n == 0:
    return 1
  return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

print(eating_cookies(10))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')