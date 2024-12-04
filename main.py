import random
def pole():
  return [random.randint(0, 100) for _ in range(10)]
array = pole(10)
print(array)
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
            print(array)
    return array

print(bubble_sort())
