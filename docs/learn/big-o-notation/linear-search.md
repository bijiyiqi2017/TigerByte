# Big O Example: Linear Search

## What is Linear Search?

**Linear search** is one of the simplest search algorithms. It sequentially checks each element in a list, from the beginning to the end, until it finds the target value or reaches the end of the list.

## Time Complexity Analysis: O(n)

The time complexity of linear search is **O(n)**, which means it has **Linear Time** complexity.

Let's break down why:

* **Input Size (`n`):** The "input size" is the number of elements in the list we are searching through.
* **Operations:** The "operation" we count is the **comparison** (i.e., "is this element the one I'm looking for?").
* **Best-Case Scenario:** The element we are looking for is the very first one in the list. The algorithm runs in **O(1)** time (Constant Time) because it finds the item on its first check, regardless of how large the list is.
* **Worst-Case Scenario:** The element we are looking for is the very last one in the list, or it's not in the list at all. In this case, the algorithm must perform a comparison for **every single element** in the list.
* **Conclusion:** Since Big O notation describes the **worst-case scenario**, the time it takes to complete the search grows in a direct, linear relationship with the number of elements (`n`). If the list doubles in size, the worst-case search time also doubles. Therefore, we say the algorithm is **O(n)**.



## Codebyte Example

Here is a simple Python implementation of linear search. Notice that the `for` loop must visit each item (`n` times) in the worst case.

```codebyte/python
def linear_search(data_list, target):
  """
  Performs a linear search on a list.
  Returns the index of the target, or -1 if not found.
  """
  # 'n' is the length of data_list
  n = len(data_list)

  # In the worst case, this loop runs 'n' times
  for i in range(n):
    # This comparison is the key operation
    if data_list[i] == target:
      return f"Found target {target} at index {i}"

  return f"Target {target} not found in the list."

# --- Test Cases ---
my_list = [4, 8, 15, 16, 23, 42]
n = len(my_list) # n = 6

# Best-case: Found at the beginning
print(linear_search(my_list, 4)) 

# Worst-case: Found at the end
print(linear_search(my_list, 42)) 

# Worst-case: Not in the list
print(linear_search(my_list, 108))