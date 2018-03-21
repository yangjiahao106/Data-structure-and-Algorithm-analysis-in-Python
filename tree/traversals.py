#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/23
from queue import Queue


class Node(object):
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            queue_ = Queue()
            queue_.put(self.root)
            while queue_:
                cur = queue_.get(0)
                if cur.left is None:
                    cur.left = node
                    return
                elif cur.right is None:
                    cur.right = node
                    return
                else:
                    queue_.put(cur.left)
                    queue_.put(cur.right)

    def pre_order(self, node):
        if not isinstance(node, Node) or not node:
            return
        print(node.val, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if not isinstance(node, Node) or not node:
            return
        self.in_order(node.left)
        print(node.elfment, end=" ")
        self.in_order(node.right)

    def post_order(self, node):
        if not isinstance(node, Node) or not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val, end=" ")

    @staticmethod
    def level_order(root_in):
        if root_in is None:
            return
        q = Queue()
        q.put(root_in)

        while not q.empty():
            cur = q.get()
            print(cur.val, end=' ')
            if cur.left is not None:
                q.put(cur.left)
            if cur.right is not None:
                q.put(cur.right)


if __name__ == '__main__':
    tree = BinaryTree()
    vals = [1,2,3,4,5,6]
    for v in vals:
        tree.add(v)
    print('pre order:')
    tree.pre_order(tree.root)

    print('\nlevel order:')
    tree.level_order(tree.root)
