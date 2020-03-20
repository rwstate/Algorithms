#!/usr/bin/python

import math

# 1. if len(ingr) < len(recipe), => 0
# 2. for i in range(0, len(ingr)), set maxBatch to rec[i] // ing[i] if the latter is less than maxBatch
# 3. return maxBatch

def recipe_batches(recipe, ingredients):
  if len(ingredients) < len(recipe):
    return 0
  maxBatch = float("inf")
  for i in recipe:
    if ingredients[i] // recipe[i] < maxBatch:
      maxBatch = ingredients[i] // recipe[i]
  return maxBatch 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))