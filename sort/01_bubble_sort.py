# coding=utf-8

def bubble_sort(alist):
    n = len(alist)
    for j in range(1,n):
        count = 0
        for i in range(n-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        # if count == 0:
        if 0 == count:
            return
def main():
    alist = [3,6,65,343,15,25,8,56,4,5,7,3,73]
    print alist
    bubble_sort(alist)
    print alist

if __name__ == "__main__":
    main()
