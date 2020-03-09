# -*- coding: utf-8 -*-

"""为某对象提供一个代理，以控制对此对象的访问和控制。
代理模式在使用过程中，应尽量对抽象主题类进行代理，而尽量不要对加过修饰和方法的子类代理。

优点:
1、职责清晰：非常符合单一职责原则，主题对象实现真实业务逻辑，而非本职责的事务，交由代理完成；
2、扩展性强：面对主题对象可能会有的改变，代理模式在不改变对外接口的情况下，可以实现最大程度的扩展；
3、保证主题对象的处理逻辑：代理可以通过检查参数的方式，保证主题对象的处理逻辑输入在理想范围内。

应用场景：
1、针对某特定对象进行功能和增强性扩展。如IP防火墙、远程访问代理等技术的应用；
2、对主题对象进行保护。如大流量代理，安全代理等；
3、减轻主题对象负载。如权限代理等。

缺点:
可能会降低整体业务的处理效率和速度。
"""


class Server:
    """ 网络服务器 """
    content = ""

    def recv(self, info):
        pass

    def send(self, info):
        pass

    def show(self):
        pass


class InfoServer(Server):
    """infoServer有接收和发送的功能，发送功能由于暂时用不到，保留。另外新加一个接口show，
    用来展示服务器接收的内容。接收的数据格式必须如info_struct所示，服务器仅接受info_struct的content字段。
    那么，如何给这个服务器设置一个白名单，使得只有白名单里的地址可以访问服务器呢？
    修改Server结构是个方法，但这显然不符合软件设计原则中的单一职责原则。--使用代理
    """

    def recv(self, info):
        self.content = info
        return "Recv OK!"

    def send(self, info):
        pass

    def show(self):
        print("Show: ", self.content)


class ServerProxy:
    pass


class InfoServerProxy(ServerProxy):
    def __init__(self, server):
        self.server = server

    def recv(self, info):
        return self.server.recv(info)

    def show(self):
        self.server.show()


class WhiteInfoServerProxy(InfoServerProxy):
    """代理中有一个server字段，控制代理的服务器对象，infoServerProxy充当Server的直接接口代理，
    而whiteInfoServerProxy直接继承了infoServerProxy对象，同时加入了white_list和对白名单的操作。
    这样，在场景中通过对白名单代理的访问，就可以实现服务器的白名单访问了。
    """
    white_list = []

    def recv(self, info):
        try:
            assert type(info) == dict
        except:
            return "info structure is not correct"

        addr = info.get("addr", 0)
        if not addr in self.white_list:
            return "Your address is not in the white list"
        else:
            content = info.get("content" "")
            return self.server.recv(content)

    def add_white(self, addr):
        self.white_list.append(addr)

    def rmv_white(self, addr):
        self.white_list.remove(addr)

    def clear_white(self):
        self.white_list = []


if __name__ == '__main__':
    info_struct = {
        "addr": 10010,
        "content": "Hello, world!"
    }

    info_server = InfoServer()
    info_server_proxy = WhiteInfoServerProxy(info_server)
    print(info_server_proxy.recv(info_struct))

    info_server_proxy.show()
    info_server_proxy.add_white(10010)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()
