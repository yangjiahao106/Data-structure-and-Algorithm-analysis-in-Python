#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/22


def select_sort(a_list):
    for i in range(0, len(a_list)-1):
        min_index = i
        for j in range(i+1, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]

if __name__ == '__main__':
    ll = [1, 5, 3, 6, 2, 4, 0]
    print(ll)
    select_sort(ll)
    print(ll)
