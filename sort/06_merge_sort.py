# coding=utf-8

def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    # 拆分
    mid = n / 2
    lift_list = merge_sort(alist[ :mid])
    right_list = merge_sort(alist[mid: ])
    # 排序并合并
    lpointer, rpointer = 0, 0
    merge_list = []
    while (lpointer < len(lift_list)) and (rpointer < len(right_list)):
        if lift_list[lpointer] <= right_list[rpointer]:
            merge_list.append(lift_list[lpointer])
            lpointer += 1
        else:
            merge_list.append(right_list[rpointer])
            rpointer += 1
    merge_list += (lift_list[lpointer: ] + right_list[rpointer: ])
    return merge_list

def main():
    alist = [3, 6, 65, 343, 15, -5, 25, 8, 56, 4, -34, -5, 7, 3, 73, 0]
    print alist
    alist_sort = merge_sort(alist)
    print alist_sort


if __name__ == "__main__":
    main()

