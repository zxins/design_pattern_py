# -*- coding: utf-8 -*-
"""装饰器模式和代理模式非常相似，可以认为，装饰器模式就是代理模式的一个特殊应用，
两者的共同点是都具有相同的接口，不同点是侧重对主题类的过程的控制，而装饰模式则侧重对类功能的加强或减弱。

优点：
1、装饰器模式是继承方式的一个替代方案，可以轻量级的扩展被装饰对象的功能；
2、Python的装饰器模式是实现AOP的一种方式，便于相同操作位于不同调用位置的统一管理。

应用场景：
需要扩展、增强或者减弱一个类的功能。

缺点：
多层装饰器的调试和维护有比较大的困难。
"""

"""快餐店卖可乐时，可以选择加冰，如果加冰的话，要在原价上加0.3元；
卖牛奶时，可以选择加糖，如果加糖的话，要原价上加0.5元。
怎么解决这样的问题？可以选择装饰器模式来解决这一类的问题。
"""


class Beverage:
    def __init__(self):
        self.name = ""
        self.price = 0.0
        self.type = "BEVERAGE"

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Coke(Beverage):
    def __init__(self):
        super().__init__()
        self.name = "coke"
        self.price = 4.0


class DrinkDecorator:
    def get_name(self):
        pass

    def get_price(self):
        pass


class IceDrinkDecorator(DrinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_name(self):
        return self.beverage.get_name() + "ice"

    def get_price(self):
        """ 加冰要加0.3元 """
        return self.beverage.get_price() + 0.3


class SugarDrinkDecorator(DrinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_name(self):
        return self.beverage.get_name() + "sugar"

    def get_price(self):
        """ 加糖要加0.5元 """
        return self.beverage.get_price() + 0.5


if __name__ == '__main__':
    coke = Coke()
    print("Name:", coke.get_name())
    print("Price:", coke.get_price())

    ice_coke = IceDrinkDecorator(coke)
    print("Name:", ice_coke.get_name())
    print("Price:", ice_coke.get_price())
