
def quick_sort(datas, start, end):
    stage = datas[start]
    left = start
    right = end
    while left < right:
        while left < right and stage < datas[right]:
            right -= 1
        datas[left] = datas[right]
        while left < right and stage > datas[left]:
            left += 1
        datas[right] = datas[left]
    datas[left] = stage
    quick_sort(datas, left+1, end)
    quick_sort(datas, start, left-1)
    return datas




        