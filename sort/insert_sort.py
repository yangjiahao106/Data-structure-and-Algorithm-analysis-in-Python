#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/22


def insert_sort(a_list):
    for i in range(1, len(a_list)):
        for j in range(0, i):
            if a_list[i] < a_list[j]:
                a_list.insert(j, a_list[i])
                a_list.pop(i+1)
                break


def insert_sort2(a_list):
    for i in range(1, len(a_list)):
        for j in range(i, 0, -1):
            if a_list[j] < a_list[j-1]:
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
            else:
                break

if __name__ == '__main__':
    ll = [3, 2, 4, 1, 3, 6, 9, 0]
    print(ll)
    insert_sort2(ll)
    print(ll)
