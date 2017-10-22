#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/21
from chain_talbe.single_chain_table import SingleChainTable


class Node(object):
    def __init__(self, element, prev=None, nex=None):
        self.element = element
        self.prev = prev
        self.next = nex


class DoubleChainTable(SingleChainTable):
    def __init__(self, node=None):
        super(DoubleChainTable, self).__init__(node)
    
    def add(self, element):
        node = Node(element)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def append(self, element):
        """add a node in the end of the chain table"""
        node = Node(element)
        if self.head is None:
            self.head = node
        else:
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = node
            node.prev = cursor

    def insert(self, pos, element):
        """inset a node in the chain
            pos: the inserted position
        """
        if pos <= 0:
            self.add(element)
        elif pos >= self.length():
            self.append(element)
        else:
            node = Node(element)
            cursor = self.head
            for i in range(pos-1):
                cursor = cursor.next
            node.next = cursor.next
            node.prev = cursor
            cursor.next.prev = node
            cursor.next = node

    def remove(self, element):
        """remove a node which element == element"""
        if self.head.element == element:
            self.head = self.head.next
            self.head.prev = None
            return None
        cursor = self.head
        while cursor.next is not None:
            if cursor.next.element == element:
                cursor.next = cursor.next.next
                if cursor.next is not None:
                    cursor.next.prev = cursor
                break
            else:
                cursor = cursor.next


if __name__ == '__main__':
    ll = DoubleChainTable()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.add(0)
    ll.travel()
    ll.insert(3, 8)
    ll.travel()
    ll.append(5)
    ll.remove(0)
    ll.travel()
    print(ll.head.element)
    print(ll.head.next.element)
    print(ll.head.next.next.element)
    print(ll.head.next.next.next.next.prev.element)
