#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/22


class Node(object):
    """a class about the element of the chain table"""
    def __init__(self, element, nex=None):
        self.element = element
        self.next = nex


class SingleChainTable(object):
    """a class about single chain table
        :param node
    """
    def __init__(self, node=None):
        self.head = node
        if self.head is not None:
            self.head.next = self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        cursor = self.head
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.next
            if cursor == self.head:
                break
        return count

    def append(self, element):
        """add a node in the end of the chain table"""
        node = Node(element)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            cursor = self.head
            while cursor.next != self.head:
                cursor = cursor.next
            cursor.next = node
            node.next = self.head

    def add(self, element):
        """add a node in the begin of the chain table"""
        node = Node(element)
        if self.head is None:
            self.head = node
            node.next = node
        else:
            cursor = self.head
            while cursor.next != self.head:
                cursor = cursor.next
            cursor.next = node
            node.next = self.head
            self.head = node

    def insert(self, pos, element):
        """inset a node in the chain
            pos: the inserted position
        """
        if self.head is None:
            self.append(element)
            return None
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
            cursor.next = node

    def remove(self, element):
        """remove a node which element == element"""
        if self.head is None:
            return

        if self.head.element == element:  # is the first element of the chain is element
            if self.length() == 1:
                self.head = None
                return
            cursor = self.head
            while cursor.next != self.head:
                cursor = cursor.next
            self.head = self.head.next
            cursor.next = self.head
            return

        cursor = self.head
        while cursor.next != self.head:
            if cursor.next.element == element:
                cursor.next = cursor.next.next
                return
            cursor = cursor.next

    def search(self, element):
        """find element is in the chain table
            :return True or False
        """
        cursor = self.head
        while cursor is not None:
            if cursor.element == element:
                return True
            cursor = cursor.next
            if cursor == self.head:
                return False

    def travel(self):
        """print all the element of the chain table"""
        result = []
        cursor = self.head
        while cursor is not None:
            result.append(cursor.element)
            if cursor.next == self.head:
                break
            cursor = cursor.next
        print(result)

if __name__ == '__main__':
    ll = SingleChainTable()
    ll.travel()
    ll.append(3)
    ll.append(4)
    ll.add(1)
    ll.insert(1, 2)
    ll.travel()
    ll.remove(4)
    ll.travel()
    if ll.search(2):
        print('have')
