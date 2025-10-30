# Introduction to Big O Notation

## What is Big O Notation?

**Big O notation** is a mathematical notation used in computer science to describe the **scalability** and **efficiency** of an algorithm. It tells us how the runtime (time complexity) or memory usage (space complexity) of an algorithm grows as the input size (`n`) increases.

Think of it as a way to classify algorithms by their "worst-case scenario" performance. It doesn't tell you the exact speed in seconds, but rather the *rate of growth* of the time it takes to run.

## Why is it Important?

Big O notation is crucial for developers because it helps us make informed decisions about which algorithm or data structure to use.

* **Predicts Performance:** It helps predict how an algorithm will perform with very large inputs.
* **Identifies Bottlenecks:** It helps find parts of the code that will become slow as data scales.
* **Compares Solutions:** If you have two algorithms that solve the same problem, Big O helps you choose the one that will scale more efficiently. For example, an algorithm that is O(log n) is vastly more efficient for large inputs than one that is O(n²).



## Common Time Complexities

Here are some of the most common Big O complexities, from most efficient (fastest) to least efficient (slowest):

* **O(1) - Constant Time:** The algorithm takes the same amount of time regardless of the input size.
    * *Example:* Accessing an element in an array by its index (e.g., `my_array[5]`).

* **O(log n) - Logarithmic Time:** The time it takes increases slowly as the input size grows. This is common in "divide and conquer" algorithms.
    * *Example:* Finding an item in a sorted array using binary search.

* **O(n) - Linear Time:** The runtime grows in direct proportion to the size of the input.
    * *Example:* Looping through all elements in a list once (e.g., linear search).

* **O(n²) - Quadratic Time:** The runtime grows quadratically (the square of the input size). This is common with algorithms that use nested loops over the same data.
    * *Example:* Bubble Sort or Insertion Sort in their worst-case scenarios.