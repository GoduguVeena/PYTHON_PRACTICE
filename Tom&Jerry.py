import heapq

def findKthLargest(nums, k):
    # Use a heap to find the Kth largest element
    return heapq.nlargest(k, nums)[-1]

if __name__ == '__main__':
    # Read the number of elements in the stream
    n = int(input().strip())
    # Read the value of K
    k = int(input().strip())
    # Read the stream of numbers
    arr = list(map(int, input().strip().split()))
    
    # Validate the input
    if len(arr) != n:
        raise ValueError("The number of elements in the array does not match N.")
    
    # Find and print the Kth largest element
    result = findKthLargest(arr, k)
    print(result)
