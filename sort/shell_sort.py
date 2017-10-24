#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/22


def shell_sort(a_list):
    gep = len(a_list)//2
    while gep >= 1:
        for g in range(0, gep):
            for i in range(gep+g, len(a_list), gep):
                for j in range(i, 0, -gep):
                    if a_list[j] < a_list[j-gep]:
                        a_list[j], a_list[j-gep] = a_list[j-gep], a_list[j]
                    else:
                        break
        gep = gep//2


def shell_sort2(a_list):
    """优化后"""
    gep = len(a_list)//2
    while gep >= 1:
        for i in range(gep, len(a_list)):
            for j in range(i, 0, -gep):
                if a_list[j] < a_list[j-gep]:
                    a_list[j], a_list[j-gep] = a_list[j-gep], a_list[j]
                else:
                    break
        gep = gep//2


if __name__ == '__main__':
    ll = [6, 5, 4, 3, 2, 1, 3, 6, 2, 0, 9]
    print(ll)
    shell_sort(ll)
    print(ll)
