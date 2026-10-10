import random
from timeit import default_timer as timer
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break

def generate_array(size):
    return [random.randint(1,1_000_000) for _ in range(size)]

def measure_sorting_time():
    sizes = [10000, 25000, 50000, 100000]
    for size in sizes:
        original_array=generate_array(size)
        bubble_arr=list(original_array)
        start=timer()
        bubble_sort(bubble_arr)
        end=timer()
        time=(end-start)*1000
        print(f"Running time for Bubble Sort is {time:.2f} ms")

if __name__ == "__main__":
    measure_sorting_time()