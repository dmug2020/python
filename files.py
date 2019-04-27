def get_dish_fromfile():
 """
 Принимает списко блюд из файла recipes.txt(лежит той же папке что и файл files.py и преобразует в словарь cook_book
 """
  cook_book = {}
  with open('recipes.txt', encoding='utf-8') as f:
       for line in f:
        dish = line.strip()  # Имя блюда
        count = int(f.readline())  # Количество ингредиентов
        ingridients = []
        while count > len(ingridients):  # Читаем пока не наберем нужное количество
            ingridient = f.readline().strip().split('|')
            ingridients.append({
              'ingridient_name': ingridient[0].strip(),
              'quantity': (ingridient[1]),
              'measure': ingridient[2].strip()
            })
        cook_book[dish] = ingridients  # добавляем блюдо в словарь

        f.readline()  # считывание пустой строки

  print (cook_book)


get_dish_fromfile()

cook_book = {
  'Омлет': [
    {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingridient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
    {'ingridient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

def get_shop_list_dishes(dishes, person_count):
 """
 Принимает список блюд из cook_book и количество персон для кого мы будем готовить и добавляет в словарь shop_items
 """
  shop_items = {}
  for dish in cook_book:
    for ingredients in cook_book[dish]:
      product_info = ingredients
      product_info['quantity'] *= person_count # умножаем на кол-во персон
      if product_info['ingridient_name'] not in shop_items: # если в словаре покупок нет названия нашего ингредиента, то:
        shop_items[product_info['ingridient_name']] =  product_info #добавляем все данные об этом ингредиенте
      else:
        shop_items[product_info['ingridient_name']]['quantity'] += product_info['quantity']

  return shop_items

def name_func(shop_items):
"""
Выводит ингридиенты блюд
"""
  for shop_items_list in shop_items.values():
    print('{} {} {}'.format(shop_items_list['ingridient_name'], shop_items_list['quantity'], shop_items_list['measure']))


def print_shop_items_for_dishes():
"""
Выводит ингридиенты блюд для введенного кол-ва персон
"""
    person_count = int(input('Введите кол-во персон: '))
    dishes = ['Омлет', 'Запеченый картофель']
    shop_items = get_shop_list_dishes(dishes, person_count)
    name_func(shop_items)

print_shop_items_for_dishes()



