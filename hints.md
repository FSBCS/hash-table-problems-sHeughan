**Problem 1**
If three words are anagrams, what common key could we store to represent them in a hash table?

To convert a list to a string, we can use `''.join(someList)` to concatenate the elements of the list to the empty string.

**Problem 2**
Nothing fancy here!

**Problem 3**
Believe it or not, it is possible to do this with just one pass through the list! In the brute force solution (computing every subarray sum) we end up doing a lot of repeat work, so our goal should be to calculate the values of subarrays only once.

Here's the strategy. Loop over the elements of the list and:

1. store the `current_sum` (the sum of the first $i$ elements) in a hash table counting how many times that sum has appeared so far.

2. Use the hash table to figure out if there are any subarrays ending at the current element which sum to `k`. Increment a counter if you do.

Finally, return the number of subarrays found.