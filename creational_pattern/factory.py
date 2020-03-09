# -*- coding: utf-8 -*-

"""工厂模式、抽象工厂模式的优点：
1、工厂模式巨有非常好的封装性，代码结构清晰；在抽象工厂模式中，其结构还可以随着需要进行更深或者更浅的抽象层级调整，非常灵活；
2、屏蔽产品类，使产品的被使用业务场景和产品的功能细节可以分而开发进行，是比较典型的解耦框架。

工厂模式、抽象工厂模式的使用场景：
1、当系统实例要求比较灵活和可扩展时，可以考虑工厂模式或者抽象工厂模式实现。
比如，在通信系统中，高层通信协议会很多样化，同时，上层协议依赖于下层协议，
那么就可以对应建立对应层级的抽象工厂，根据不同的“产品需求”去生产定制的实例。
"""

"""工厂类模式的不足
1、工厂模式相对于直接生成实例过程要复杂一些，所以，在小项目中，可以不使用工厂模式；
2、抽象工厂模式中，产品类的扩展比较麻烦。毕竟，每一个工厂对应每一类产品，产品扩展，就意味着相应的抽象工厂也要扩展。
"""


class Burger:
    """ 汉堡 - 抽象产品类 """
    name = ""
    price = 0.0

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class CheeseBurger(Burger):
    """ 芝士汉堡 - 具体产品类 """

    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class SpicyChickenBurger(Burger):
    """ 香辣鸡肉堡 - 具体产品类 """

    def __init__(self):
        self.name = 'spicy chicken burger'
        self.price = 15.0


class Snack:
    """ 小食 - 抽象产品类 """
    name = ""
    price = 0.0
    type = "SNACK"

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Chips(Snack):
    """ 薯条 """

    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class ChickenWings(Snack):
    """ 鸡翅 """

    def __init__(self):
        self.name = "chicken wings"
        self.price = 10.0


class Beverage:
    """ 饮料 """
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Coke(Beverage):
    """ 可乐 """

    def __init__(self):
        self.name = "coke"
        self.price = 3.0


class Milk(Beverage):
    """ 牛奶 """

    def __init__(self):
        self.name = "milk"
        self.price = 5.0


class FoodFactory:
    """ 工厂 """
    type = ""

    @classmethod
    def create_food(cls, FoodCls):
        print("Simple factory produce a instance")
        food_ins = FoodCls()
        return food_ins


class BurgerFactory(FoodFactory):
    """ 汉堡工厂 """

    def __init__(self):
        self.type = "BURGER"


class SnackFactory(FoodFactory):
    """ 小食工厂 """

    def __init__(self):
        self.type = "SNACK"


class BeverageFactory(FoodFactory):
    """ 饮料工厂 """

    def __init__(self):
        self.type = "BEVERAGE"


if __name__ == '__main__':
    # 工厂模式
    # 初始化工厂
    # burger_factory = BurgerFactory()
    # snack_factory = SnackFactory()
    # beverage_factory = BeverageFactory()
    #
    # # 点餐
    # cheese_burger = burger_factory.create_food(CheeseBurger)
    # print(cheese_burger.get_name(), cheese_burger.get_price())
    #
    # chicken_wings = snack_factory.create_food(ChickenWings)
    # print(chicken_wings.get_name(), chicken_wings.get_price())
    #
    # coke_drink = beverage_factory.create_food(Coke)
    # print(coke_drink.get_name(), coke_drink.get_price())

    # 简单工厂模式
    cheese_burger = BurgerFactory.create_food(CheeseBurger)
    chicken_wings = SnackFactory.create_food(ChickenWings)
    coke_drink = BeverageFactory.create_food(Coke)

    # 抽象工厂 伪代码
    # cheese_burger = CheeseBurgerFacotry.create()
