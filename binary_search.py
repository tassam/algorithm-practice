
def binary_search(data, value):
    left = 0
    right = len(data) -1
    
    while left <= right:
        middle = (left + right) // 2
        if data[middle] == value:
            return middle 
        elif data[middle] <= value:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1

data = [10,20,30,40,50,60,70,80,90]
print(binary_search(data, 70))

