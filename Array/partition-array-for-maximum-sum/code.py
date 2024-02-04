def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * n  # Initialize a dynamic programming array to store maximum sum up to each index

    for i in range(n):
        max_val = 0  # Initialize the maximum value in the current subarray
        for j in range(1, min(k, i + 1) + 1): # for take a limit to maximm k, and 
            max_val = max(max_val, arr[i - j + 1])  # Update max_val with the maximum element in the current subarray
            prev_sum = dp[i - j] if i - j >= 0 else 0  # Get the maximum sum from the previous subarray
            dp[i] = max(dp[i], prev_sum + max_val * j)  # Update dp[i] with the maximum sum considering the current element and previous subarray

    return dp[n - 1]  # Return the maximum sum achievable for the entire array

# Example usage:
arr1 = [1, 15, 7, 9, 2, 5, 10]
k1 = 3
print(maxSumAfterPartitioning(arr1, k1))  # Output: 84

arr2 = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
k2 = 4
print(maxSumAfterPartitioning(arr2, k2))  # Output: 83
