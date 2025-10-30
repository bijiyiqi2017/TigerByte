# A Closer Look at Common Time Complexities

Big O notation provides a shared language to discuss algorithm efficiency. Here is a breakdown of the most common complexities, ordered from most efficient (fastest) to least efficient (slowest).



---

## O(1) - Constant Time

The algorithm's runtime is constant; it does not change regardless of the input size (`n`).

* **Analogy:** Grabbing the first book from a pile. It doesn't matter if the pile has 5 books or 5,000 books; picking the top one takes the same amount of time.
* **Examples:**
    * Accessing an array element by its index (e.g., `arr[5]`).
    * Pushing or popping from a stack.
    * Looking up a value in a hash map (dictionary) by its key.

---

## O(log n) - Logarithmic Time

The runtime grows very slowly, increasing by one step each time the input size (`n`) doubles. This is highly efficient and typical of "divide and conquer" algorithms.

* **Analogy:** Finding a name in a phone book. You open to the middle, decide if the name is in the first or second half, and throw the other half away. You repeat this, cutting the problem size in half at each step.
* **Examples:**
    * **Binary Search** in a sorted array.
    * Finding an item in a balanced Binary Search Tree (BST).

---

## O(n) - Linear Time

The runtime grows linearly, in direct proportion to the input size (`n`). If the input size doubles, the runtime roughly doubles.

* **Analogy:** Reading every page in a book. If the book has twice as many pages, it takes you twice as long.
* **Examples:**
    * **Linear Search** (looping through a list to find an item).
    * Finding the single largest element in an unsorted array.
    * Summing all elements in a list.

---

## O(n log n) - Log-Linear Time

The runtime is a product of `n` and `log n`. This is a very common and efficient complexity for sorting algorithms.

* **Analogy:** Imagine having to look up `n` items in a phone book (`n` $\times$ `log n`).
* **Examples:**
    * **Merge Sort**.
    * **Quicksort** (in its average case, though its worst case is O(n²)).
    * **Heapsort**.

---

## O(n²) - Quadratic Time

The runtime grows by the square of the input size. This is common when an operation must be performed on every pair of elements in a list (e.g., a loop nested inside another loop).

* **Analogy:** Shaking hands with everyone in a room. If you have 10 people (`n=10`), you have $\approx 100$ handshakes (`n²`). If the number of people doubles to 20, the handshakes quadruple to $\approx 400$.
* **Examples:**
    * **Bubble Sort**.
    * **Insertion Sort**.
    * **Selection Sort**.
    * Finding if a list has any duplicates by comparing every element to every other element.