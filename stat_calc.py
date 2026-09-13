def qsort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return qsort(left) + mid + qsort(right)

def get_median(arr):
    s_arr = qsort(arr)
    n = len(s_arr)
    
    if n % 2 == 0:
        return (s_arr[n//2 - 1] + s_arr[n//2]) / 2.0
    else:
        return s_arr[n//2]

data = [12.5, 4.1, 5.0, 3.2, 8.8, 7.1, 15.0, 2.4]
print(get_median(data))
