
import time

# Sorting program
def sort_data(data):
    return sorted(data)

# Generate datasets
partially_sorted_data = list(range(1, 500001)) + list(range(1000000, 500000, -1))  # First half sorted, second half reversed
reversed_data = list(range(1000000, 0, -1))  # Completely reversed dataset

# Sort partially sorted data
start_time = time.time()
sorted_partially = sort_data(partially_sorted_data)
end_time = time.time()
print(f"Sorting partially sorted data took: {end_time - start_time:.5f} seconds")

# Sort reversed data
start_time = time.time()
sorted_reversed = sort_data(reversed_data)
end_time = time.time()
print(f"Sorting reversed data took: {end_time - start_time:.5f} seconds")

