# Additional Big O Examples

Beyond O(n) linear time, algorithms can be much faster or much slower. Here are a few common examples.

---

## 1. Constant Time: O(1)

An algorithm is **O(1)** if it takes the same amount of time to run, regardless of the size of the input.

### Example: Accessing an Array Index

Accessing an element in an array by its index (e.g., `my_list[3]`) is a classic O(1) operation. The computer knows the memory address of the start of the list and can calculate the position of the 3rd element instantly, whether the list has 10 elements or 10 million.

```codebyte/python
def get_first_element(data_list):
  # This operation takes the same
  # amount of time no matter how
  # long data_list is.
  if len(data_list) > 0:
    return data_list[0]
  return None

small_list = [1, 2, 3]
large_list = list(range(1000000))

# Both of these print statements
# run in O(1) time.
print(f"First element (small list): {get_first_element(small_list)}")
print(f"First element (large list): {get_first_element(large_list)}")