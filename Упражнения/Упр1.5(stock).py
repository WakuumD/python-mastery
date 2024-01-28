"""
# Упражнение 1.5

*Цели:*

- Обзор того, как определить простой объект

* Созданные файлы: * `stock.py`

## (a) Определение простого объекта

Создайте файл `stock.py` и определите следующий класс:

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares #акции
        self.price = price #цена
    def cost(self):
        return self.shares * self.price

Как только вы это сделаете, запуsстите вашу программу и поэкспериментируйте с вашим новым
`Складской` объект:

```питон
>>> s = Stock('GOOG',100 490,10)
>>> фамилию
"GOOG"
>>> с.акции
100
>>> с.цена
490,1
>>> s.cost()
49010.0
>>> print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
       ГООГ 100 490,10
>>> t = Stock('IBM', 50, 91.5)
>>> t.cost()
4575.0
>>>
```
"""
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares #акции
        self.price = price #цена
    def cost(self):
        return self.shares * self.price