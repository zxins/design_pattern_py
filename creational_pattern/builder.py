# -*- coding: utf-8 -*-
"""建造者模式
优点：
1、封装性好，用户可以不知道对象的内部构造和细节，就可以直接建造对象；
2、系统扩展容易；
3、建造者模式易于使用，非常灵活。在构造性的场景中很容易实现“流水线”；
4、便于控制细节。
缺点：
“加工工艺”对用户不透明。（封装的两面性）

使用场景：
1、目标对象由组件构成的场景中，很适合建造者模式。例如，在一款赛车游戏中，
车辆生成时，需要根据级别、环境等，选择轮胎、悬挂、骨架等部件，构造一辆“赛车”；
2、在具体的场景中，对象内部接口需要根据不同的参数而调用顺序有所不同时，可以使用建造者模式。
例如：一个植物养殖器系统，对于某些不同的植物，浇水、施加肥料的顺序要求可能会不同，
因而可以在Director中维护一个类似于队列的结构，在实例化时作为参数代入到具体建造者中。
"""

from creational_pattern.factory import CheeseBurger, Chips, Coke


class Order:
    """ 订单 """

    def __init__(self, order_builder):
        self.burger = order_builder.build_burger
        self.snack = order_builder.build_snack
        self.beverage = order_builder.build_beverage

    def show(self):
        print("Burger: %s" % self.burger.get_name())
        print("Snack: %s" % self.snack.get_name())
        print("Beverage: %s" % self.beverage.get_name())


class OrderBuilder:
    """ 订单建造者 """
    build_burger = ""
    build_snack = ""
    build_beverage = ""

    def add_burger(self, burger):
        self.build_burger = burger

    def add_snack(self, snack):
        self.build_snack = snack

    def add_beverage(self, beverage):
        self.build_beverage = beverage

    def build(self):
        return Order(self)


class OrderDirector:
    def __init__(self, order_builder):
        self.order_builder = order_builder

    def create_order(self, burger, snack, beverage):
        self.order_builder.add_burger(burger)
        self.order_builder.add_snack(snack)
        self.order_builder.add_beverage(beverage)
        return self.order_builder.build()


"""
建造者模式的定义如下：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
建造者模式的作用，就是将“构建”和“表示”分离，以达到解耦的作用。
在上面订单的构建过程中，如果将order直接通过参数定义好（其构建与表示没有分离），
同时在多处进行订单生成，此时需要修改订单内容，则需要一处处去修改，业务风险也就提高了不少。
在建造者模式中，还可以加一个Director类，用以安排已有模块的构造步骤。
对于在建造者中有比较严格的顺序要求时，该类会有比较大的用处。
"""

if __name__ == '__main__':
    # builder = OrderBuilder()
    # builder.add_burger(CheeseBurger())
    # builder.add_snack(Chips())
    # builder.add_beverage(Coke())
    #
    # order = builder.build()
    # order.show()

    builder = OrderBuilder()
    director = OrderDirector(builder)
    order = director.create_order(CheeseBurger(), Chips(), Coke())
    order.show()
