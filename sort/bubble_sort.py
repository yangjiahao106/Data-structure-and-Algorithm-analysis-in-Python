#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/22

def bubble_sort(a_list):
    for i in range(len(a_list)-1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]


if __name__ == '__main__':
    ll = [1, 5, 3, 6, 2, 4, 9]
    print(ll)
    bubble_sort(ll)
    print(ll)
