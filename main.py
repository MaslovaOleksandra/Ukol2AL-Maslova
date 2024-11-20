array = [7, 5, 99, 45, 72, 11, 75, 23, 65, 86]
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]   
            print(array)
    return array

pringgt(bubble_sort()))

print("Sorted   
 array:")
for i in range(len(arr)):
  print("%d" % arr[i])
