#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/20
from queue import Queue


class Node(object):
    def __init__(self, val, parent=None):
        self.parent = parent
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = Node(val)
        if self.empty():
            self.root = node
        else:
            parent = None
            curr_node = self.root

            while True:
                if curr_node is not None:
                    parent = curr_node

                    if node.val > curr_node.val:
                        curr_node = curr_node.right
                    else:
                        curr_node = curr_node.left
                else:
                    if node.val > parent.val:
                        parent.right = node
                        node.parent = parent
                    else:
                        parent.left = node
                        node.parent = parent
                    break

    def delete(self, val, curr_node):
        if curr_node is None:
            print('not found element')
            return

        if val < curr_node.val:
            self.delete(val, curr_node.left)
        elif val > curr_node.val:
            self.delete(val, curr_node.right)

        else:  # find element
            if curr_node.left and curr_node.right:  # tow child
                temp = self.findMin(curr_node.right)
                curr_node.val = temp
                self.delete(temp, curr_node.right)

            else:  # one or zero child
                if curr_node.parent is None:  # 如果删除的是根节点
                    self.root = curr_node.left or curr_node.right

                elif curr_node.left is None:
                    if curr_node.parent.left == val:
                        curr_node.parent.left = curr_node.right
                    else:
                        curr_node.parent.right = curr_node.right
                else:
                    if curr_node.parent.left == val:
                        curr_node.parent.left = curr_node.left
                    else:
                        curr_node.parent.right = curr_node.left

    def findMin(self, curr_node):
        if curr_node:
            if not curr_node.left:
                return curr_node.val
            else:
                return self.findMin(curr_node.left)

    def dfs(self, curr_node):
        if curr_node is not None:
            print(curr_node.val, end=' ')
            self.dfs(curr_node.left)
            self.dfs(curr_node.right)

    def bfs(self, curr_node):
        if curr_node is None:
            return
        q = Queue()
        q.put(curr_node)
        while not q.empty():
            cur = q.get()
            print(cur.val, end=' ')
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)

    def empty(self):
        if self.root is None:
            return True
        return False


if __name__ == '__main__':
    tree = BinarySearchTree()
    vals = [1, 2, 3, 4, 5]
    for v in vals:
        tree.insert(v)

    tree.dfs(tree.root)
    print('')
    tree.bfs(tree.root)
    tree.delete(1, tree.root)
    print('')
    tree.bfs(tree.root)
