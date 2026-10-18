# Data Structures & Algorithms

My work from the DSA unit, done in Python. Most of the course was sorting, searching and the usual data structures, then graphs towards the end of the semester.

## What's in here

- `sorting/` – bubble, selection, insertion, merge and quick sort
- `searching/` – linear search and binary search (did binary search both with a loop and recursively)
- `data_structures/` – linked list, stack, queue and a binary search tree
- `graphs/` – BFS, DFS and Dijkstra
- `tests/` – unit tests for all of the above

## Running it

Just Python 3, nothing to install.

```bash
python sorting/sorts.py
python graphs/graph.py
python -m unittest discover tests
```

The graph demo uses a few towns around Nairobi with rough distances in km, which made Dijkstra a lot easier to check by hand than letters.

## Complexities

| Algorithm | Best | Average | Worst |
|---|---|---|---|
| Bubble sort | O(n) | O(n²) | O(n²) |
| Selection sort | O(n²) | O(n²) | O(n²) |
| Insertion sort | O(n) | O(n²) | O(n²) |
| Merge sort | O(n log n) | O(n log n) | O(n log n) |
| Quick sort | O(n log n) | O(n log n) | O(n²) |
| Binary search | O(1) | O(log n) | O(log n) |
| BST insert / search | O(log n) | O(log n) | O(n) |
| BFS / DFS | O(V + E) | | |
| Dijkstra (with heap) | O((V + E) log V) | | |

## Things I noticed

- Bubble sort gets its O(n) best case only because of the `swapped` check. Without it, it always does every pass.
- My quick sort picks the middle element as the pivot. Picking the first element made it really slow on lists that were already sorted.
- The BST doesn't balance itself, so if you insert numbers in order it turns into a linked list and searching becomes O(n).
- All my sort functions copy the list first so the original isn't changed. That means they use extra memory, but it made testing them against each other easier.
