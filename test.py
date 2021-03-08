n = 5
data = [8, 5, 4, 7, 2]

def quick_sort(start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if right < left:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]
    quick_sort(start, right-1)
    quick_sort(right+1, end)

quick_sort(0, n-1)

for x in data:
    print(x)