#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/23


def quick_sort(a_list, start, end):
    if start >= end:
        return
    print(a_list)
    low = start
    high = end
    mid_value = a_list[start]

    while low < high:
        while low < high and a_list[high] >= mid_value:
                high -= 1
        a_list[low] = a_list[high]

        while low < high and a_list[low] <= mid_value:
            low += 1
        a_list[high] = a_list[low]

    a_list[low] = mid_value
    quick_sort(a_list, start, low-1)
    quick_sort(a_list, low+1, end)


if __name__ == '__main__':
    ll = [6, 5, 7, 3, 2, 1, 3, 7, 2, 0, 9]
    print(ll)
    quick_sort(ll, 0, len(ll)-1)
    print(ll)

