#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/23

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def merge_sort(a_list):
    n = len(a_list)
    if n <=1:
        return a_list
    left = merge_sort(a_list[:n//2])
    right = merge_sort(a_list[n//2:])
    result = merge(left, right)
    return result

if __name__ == '__main__':
    ll = [6, 5, 7, 3, 4, 8, 0]
    print(ll)
    sorted = merge_sort(ll)
    print(sorted)



