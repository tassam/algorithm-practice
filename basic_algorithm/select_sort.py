
def selection_sort(a, n):
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        
        a[i], a[min_index] = a[min_index], a[i]

        print(*a)

n = int(input())
a = list(map(int, input().split()))
ccccccc
selection_sort(a, n)


