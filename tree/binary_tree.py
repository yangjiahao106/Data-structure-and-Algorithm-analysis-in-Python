#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/23


class Node(object):
    def __init__(self, element=-1, l_child=None, r_child=None):
        self.element = element
        self.l_child = l_child
        self.r_child = r_child


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, element):
        node = Node(element)
        if self.root is None:
            self.root = node
        else:
            queue_ = list()
            queue_.append(self.root)
            while queue_:
                cur = queue_.pop(0)
                if cur.l_child is None:
                    cur.l_child = node
                    return
                elif cur.r_child is None:
                    cur.r_child = node
                    return
                else:
                    queue_.append(cur.l_child)
                    queue_.append(cur.r_child)

    def depth_travel(self, root_in):
        if root_in is None:
            return
        print(root_in.element, end=', ')
        self.depth_travel(root_in.l_child)
        self.depth_travel(root_in.r_child)

    @staticmethod
    def breadth_travel(root_in):
        if root_in is None:
            return
        queue = list()
        queue.append(root_in)
        while queue:
            cur = queue.pop(0)
            print(cur.element, end=', ')
            if cur.l_child is not None:
                queue.append(cur.l_child)
            if cur.r_child is not None:
                queue.append(cur.r_child)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    print('breadth travel:')
    tree.breadth_travel(tree.root)
    print('\ndepth travel:')
    tree.depth_travel(tree.root)
