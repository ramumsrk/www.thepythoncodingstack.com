#! /usr/bin/python3.12

if __name__ == '__main__':
  great_food : list[str] = [
    "Cacio e Pepe",
    'Pizza al Taglio',
    "Saltimbocca",
    'Suppli',
  ]
  print(f'Type of `great_food\' is \'{type(great_food)=}\'')
  # Another name for the same list
  what_im_eating_this_week : list[str] = great_food
  # Are both the list references pointing to the same object
  if what_im_eating_this_week is great_food:
    print(F'\'{id(what_im_eating_this_week)=}\' and \'{id(great_food)=}\'')