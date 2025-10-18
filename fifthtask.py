items = {
 'milk15':{'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
 'cheese':{'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
 'sausage':{'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}
price_less_20 = dict()

for i in items:
    if items[i]['count'] < 20:
        price_less_20[i] = True
    else:
        price_less_20[i] = False
print(price_less_20)
