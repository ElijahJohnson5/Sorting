import time
import argparse
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]

    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted
def merge_sort(arr,l,r):
    if l < r:
        m = int((l+(r-1))/2)

        # Sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

    return arr


def merge_sort_help(arr):
    return merge_sort(arr, 0, len(arr) - 1)


def insertion_sort(arr):
    #loop through list and get the key set j equal to the previous
    #element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        #Loop from j to 0 for each item
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        #put the key in the right place after sorting all previous elements
        arr[j + 1] = key

    return arr

#Like insertion sort but only in pairs
def bubble_sort(arr):
    #do while loop, do the sort until no more swaps have occured
    while True:
        swaps = 0
        #loop through the list checking pairs of items, and swapping them
        #if needed
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1

        #exit while loop if no swaps occured
        if swaps == 0:
            break

    return arr


def counting_sort(arr):
    #create list to hold the sorted array
    temp_arr = [0] * len(arr)
    #create count list, keeps count of how many times a number occurs
    #has to be as long as the greatest value in original array
    c = [0] * (max(arr) + 1)
    #count how many occurences of each number
    for i in range(0, len(arr)):
        c[arr[i]] += 1
    #add the pervious count to the next count figuring out the position for
    #the value in the final array
    for i in range(1, len(c)):
        c[i] += c[i - 1]

    #get the value in the count array for the current value in the
    #original array and set it to the current value
    for i in range(0, len(arr)):
        temp_arr[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1

    return temp_arr


def main():
    #Create parser for command line arguments and add custom sort arguments
    parser = argparse.ArgumentParser(description='Sort an array using different sorting methods, defaults to merge sort')
    parser.add_argument('integers', metavar='ARR', nargs='+', type=int, help='Array to be sorted')
    parser.add_argument('-bubble', dest='sort',
                        help='Sorts using bubble sort', action='append_const',
                        const=bubble_sort)
    parser.add_argument('-counting', dest='sort',
                        help='Sorts using counting sort', action='append_const',
                        const=counting_sort)
    parser.add_argument('-insertion', dest='sort',
                        help='Sorts using insertion sort', action='append_const',
                        const=insertion_sort)
    parser.add_argument('-merge', dest='sort',
                        help='Sorts using merge sort', action='append_const',
                        const=merge_sort_help)

    #parser the args
    args = parser.parse_args()

    #if no sort was defined default to merge sort
    if not args.sort:
        args.sort = [merge_sort_help]

    #loop through all of the sort arguments
    #and sort the array with those sorting methods
    for f in args.sort:
        #print out the name of the sorting method
        if f == bubble_sort:
            print('Bubble sort')
        elif f == counting_sort:
            print('Counting sort')
        elif f == insertion_sort:
            print('Insertion sort')
        else:
            print('Merge sort')

        #Time how long each sort takes
        start_time = time.time()
        #Call the method stored in f and get the resulting array
        arr = f(args.integers)
        elapsed_time = time.time() - start_time
        #Print out the time taken and the sorted array
        print(f"Time taken = {elapsed_time}")
        print ("Sorted array is")
        print(arr)

if __name__ == '__main__':
    main()
