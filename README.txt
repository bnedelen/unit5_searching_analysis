# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Implementation Documentation

### Linear Search

I implemented `linear_search(lst, target)` with a `for` loop that checked each element from index 0 to the end of the list. The function returned the index as soon as it found a match and returned -1 if the loop finished without one. I documented in the comments that the worst case checked every element, which made the time complexity O(n).

### Binary Search

I implemented `binary_search(lst, target)` with a `while` loop and two pointers, `low` and `high`, that marked the part of the sorted list still being searched. Each iteration, I calculated the middle index and compared it to the target. If the middle value was too small, I moved `low` past the middle. If it was too large, I moved `high` before the middle. The search space was cut in half each time, which made the time complexity O(log n). The function returned -1 once `low` passed `high`.

### Helper Functions

I added `count_linear_comparisons`, `count_binary_comparisons`, and `time_search` so I could measure how many comparisons each algorithm made and how long each took. The two search functions themselves stayed unchanged.

### Small Dataset Test

I created a sorted list of 10 numbers and searched for 57 (exists) and 50 (does not exist). Both algorithms returned the same results. Linear search used 6 and 10 comparisons, and binary search used 3 for both. The difference was small because the list was small.

### Large Dataset Test

I created a sorted list of 1,000,000 even numbers and searched for the last value and for a missing value. Linear search made 1,000,000 comparisons and took roughly 26 to 32 ms. Binary search made 20 comparisons and took less than 0.01 ms. This showed that binary search became far more efficient as the dataset grew.

### Edge Cases

I tested six edge cases:

- **Empty list:** Both searches returned -1 without errors.
- **Single-element list (found and not found):** Both searches handled it correctly.
- **Value at the first position:** Linear search found it in 1 comparison, which was its best case.
- **Value at the last position:** Linear search checked every item, which was its worst case.
- **Unsorted list:** Binary search returned -1 even though the value was present, which showed that it required sorted data.

### Real-World Scenario

I built a student records example. I used binary search to look up student IDs in a large sorted roster. I used linear search to check a short, unsorted list of recent logins, because sorting it would have cost more than scanning it.

### Performance Analysis

Linear search grew in a straight line with the data (O(n)), while binary search grew very slowly (O(log n)). Doubling the data doubled the work for linear search but added only one extra step for binary search.

