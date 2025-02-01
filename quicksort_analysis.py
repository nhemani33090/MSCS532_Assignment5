import random
import time

# Standard Quicksort using the middle element as the pivot
def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]  # Selecting middle element as the pivot
    smaller = [x for x in array if x < pivot]  
    equal = [x for x in array if x == pivot]  
    greater = [x for x in array if x > pivot]  

    return quicksort(smaller) + equal + quicksort(greater)

# Randomized Quicksort where the pivot is chosen randomly
def randomized_quicksort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)  # Choosing random pivot
    smaller = [x for x in array if x < pivot]  
    equal = [x for x in array if x == pivot]  
    greater = [x for x in array if x > pivot]  

    return randomized_quicksort(smaller) + equal + randomized_quicksort(greater)

# Function to calculate sorting execution time
def get_execution_time(sorting_function, dataset):
    start_time = time.time()
    sorting_function(dataset)
    return time.time() - start_time

# Creating test cases with different input types
test_sizes = [1000, 5000, 10000, 20000]
test_data = {
    "Random": [random.sample(range(1, 100000), size) for size in test_sizes],
    "Sorted": [list(range(size)) for size in test_sizes],
    "Reverse-Sorted": [list(range(size, 0, -1)) for size in test_sizes]
}

# Displaying execution time results
print(f"{'Data Type':<15}{'Size':<10}{'Quicksort Time (s)':<25}{'Randomized Time (s)':<25}")
print("=" * 75)

for data_type, test_cases in test_data.items():
    for index, dataset in enumerate(test_cases):
        quicksort_time = get_execution_time(quicksort, dataset.copy())  
        randomized_time = get_execution_time(randomized_quicksort, dataset.copy())  
        print(f"{data_type:<15}{test_sizes[index]:<10}{quicksort_time:<25.6f}{randomized_time:<25.6f}")
