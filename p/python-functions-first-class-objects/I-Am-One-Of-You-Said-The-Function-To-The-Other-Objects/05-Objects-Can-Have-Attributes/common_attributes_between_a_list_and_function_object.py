#! /usr/bin/python3.12

if __name__ == '__main__':
  print(f'\'{(set([].__dir__()) & set(print.__dir__()))}\'')