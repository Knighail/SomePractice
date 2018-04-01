# coding=utf-8

class Node(object):
    """树的节点"""
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self, item):
        """增加节点"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            else:
                cur_node.lchild = node
                return
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
            else:
                cur_node.rchild = node
                return

    def breadth_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print cur_node.elem,
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
        print ""

    def preorder(self, node):
        """前序遍历"""
        if node is None:
            return
        print node.elem,
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print node.elem,
        self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print node.elem,


def main():
    binary_tree = BinaryTree()
    binary_tree.add(0)
    binary_tree.add(1)
    binary_tree.add(2)
    binary_tree.add(3)
    binary_tree.add(4)
    binary_tree.add(5)
    binary_tree.add(6)
    binary_tree.add(7)
    binary_tree.add(8)
    binary_tree.add(9)
    binary_tree.breadth_travel()
    binary_tree.preorder(binary_tree.root)
    print ""
    binary_tree.inorder(binary_tree.root)
    print ""
    binary_tree.postorder(binary_tree.root)
    print ""


if __name__=="__main__":
    main()
