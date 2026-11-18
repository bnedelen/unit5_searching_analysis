"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import time


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Walk through the list one position at a time, starting at index 0.
    for index in range(len(lst)):
        # Each pass does exactly one comparison.
        if lst[index] == target:
            return index  # Found it, so stop early and return the position.

    # Reaching this line means every element was checked and none matched.
    #
    # WHY THIS IS O(n):
    # In the worst case (target is last or missing) the loop runs once for
    # every element. If the list has n items, that is n comparisons. When n
    # doubles, the work doubles too, so the running time grows in a straight
    # line with the input size.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # low and high mark the part of the list that could still hold the target.
    # At the start, that is the whole list.
    low = 0
    high = len(lst) - 1

    # Keep going while at least one candidate position remains.
    # An empty list skips this loop completely (high is -1, so low > high).
    while low <= high:
        # Check the middle of the current search space.
        # Using low + (high - low) // 2 avoids integer overflow in languages
        # like Java or C; in Python it is just a good habit.
        mid = low + (high - low) // 2

        if lst[mid] == target:
            return mid  # Found it.
        elif lst[mid] < target:
            # The target is larger, and the list is sorted, so everything at
            # or before mid is too small. Throw away the left half.
            low = mid + 1
        else:
            # The target is smaller, so everything at or after mid is too
            # large. Throw away the right half.
            high = mid - 1

        # Either way, the search space shrank by about half this iteration:
        # n -> n/2 -> n/4 -> ... -> 1. Halving n down to 1 takes about
        # log2(n) steps, which is why binary search is O(log n).

    # low passed high, so no candidates are left and the target is not here.
    return -1


def count_linear_comparisons(lst, target):
    """Helper: count how many comparisons linear search makes."""
    comparisons = 0
    for value in lst:
        comparisons += 1
        if value == target:
            break
    return comparisons


def count_binary_comparisons(lst, target):
    """Helper: count how many comparisons binary search makes."""
    comparisons = 0
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = low + (high - low) // 2
        comparisons += 1
        if lst[mid] == target:
            break
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return comparisons


