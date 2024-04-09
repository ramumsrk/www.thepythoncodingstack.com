#! /usr/bin/python3.12

if __name__ == '__main__':
  great_food : list[str] = [
    'Cacio e Pepe',
    "Pizza al Taglio",
    'Saltimbocca',
    "Suppli",
  ]
  print(f'\'{sorted(great_food , key=len)=}\'')