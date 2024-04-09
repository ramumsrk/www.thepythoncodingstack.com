#! /usr/bin/python3.12

if __name__ == '__main__':
  print(f'\'{bool(0)=}\'')
  print(F'\'{bool(10)=}\'')  
  print(f'\'{bool([])=}\'')
  great_food : list[str] = [
    'Cacio e Pepe',
    "Pizza al Taglio",
    'Saltimbocca',
    "Suppli",
  ]
  print(F'\'{bool(great_food)=}\'')