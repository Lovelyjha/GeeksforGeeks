def transitionPoint(arr,n):
    for i in range(n):
        if arr[i]==1:
            return i

    return -1
