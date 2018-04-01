# coding=utf-8

def insert_sort(alist):
    n = len (alist)
    for turn in range(1, n): # 执行第几次，共执行n-1次
        while turn:
            if alist[turn] < alist[turn-1]:
                alist[turn], alist[turn-1] = alist[turn-1], alist[turn]
            turn -= 1

def main():
    alist = [3, 6, 65, 343, 15, 25, 8, 56, 4, 5, 7, 3, 73]
    print alist
    insert_sort(alist)
    print alist


if __name__ == "__main__":
    main()