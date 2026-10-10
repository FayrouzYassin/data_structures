import random
from timeit import default_timer as timer
def selectionsort (arr):
    n=len(arr);
    for i in range(n):
        min=i
        for j in range(n):
            if(arr[min]<arr[j]):
                temp = arr[j]
                arr[j] = arr[min]
                arr[min] = temp
            else:
                j+=1

def generate_array(size):
    return [random.randint(1,1_000_000) for _ in range(size)]

def measure_sorting_time():
    sizes = [10000, 25000, 50000, 100000]
    for size in sizes:
        original_array=generate_array(size)
        selection_arr=list(original_array)
        start=timer()
        selectionsort(selection_arr)
        end=timer()
        t=(end-start)*1000
        print(f"Running time for selection Sort with array of size {size} is {t:.2f} ms")

measure_sorting_time()

