# coding=utf-8

def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    key = alist[first]
    low = first
    high = last
    while low < high:
        while alist[high] >= key:
            # >=是为了把与key值相同的都放到右边,虽然不加=也能完成排序
            high -= 1
        alist[low] = alist[high]
        while (low < high) and (alist[low] < key):
            # 加上low < high保证两者重合时low不再移动
            low += 1
        alist[high] = alist[low]
    # 退出循环说明此时 low == high
    alist[low] = key
    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)

def main():
    alist = [3, 6, 65, 343, 15, -5, 25, 8, 56, 4, -34, -5, 7, 3, 73, 0]
    print alist
    quick_sort(alist, 0, len(alist)-1)
    print alist


if __name__ == "__main__":
    main()
