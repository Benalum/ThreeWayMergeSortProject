import ThreeWayMergeSort as MST
import random
import timeit

def main():
    random.seed(42)

# Loop over different data sizes
for i in range(26, 31):

    data_size = 2 ** i
    print("Data Size: " , data_size)
    if(i > 24):
        number_of_sections = 2**(i - 24)
        section_length = data_size // number_of_sections
        # Generate test data
        integers = [random.randint(0, 1048576) for _ in range(section_length)]
        floats = [random.uniform(0.0, 0.9) for _ in range(section_length)]
        start_time = timeit.default_timer()
        #loop through sections at a time
        for z in range(0, number_of_sections):
            MST.three_way_merge_sort_initialization(integers.copy())
            print(z)
        time_taken_integers = timeit.default_timer() - start_time

        # Output the results
        print(f"Three Way Merge Sort: Time taken for integers: {time_taken_integers:.6f} seconds")

        # Time sorting for floats
        start_time = timeit.default_timer()
        for z in range(0, number_of_sections):
            MST.three_way_merge_sort_initialization(floats.copy())
            print(z)
        # End float timer
        time_taken_floats = timeit.default_timer() - start_time

        # Output the results
        print(f"Three Way Merge Sort: Time taken for floats: {time_taken_floats:.6f} seconds")

    else:
        # Generate test data
        integers = [random.randint(0, 1048576) for _ in range(data_size)]
        floats = [random.uniform(0.0, 0.9) for _ in range(data_size)]

        # Time sorting for integers
        start_time = timeit.default_timer()
        MST.three_way_merge_sort_initialization(integers.copy())
        time_taken_integers = timeit.default_timer() - start_time

        # Time sorting for floats
        start_time = timeit.default_timer()
        MST.three_way_merge_sort_initialization(floats.copy())
        time_taken_floats = timeit.default_timer() - start_time

        # Output the results
        print(f"Three Way Merge Sort: Time taken for integers: {time_taken_integers:.6f} seconds")
        print(f"Three Way Merge Sort: Time taken for floats: {time_taken_floats:.6f} seconds")
