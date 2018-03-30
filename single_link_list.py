# coding=utf-8


class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        """
        if self.__head == None:
            return True
        else:
            return False
        """
        # 以上等价为：
        return self.__head == None

    def length(self):
        """链表长度"""
        cur = self.__head  # cur用来指定链表的节点位置
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        print "当前链表所有元素为：",
        while cur != None:
            print cur.elem,
            cur = cur.next
        print ""

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node  # 注意node和node.elem的区别

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        """
        if self.__head == None
            self.__head = node
        """
        # 以下方式更直观：
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

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
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        """
        # 是否为空链表
        if cur == None
            return False
        # 是否仅有一个头节点
        elif cur.next == None:
            if cur.elem == item:
                head.__ = None
            else:
                return False
        elif cur.elem == item:
            self.__head = cur.next
        else:   
            while cur.next == None:
                if cur.next.elem == item:
                    cur.next = cur.next.next
                cur = cur.next
        """
        # 以上尝试用单cur变量实现，单链表无法返回，失败
        pre = None  # pre为cur的前一个节点
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
            pre = cur
            cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


def test():
    # node = Node(1)
    link_list = SingleLinkList()
    print(link_list.is_empty())
    print link_list.search(1)
    print(link_list.length())
    link_list.append(1)
    print(link_list.is_empty())
    print(link_list.length())
    link_list.append(2)
    link_list.append(3)
    link_list.append(4)
    link_list.append(5)
    link_list.append(6)
    link_list.travel()
    link_list.add(7)
    link_list.travel()
    link_list.insert(34,8)
    link_list.travel()
    print link_list.search(1)
    print link_list.search(10)
    link_list.remove(9)
    link_list.travel()

if __name__ == "__main__":
    test()
