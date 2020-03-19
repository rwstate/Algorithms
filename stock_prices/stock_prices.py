#!/usr/bin/python

import argparse

# Given an array of integers arr, find the maximum value of arr[b] - arr[a] where a < b
# 1. iterate from i = len(arr) - 1 to i = 1
# 2. for the first iteration, set arr[i] to maxSell and push maxSell to sells = []
# 3. for each iteration after that, if arr[i] > maxSell, set arr[i] to maxSell and
#    then place current maxSell at the beginning of sell
# 4. iterate from i = 0 to i = len(arr) - 2
# 5. for the first iteration, set sells[i] - arr[i] to maxProfit
# 6. for each iteration after that, if sells[i] - arr[i] > maxProfit, 
#    set sells[i] - arr[i] to maxProfit
# 7. return maxProfit
def find_max_profit(prices):
  maxSell = prices[-1]
  bestSells = [prices[-1]]
  i = len(prices) - 2
  while i > 0:
    if prices[i] > maxSell:
      maxSell = prices[i]
    bestSells.insert(0, maxSell)
    i -= 1
  i = 1
  maxProfit = bestSells[0] - prices[0]
  while i < len(prices) - 1:
    if bestSells[i] - prices[i] > maxProfit:
      maxProfit = bestSells[i] - prices[i]
    i += 1
  return maxProfit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))