# geeksforgeeks.com helped a lot

def three_way_merge_sort(arr, start_location_size, one_third_size_location, two_third_size_location,
                            end_location_size, d_arr):
    #  Get the index location for the 0/3 , 1/3, 2/3, 3/3.
    #  The code needs to keep the original input sent to it as well as alter them so placing them as a variable allows
    #  the code to be able to keep the original index's and also alter the ones saved as i,j,k,l/.
    i = start_location_size
    j = one_third_size_location
    k = two_third_size_location
    l = start_location_size

    #  Sorting first iteration
    #  This while loop will perform many checks with if statements.  It will iterate through the start index to 1/3 * size
    #  1/3 * size to 2/3 * size and 2/3 * size to the end index.  It will iteratively check to see which one is less than
    #  the rest of them.  When it determines which one is the minimum of the three it will take that number and place it in
    #  the array d_arr based on the l location which starts of at the starting index and is iterated every time a number is
    #  placed into the array.
    while i < one_third_size_location and j < two_third_size_location and k < end_location_size:
        #  Check to see if the value at i is less than j
        if arr[i] < arr[j]:
            #  If previous if statement holds then check if value at index i is less than value at index k
            #  If so then add the value at index i in arr to d_arr at index l
            #  Then increment i to check the next value for i in arr
            #  Then increment l for the next placement into d_arr
            if arr[i] < arr[k]:
                d_arr[l] = arr[i]
                l += 1
                i += 1
            #  If previous if statement does not hold then the number in the array arr at index i is greater than
            #  the number in the array arr at index k.
            #  Take the value the index k from array arr and place it into d_arr at index l.
            #  Then increment l for the next placement into d_arr
            #  Then increment k to check the next value for k in arr
            else:
                d_arr[l] = arr[k]
                l += 1
                k += 1
        #  if statement fails then we know index j of array arr is less than index i of array arr
        else:
            #  Checks to see if the value at index j in array arr is less than the value at index k in array arr
            #  If so then place the value into array d_arr at index l
            #  Then increment l for the next placement into d_arr
            #  Then increment j to check the next value for j in arr
            if arr[j] < arr[k]:
                d_arr[l] = arr[j]
                l += 1
                j += 1
            #  if previous if statement failed then we know the value at index j in array arr is greater than index k in array arr
            #  Then the value for the array d_arr at index l will now become the value in array arr at index k
            #  Then increment l for the next placement into d_arr
            #  Then increment k to check the next value for k in arr.
            else:
                d_arr[l] = arr[k]
                l += 1
                k += 1

    #  Sorting second iteration: Remaining values for first and second range.
    while i < one_third_size_location and j < two_third_size_location:
        #  If the value at index i in the array arr is less than the value at index j of the array
        #  Then the new value for d_arr at index l will be the value from array arr at index i
        #  Then increment i for the next value for i in arr
        #  Then increment l for the next placement into d_arr
        if arr[i] < arr[j]:
            d_arr[l] = arr[i]
            i += 1
            l += 1
        #  If previous statement is false then there is only one other outcome
        #  The value in the array d_arr at index l will now become the value of the array arr at index j
        #  Then increment l for the next placement into d_arr
        #  Then increment j for the next value for i in arr
        else:
            d_arr[l] = arr[j]
            l += 1
            j += 1

    #  Sorting third iteration: Remaining values second to third range.
    while j < two_third_size_location and k < end_location_size:
        #  If the value at the index j in the array arr is less than the value at the index k in the array arr then
        #  the new value for d_arr at the index l will be the value from the array arr at the index j
        #  Then increment j for the next value for j in arr
        #  Then increment l for the next placement into d_arr
        if arr[j] < arr[k]:
            d_arr[l] = arr[j]
            j += 1
            l += 1
        #  If the previous statement is false then there is only one other outcome
        #  The value in the array d_arr at index l will now become the value of the array arr ar index k
        #  Then increment k for the next value for k in arr
        #  Then increment l for the next placement into d_arr
        else:
            d_arr[l] = arr[k]
            l += 1
            k += 1

    #  Sorting fourth iteration:  Remaining values for third and first range.
    while i < one_third_size_location and k < end_location_size:
        #  If the value at the index i in the array arr is less than the value at the index k in the array arr then
        #  The new value for d_arr at the index l will be the value from the array arr at the index i
        #  Then increment i for the next value for i in arr
        #  Then increment l for the next placement into d_arr
        if arr[i] < arr[k]:
            d_arr[l] = arr[i]
            i += 1
            l += 1
        #  If the previous if statement is false then there is only one other outcome
        #  The value in the array d_arr at index l will now become the value of the array arr at index k
        #  Then increment l for the next placement into d_arr
        #  Then increment k for the next value for k in arr
        else:
            d_arr[l] = arr[k]
            l += 1
            k += 1
    return arr


#  Merge function
def three_way_merge_sort_split(d_arr, start_location_size, end_location_size, arr):
    size = end_location_size - start_location_size

    #  Check size return if < 2
    #  If the size is less than two, then the operation is complete and we would just return
    if end_location_size - start_location_size < 2:
        return

    #  Since this is three way merge sort we must split the array into 3 seperate sections
    #  We know the first and last location based on the size of the array
    #  To get the first point take the size of the array and divide it by 3 and add the start location
    #  This is incase the start is not 0
    #  To get the second point we do 2/3 * size + start size/index and add 1 to prevent maximum recursion error.
    one_third_size_location = start_location_size + (size // 3)
    two_third_size_location = start_location_size + 2 * (size // 3) + 1  # Prevents maximum recursion doing + 1

    #  Recursively split the array.
    #  Parameter one is the array
    #  Parameter two is where the start for the section that will be split
    #  Parameter three is the end location for the section that will be split
    #  Parameter four is the array
    three_way_merge_sort_split(arr, start_location_size, one_third_size_location, d_arr)
    three_way_merge_sort_split(arr, one_third_size_location, two_third_size_location, d_arr)
    three_way_merge_sort_split(arr, two_third_size_location, end_location_size, d_arr)

    #  Merge to create the sorted array
    #  Parameter one is the array
    #  Parameter two is the starting index of the array
    #  Parameter three is the one-third index location
    #  Parameter four is the two-third index location
    #  Parameter five is the end index
    #  Parameter six is the array
    three_way_merge_sort(arr, start_location_size, one_third_size_location, two_third_size_location,
                            end_location_size, d_arr)

    return d_arr


#  Check if size exists, create duplicate array
def three_way_merge_sort_initialization(arr):
    size = len(arr)

    # If array size is zero it will return nothing
    if size == 0:
        return

    # Create a duplicate array
    d_arr = arr.copy()

    #  Run the first function for three way merge sort which would be splitting the array into 1/3 sections.
    #  The first parameter is a copy of the original array
    #  The second parameter is the index of the starting location
    #  The third parameter is the size of the array that will have 3 way merge sort performed on it
    #  The last parameter is the original array
    #  One possible way to shorten this would be to get rid of 0 and hard code it into the function
    #  Another would be to get the size of the array in the function to prevent the need to send it this information
    three_way_merge_sort_split(d_arr, 0, size, arr)
