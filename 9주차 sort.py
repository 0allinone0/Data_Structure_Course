def selection_sort(l):
    for i in range(len(l)-1):
        least = i
        for j in range(i, len(l)):
            if l[least] >= l[j]:
                least = j
    
        tmp = l[i]
        l[i] = l[least]
        l[least] = tmp
    return l

a = [2, 3, 1,6,7,5]
s_a = selection_sort(a)
print(s_a)


def insert_sort(l):
    n = len(l)
    for i in range(1,n):
        compare =  l[i]
        j = i-1
        while j>=0 and l[j]>compare:
            l[j+1] = l[j]
            j -= 1

        l[j+1] = compare
    return l

b = [2,5,1,4,6]
s_b = insert_sort(b)
print(s_b)


def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

a = [2, 3, 1, 6, 7, 5]
print(bubble_sort(a))


######
#이진 탐색
def binary_search(l,key):
    n = len(l)
    low = 0
    high = n
    while (low <= high):
        middle = (high+low)//2

        if key == l[middle]:
            return middle
        elif key < l[middle]:
            high = middle - 1
        elif key >l[middle]:
            low = middle + 1
        else:
            print("찾는 값 없습니다.")

a = [1,2,3,4,5,6,7,8,10]

print(binary_search(a,9))
