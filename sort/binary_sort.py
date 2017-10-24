#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/23


def binary_search(a_list, item):
    """binary search use recursion"""
    if len(a_list) < 1:
        return False
    else:
        mid = len(a_list)//2
        if item == a_list[mid]:
            return True
        elif item < a_list[mid]:
            return binary_search(a_list[:mid], item)
        elif item > a_list[mid]:
            return binary_search(a_list[mid + 1:], item)

if __name__ == '__main__' :
    ll = [1, 3, 4, 6, 2, 7, 8]
    if binary_search(ll, 0):
        print('Found')
    else:
        print('Not found')
