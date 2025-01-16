# Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array.

arr = [2, 56, 67, 45, 67, 78, 100, 1]

k = int(input("Enter the term 'k': "))

if (k > 0 and k <= len(arr)):
    arr.sort()
    print (f"The {k}th smallest term is {arr[k-1]}.")

else :
    raise ValueError(f"Invalid input: 'k' should be between 1 and the size of the array ({len(arr)}).")