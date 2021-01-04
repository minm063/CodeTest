def solution(arr):
    if len(arr) <=1 : 
        arr[0]=-1
    else: 
        c=sorted(arr)
        arr.remove(c[0])
    return arr
