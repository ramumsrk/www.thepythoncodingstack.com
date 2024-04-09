#! /usr/bin/python3.12

# User defined function
def create_menu(food_items : list[str]) -> None:
  print(f'On holiday I\'ll eat \'{food_items=}\'')
  return

if __name__ == '__main__':
  print(F'Type of \'create_menu\' is \'{type(create_menu)=}\'')
  order_food = create_menu
  if order_food is create_menu:
    print(f'\'{id(create_menu)=}\' and \'{id(order_food)}\'')