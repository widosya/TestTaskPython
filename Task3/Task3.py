import math


def introSort(a, d, start, end):
    n = end - start
    if n <= 1:
        return
    elif d == 0:
        introHS(a, start, end)
    else:
        p = partition(a, start, end)
        introSort(a, d-1, start, p)
        introSort(a, d-1, p+1, end)


def introHS (a, start, end):
    b = a[start:end]
    heapSort(b)
    for i in range(0,len(b)):
        a[start+i] = b[i]


def heapSort (a):
    END = len(a)
    for k in range (math.floor(END/2) - 1, -1, -1):
        heapify(a, END, k)

    for k in range(END, 1, -1):
        swap(a, 0, k-1)
        heapify(a, k-1, 0)


def partition(a, start, end):
    x = a[end-1]
    i = start-1
    for j in range(start, end-1):
        if a[j] <= x:
            i=i+1
            swap(a, i, j)
    swap(a, i+1, end-1)
    return i+1


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def heapify(a,iEnd,iRoot):
    iL = 2*iRoot + 1
    iR = 2*iRoot + 2
    if iR < iEnd:
        if a[iRoot] >= a[iL] and a[iRoot] >= a[iR]:
            return

        else:
            if a[iL] > a[iR]:
                j = iL
            else:
                j = iR
            swap(a, iRoot, j)
            heapify(a, iEnd, j)

    elif iL < iEnd:
        if a[iRoot] >= a[iL]:
            return
        else:
            swap(a, iRoot, iL)
            heapify(a,iEnd,iL)

    else:
        return