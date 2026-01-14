


# In selection sort , we first take first elem traverse the array, replace the min with that,
# go to next traverse and replace the second smallest with the second elem 
# this way travel the whole array till n-1 because don't need to do so 
#  time complexity is n squre 

def selectionSort(arr):
    for i in range(0, len(arr) - 1,1):
        min = i
        for j in range(i, len(arr), 1):
            if(arr[j] < arr[min]):
                min = j
        swap(i,min,arr)
    
    return arr

# BUBBLE SORT --> In bubble sort we compare ajducent values in a single loop and swap 
# till the greater elem is at the end. In a single loop when we compare [3,2,1,6,5] 
# 6 will be always at the end of the array. then we repeat the procedure but we don't 
# need to include last elem, then second last elem and so on..

def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i,1):
            if(arr[j] > arr[j+1]):
                swap(j,j+1,arr)
    return arr





def swap(a: int,b: int,arr):
    arr[a], arr[b] = arr[b], arr[a]
    return arr 





if __name__ == '__main__':
    arr =[3,2,1,6,5]
    c = bubbleSort(arr)
    print(c)
