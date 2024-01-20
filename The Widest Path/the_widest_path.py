def solution(x, y, n):
    quick_sort(x, 0, n - 1)
    max_length = 0
    for i in range(n - 1):
        width = x[i + 1] - x[i]
        if width > max_length:
            max_length = width
    return max_length

def quick_sort(x, startIdx, endIdx):
    start = startIdx
    end = endIdx
    mid = round((startIdx + endIdx) / 2)
    #print("Mid: ", mid)
    if mid == startIdx or mid == endIdx:
        return
    while startIdx < mid and endIdx > mid:
        if x[startIdx] <= x[mid]:
            startIdx = startIdx + 1
        if x[endIdx] > x[mid]:
            endIdx = endIdx - 1
        #swap
        #print("starIDX", startIdx)
        #print("endIDX", endIdx)
        temp = x[startIdx]
        x[startIdx] = x[endIdx]
        x[endIdx] = temp
        #print("X ", x)
    quick_sort(x, start, mid)
    quick_sort(x, mid + 1, end)
    

x = [1, 8, 7, 3, 4, 1, 8]
y = [6, 4, 1, 8, 5, 1, 7]
length = solution(x, y, 7)
print("Lenth: ", length)
quick_sort(x, 0, 6)
print("Array after sorting ", x)