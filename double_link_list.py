# coding=utf-8


class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """双链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head  # cur用来指定链表的节点位置
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        print "当前链表所有元素为：",
        while cur is not None:
            print cur.elem,
            cur = cur.next
        print ""

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node  # 注意node和node.elem的区别
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素"""
        node = Node(item)
        count = 0
        cur = self.__head
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            while count < (pos-1):
                cur = cur.next
                count += 1
            node.next = cur.next
            node.prev = cur
            cur.next = node
            node.next.prev = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                # 判断是否是头节点
                if cur == self.__head:
                    # 是头节点：
                    # 再判断是否仅有一个节点：
                    if cur.next is None:
                        self.__head = None
                    # 不止一个节点：
                    else:
                        self.__head = cur.next
                # 不是头结点：
                elif cur.next is None:
                    cur.prev.next = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
            cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


def test():
    link_list = DoubleLinkList()
    print(link_list.is_empty())
    print link_list.search(1)
    print(link_list.length())
    link_list.append(1)
    print(link_list.is_empty())
    print(link_list.length())
    link_list.remove(1)
    link_list.travel()
    link_list.append(2)
    link_list.append(3)
    link_list.append(4)
    link_list.append(5)
    link_list.append(6)
    link_list.travel()
    link_list.add(7)
    link_list.travel()
    link_list.insert(2,8)
    link_list.travel()
    print link_list.search(1)
    print link_list.search(10)
    link_list.remove(8)
    link_list.travel()


if __name__ == "__main__":
    test()

"""
注意各操作要彻底，不要藕断丝连，
这里就因为插入元素函数少处理了一条链接，
导致出现删除函数唯独不能删除经过插入函数插入的元素，
这一奇妙的bug
"""
