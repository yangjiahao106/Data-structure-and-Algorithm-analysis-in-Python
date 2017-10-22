#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/21


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
        return count

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

    def add(self, element):
        """add a node in the begin of the chain table"""
        node = Node(element)
        node.next = self.head
        self.head = node

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
            cursor.next = node

    def remove(self, element):
        """remove a node which element == element"""
        if self.head.element == element:
            self.head = self.head.next
            return None
        cursor = self.head
        while cursor.next is not None:
            if cursor.next.element == element:
                cursor.next = cursor.next.next
                break
            else:
                cursor = cursor.next

    def removes(self, element):
        """remove all the node which element == element"""
        if self.is_empty():
            return None
        while self.head.element == element:
            self.head = self.head.next
            if self.is_empty():
                return None

        cursor = self.head
        while cursor.next is not None:
            if cursor.next.element == element:
                cursor.next = cursor.next.next
            else:
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
        return False

    def travel(self):
        """print all the element of the chain table"""
        cursor = self.head
        result = []
        while cursor is not None:
            result.append(cursor.element)
            cursor = cursor.next
        print(result)

if __name__ == '__main__':
    ll = SingleChainTable()
    ll.append(0)
    ll.append(0)
    ll.insert(0, 0)
    ll.insert(4, 8)
    ll.travel()
    print(ll.length())
    ll.remove(8)
    print('remove')
    ll.travel()
