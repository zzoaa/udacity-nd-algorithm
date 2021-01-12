## Why did you use that data structure?

I apply the double linked list for LRU Cache.

Because if the some value were selected, that value should move to tail.
Double Linked List support to add element to tail.

Therefore, the element of head will be removed when the cache is full.

## the efficiency (time and space) of your solution.

Adding cache is O(1) of time complexity.
Getting cache is O(1) of time complexity.

LRU Cache is O(N) of space complexity.
