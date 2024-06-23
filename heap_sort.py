#function for correcting a single node which violates the max_heap property
def max_heapify(arr,i,length):
    left = 2* i + 1
    right = left + 1
    largest = i
    if left < length and arr[left] > arr[largest]:
        largest = left
    if right < length and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i],arr[largest]
        arr = max_heapify(arr,largest,length)
    return arr


#function for creating a max_heap from the normal arr
def built_max_heap(arr,length):
    for i in range(length//2,-1,-1):
        arr = max_heapify(arr,i,length)
    return arr

#function to sort the array from the max_heap
def heap_sort(arr):
    size = len(arr)
    for i in range(size):
        arr[0],arr[size-1] = arr[size-1],arr[0]
        size -= 1
        arr = max_heapify(arr,0,size)
    return arr

#function to place the inserted element at right position according to the max_heap property
def bottom_up_heapify(arr,i):
    while i > 0 and arr[i] > arr[i//2]:
        arr[i],arr[i//2] = arr[i//2],arr[i]
        i = i//2
#code to insert new element into heap
def insert(arr,x):
    arr.append(x)
    bottom_up_heapify(arr,len(arr)-1)


arr = list(map(int,input().split()))
print(arr)
max_heap = built_max_heap(arr,len(arr))
print(max_heap)
insert(max_heap,int(input("enter a nnumber to insert into max_heap")))
print(max_heap)
sorted_arr = heap_sort(list(max_heap))
print(sorted_arr)
