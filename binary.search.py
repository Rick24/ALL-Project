#Binary search algorithm

def binary_search(A, size, target):
    low = 0
    high = size
    while(low + 1 < high):
        test = (low + high)/2
        if(A[test]> target):
            high = test
        else:
            low = test
    if(A[low] == target):
        return low
    else:
        return -1
        

A = [2, 3, 6, 9, 10, 24]
