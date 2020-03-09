# -*- coding: utf-8 -*-
import threading
import time

"""某中央处理器（CPU）通过某种协议总线与一个信号灯相连，信号灯有64种颜色可以设置，
中央处理器上运行着三个线程，都可以对这个信号灯进行控制，并且可以独立设置该信号灯的颜色。
抽象掉协议细节（用打印表示），如何实现线程对信号等的控制逻辑。
加线程锁进行控制，无疑是最先想到的方法，但各个线程对锁的控制，无疑加大了模块之间的耦合。

单例模式是指：保证一个类仅有一个实例，并提供一个访问它的全局访问点。
具体到此例中，总线对象，就是一个单例，它仅有一个实例，各个线程对总线的访问只有一个全局访问点，即惟一的实例。
"""

"""单例模式的优点：
1、由于单例模式要求在全局内只有一个实例，因而可以节省比较多的内存空间；
2、全局只有一个接入点，可以更好地进行数据同步控制，避免多重占用；
3、单例可长驻内存，减少系统开销。

单例模式的应用举例：
1、生成全局惟一的序列号；
2、访问全局复用的惟一资源，如磁盘、总线等；
3、单个对象占用的资源过多，如数据库等；
4、系统全局统一管理，如Windows下的Task Manager；
5、网站计数器。
"""

"""单例模式的缺点：
1、单例模式的扩展是比较困难的；
2、赋于了单例以太多的职责，某种程度上违反单一职责原则（六大原则后面会讲到）;
3、单例模式是并发协作软件模块中需要最先完成的，因而其不利于测试；
4、单例模式在某种情况下会导致“资源瓶颈”。
"""

class Singleton:
    """ 单例 """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Bus(Singleton):
    """ 总线 """
    lock = threading.RLock()

    def send_data(self, data):
        self.lock.acquire()
        time.sleep(3)
        print('Sending Single Data...', data)
        self.lock.release()


# demo
class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        print("my_bus的内存地址: %d" % id(self.my_bus))
        self.my_bus.send_data(self.name)


if __name__ == '__main__':
    for i in range(3):
        print("Entity %d begin to run..." % i)
        entity = VisitEntity()
        entity.set_name("Entity_" + str(i))
        entity.start()
