# coding=utf-8

def select_sort(alist):
    n = len(alist)
    for j in range(1,n):  # j为次数，开始为第一次，共执行n-1次
        min_index = (j-1)
        for i in range(j,n):  # i为要比较的下标，比较到最后一位，下标为n-1
            if alist[min_index] > alist[i]:
                min_index = i
        # alist[j-1] = alist[min_index]  # 这样每次就把数丢了
        alist[j-1], alist[min_index] = alist[min_index], alist[j-1]

def main():
    alist = [3,6,65,343,15,25,8,56,4,5,7,3,73]
    print alist
    select_sort(alist)
    print alist

if __name__ == "__main__":
    main()