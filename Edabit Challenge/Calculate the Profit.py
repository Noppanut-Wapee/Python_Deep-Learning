'''
profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}) ➞ 14796

countries = {'th':'Thailand','jp':'Japan'}
for key in countries:
    print(countries[key]) # print value โดยใช้ Key
'''

def profit(info): 
    a = ((info['sell_price'] - info['cost_price'] )*info['inventory'] )
    return print(int(a))

profit({'cost_price': 0.1, 'sell_price': 0.18, 'inventory': 259800})

