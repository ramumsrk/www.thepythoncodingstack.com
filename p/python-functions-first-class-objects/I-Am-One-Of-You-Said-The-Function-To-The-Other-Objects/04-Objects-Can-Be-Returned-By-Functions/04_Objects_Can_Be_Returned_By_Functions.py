#! /usr/bin/python3.12

import random

# User-defined function definition
def surprise_print():
  options : tuple = print , bool , random.randint , len
  return random.choice(options)

if __name__ == '__main__':
  print(f'\'{surprise_print()}\'')