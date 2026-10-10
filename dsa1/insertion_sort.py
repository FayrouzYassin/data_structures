import random
from timeit import default_timer as timer

def insert_sort(a):
    for i in range(1, len(a)):
        j = i - 1
        temp = a[i]
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = temp

def generate_array(size):
    return [random.randint(1, 1_000_000) for _ in range(size)]

def measure_sorting_time():
    sizes = [10000, 25000, 50000, 100000]
    for size in sizes:
        original_array = generate_array(size)
        insertion_arr = list(original_array)   # fresh copy
        start = timer()
        insert_sort(insertion_arr)
        end = timer()
        ms = (end - start) * 1000
        print(f"Size {size}: Running time for Insertion Sort is {ms:.2f} ms")

if __name__ == "__main__":
    measure_sorting_time()