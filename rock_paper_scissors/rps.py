#!/usr/bin/python

import sys

def helper(movesListList):
    if not movesListList:
        yield []
    else:
        for a in movesListList[0]:
            for b in helper(movesListList[1:]):
                yield [a] + b

def rock_paper_scissors(n):
  moveList = [["rock", "paper", "scissors"]] * n
  print(moveList)
  return list(helper(moveList))
  
print(rock_paper_scissors(8))
# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')