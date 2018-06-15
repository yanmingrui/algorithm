def sort_max(arr, kth_number):
    det = arr[0]
    arr1 = []
    arr2 = []
    
    for i in range(1, len(arr)):
        if(arr[i] < det):
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
    if(len(arr1) < kth_number):
        if(len(arr1) == kth_number - 1):
            return det
        else:
            #Notice:
            #if the following clause lacks key word "return", it will return none
            #the recursive is stack, so the whole process is :sort_max(arr1 or arr2, kth_number) -> sort_max(arr1 or arr2, kth_number)......
            #and last find the break point, such as return 5 and ->  sort_max(arr1 or arr2, kth_number) ->  sort_max(arr1 or arr2, kth_number)
            #Notice, there is no return value here, so return None
            return sort_max(arr2, kth_number - 1 - len(arr1))
    else:
        return sort_max(arr1, kth_number)
