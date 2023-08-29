def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

def selectionsort(arr):
    size=len(arr)
    for step in range(size):
        minidx=step
        for i in range(step+1,size):
            if arr[i]<arr[minidx]:
                minidx=i
        arr[step],arr[minidx]=arr[minidx],arr[step]

def insertionsort(arr):
    for i in range(1,len(arr)):
        key,j=arr[i],i-1
        while j>=0 and key<arr[j]:
            arr[j+1],j=arr[j],j-1
        arr[j+1]=key