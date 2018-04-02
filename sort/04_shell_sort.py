# coding=utf-8

def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n / 2  # 定义增量gap
    while gap >= 1:  # 增量减为1时执行最后一次插入排序
        # 插入排序
        for i in range(gap, n):  # 算法核心，每次循环让分组进行插入排序\
            # 而不是让一个分组排序完再排下一分组
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                else:
                    break
                i -= gap
        gap /= 2  # 减少增量

def main():
    alist = [3, 6, 65, 343, 15, -5, 25, 8, 56, 4, -34, 5, 7, 3, 73, 0]
    print alist
    shell_sort(alist)
    print alist


if __name__ == "__main__":
    main()