def time_search(search_fn, lst, target, repeats=20):
    """Helper: average run time (in milliseconds) over several runs."""
    start = time.perf_counter()
    for _ in range(repeats):
        search_fn(lst, target)
    end = time.perf_counter()
    return (end - start) / repeats * 1000


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small = [3, 8, 15, 23, 42, 57, 61, 78, 90, 104]
    print(f"Dataset: {small}")

    # Value that exists (57 is at index 5).
    # Both algorithms should return 5. Linear search needs 6 comparisons
    # (3, 8, 15, 23, 42, 57); binary search needs only 3.
    print("\nSearching for 57 (exists):")
    print(f"  Linear search index: {linear_search(small, 57)}")
    print(f"  Binary search index: {binary_search(small, 57)}")
    print(f"  Linear comparisons:  {count_linear_comparisons(small, 57)}")
    print(f"  Binary comparisons:  {count_binary_comparisons(small, 57)}")

    # Value that does not exist (50 falls between 42 and 57).
    # Both algorithms should return -1. Linear search had to check all 10
    # items to be sure; binary search ruled it out in only 3 checks.
    print("\nSearching for 50 (does not exist):")
    print(f"  Linear search index: {linear_search(small, 50)}")
    print(f"  Binary search index: {binary_search(small, 50)}")
    print(f"  Linear comparisons:  {count_linear_comparisons(small, 50)}")
    print(f"  Binary comparisons:  {count_binary_comparisons(small, 50)}")

    # With only 10 items the difference is tiny, so either algorithm feels
    # instant. The gap only becomes meaningful as the data grows.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    size = 1_000_000
    large = list(range(0, size * 2, 2))  # sorted even numbers: 0, 2, 4, ...
    print(f"Dataset: {size:,} sorted even numbers")

    # Worst case for linear search: the target is the very last item.
    last_value = large[-1]
    # A missing value: odd numbers are never in this list.
    missing_value = 777_777

    for label, target in [("last item (worst case)", last_value),
                          ("missing value", missing_value)]:
        print(f"\nSearching for {target:,} ({label}):")
        print(f"  Linear index: {linear_search(large, target)}  | "
              f"comparisons: {count_linear_comparisons(large, target):,}  | "
              f"time: {time_search(linear_search, large, target, 5):.4f} ms")
        print(f"  Binary index: {binary_search(large, target)}  | "
              f"comparisons: {count_binary_comparisons(large, target):,}  | "
              f"time: {time_search(binary_search, large, target):.6f} ms")

    # RESULTS EXPLANATION:
    # Linear search made about 1,000,000 comparisons, while binary search
    # made about 20 (log2 of 1,000,000 is roughly 19.9). Every comparison in
    # binary search throws away half of what is left, so doubling the
    # dataset adds only ONE extra step. Linear search must do twice as much
    # work when the dataset doubles. That is why binary search pulls further
    # ahead as the data gets larger: O(log n) grows very slowly compared to
    # O(n).

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: empty list.
    # Linear search's loop never runs, and binary search's while condition
    # (0 <= -1) is False right away, so both return -1 without crashing.
    print("\nEmpty list [] searching for 5:")
    print(f"  Linear: {linear_search([], 5)}  Binary: {binary_search([], 5)}")

    # Edge case 2: single-element list, target present.
    # Binary search checks mid = 0 and finds it on the first try.
    print("\nSingle-element list [7] searching for 7:")
    print(f"  Linear: {linear_search([7], 7)}  Binary: {binary_search([7], 7)}")

    # Edge case 3: single-element list, target missing.
    # One comparison shows it is not there, then the search space is empty.
    print("\nSingle-element list [7] searching for 9:")
    print(f"  Linear: {linear_search([7], 9)}  Binary: {binary_search([7], 9)}")

    # Edge case 4: value at the first position.
    # Linear search finds it on comparison #1 (its best case, O(1)).
    # Binary search still has to narrow in from the middle.
    print("\nValue at first position (3 in the small dataset):")
    print(f"  Linear: {linear_search(small, 3)} "
          f"({count_linear_comparisons(small, 3)} comparison)  "
          f"Binary: {binary_search(small, 3)} "
          f"({count_binary_comparisons(small, 3)} comparisons)")

    # Edge case 5: value at the last position.
    # This is linear search's worst case (checks every item), but binary
    # search still finds it in about log2(n) steps.
    print("\nValue at last position (104 in the small dataset):")
    print(f"  Linear: {linear_search(small, 104)} "
          f"({count_linear_comparisons(small, 104)} comparisons)  "
          f"Binary: {binary_search(small, 104)} "
          f"({count_binary_comparisons(small, 104)} comparisons)")

    # Edge case 6: unsorted list (invalid input for binary search).
    # Binary search ASSUMES sorted data. On an unsorted list it can discard
    # the half that holds the target and wrongly return -1.
    unsorted = [42, 7, 91, 3, 60]
    print("\nUnsorted list [42, 7, 91, 3, 60] searching for 3:")
    print(f"  Linear: {linear_search(unsorted, 3)} (correct)  "
          f"Binary: {binary_search(unsorted, 3)} (wrong, 3 IS in the list)")

    # ===============================
    # REAL-WORLD SEARCH SCENARIO
    # ===============================
    # README requirement 5: a student records system that uses BOTH searches.
    #
    # - Student ID lookup uses BINARY search because the roster is stored
    #   sorted by ID and is large and searched often.
    # - "Recent activity" lookup uses LINEAR search because the log is short,
    #   unsorted (newest entries are just added to the end), and sorting it
    #   every time would cost more than a quick scan.

    print("\n=== REAL-WORLD SCENARIO: STUDENT RECORDS ===")
    roster_ids = list(range(100000, 150000, 3))  # sorted student IDs
    recent_logins = ["S104523", "S100012", "S149997", "S120300", "S100003"]

    lookup_id = 120001
    pos = binary_search(roster_ids, lookup_id)
    print(f"Roster lookup (binary): ID {lookup_id} -> "
          f"{'found at index ' + str(pos) if pos != -1 else 'not found'}")

    login_id = "S120300"
    pos = linear_search(recent_logins, login_id)
    print(f"Recent login check (linear): {login_id} -> "
          f"{'found at index ' + str(pos) if pos != -1 else 'not found'}")

    print("\nBinary search fits the huge sorted roster; linear search fits "
          "the tiny unsorted log.")


if __name__ == "__main__":
    main()
