# -*- coding: utf-8 -*-
"""原型模式定义如下：用原型实例指定创建对象的种类，并且通过复制这些原型创建新的对象。
需要注意一点的是，进行clone操作后，新对象的构造函数没有被二次执行，新对象的内容是从内存里直接拷贝的。

优点：
1、性能极佳，直接拷贝比在内存里直接新建实例节省不少的资源；
2、简化对象创建，同时避免了构造函数的约束，不受构造函数的限制直接复制对象，是优点，也有隐患，这一点还是需要多留意一些。

使用场景：
1、对象在修改过后，需要复制多份的场景。如本例和其它一些涉及到复制、粘贴的场景；
2、需要优化资源的情况。如，需要在内存中创建非常多的实例，可以通过原型模式来减少资源消耗。
此时，原型模式与工厂模式配合起来，不管在逻辑上还是结构上，都会达到不错的效果；
3、某些重复性的复杂工作不需要多次进行。如对于一个设备的访问权限，多个对象不用各申请一遍权限，
由一个设备申请后，通过原型模式将权限交给可信赖的对象，既可以提升效率，又可以节约资源。

缺点：
1、深拷贝和浅拷贝的使用需要事先考虑周到；
2、某些编程语言中，拷贝会影响到静态变量和静态函数的使用。
"""
import copy


class SimpleLayer:
    background = [0, 0, 0, 0]
    content = ""

    def get_content(self):
        return self.content

    def get_background(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def set_parent(self, p):
        self.background[3] = p

    def fill_background(self, back):
        self.background = back

    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    layer = SimpleLayer()
    layer.paint("Dog")
    layer.fill_background([0, 0, 255, 0])
    print("Original Background:", layer.get_background())
    print("Original Content:", layer.get_content())
    print("***" * 30)

    # 浅拷贝
    # copy_layer = layer.clone()
    # print("Copy Background:", copy_layer.get_background())
    # print("Copy Content:", copy_layer.get_content())
    # print("***" * 30)

    # 浅拷贝修改
    # copy_layer.paint("Cat")
    # copy_layer.set_parent(128)
    # print("Original Background:", layer.get_background())
    # print("Original Content:", layer.get_content())
    # print("Copy Background:", copy_layer.get_background())
    # print("Copy Content:", copy_layer.get_content())
    # print("***" * 30)

    # 深拷贝修改
    deep_copy_layer = layer.deep_clone()
    deep_copy_layer.paint("Cat")
    deep_copy_layer.set_parent(128)
    print("Original Background:", layer.get_background())
    print("Original Content:", layer.get_content())
    print("Copy Background:", deep_copy_layer.get_background())
    print("Copy Content:", deep_copy_layer.get_content())
