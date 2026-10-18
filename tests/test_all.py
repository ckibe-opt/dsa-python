import os
import random
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from sorting.sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
from searching.search import linear_search, binary_search, binary_search_recursive
from data_structures.linked_list import LinkedList
from data_structures.stack_queue import Stack, Queue, balanced_brackets
from data_structures.bst import BST
from graphs.graph import Graph


class TestSorting(unittest.TestCase):
    def test_all_sorts_match_sorted(self):
        for _ in range(20):
            data = [random.randint(-50, 50) for _ in range(random.randint(0, 30))]
            for fn in (bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort):
                self.assertEqual(fn(data), sorted(data), fn.__name__)

    def test_input_not_changed(self):
        data = [3, 1, 2]
        merge_sort(data)
        self.assertEqual(data, [3, 1, 2])


class TestSearching(unittest.TestCase):
    def setUp(self):
        self.nums = [1, 3, 5, 7, 9, 11]

    def test_found(self):
        self.assertEqual(linear_search(self.nums, 7), 3)
        self.assertEqual(binary_search(self.nums, 7), 3)
        self.assertEqual(binary_search_recursive(self.nums, 7), 3)

    def test_not_found(self):
        self.assertEqual(binary_search(self.nums, 4), -1)
        self.assertEqual(binary_search([], 4), -1)


class TestLinkedList(unittest.TestCase):
    def test_basic_ops(self):
        ll = LinkedList()
        for x in [1, 2, 3]:
            ll.append(x)
        ll.prepend(0)
        self.assertEqual(ll.to_list(), [0, 1, 2, 3])
        self.assertTrue(ll.delete(2))
        self.assertFalse(ll.delete(99))
        ll.reverse()
        self.assertEqual(ll.to_list(), [3, 1, 0])
        self.assertEqual(len(ll), 3)


class TestStackQueue(unittest.TestCase):
    def test_stack(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.peek(), 1)

    def test_queue(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        self.assertEqual(q.dequeue(), "a")

    def test_empty_errors(self):
        with self.assertRaises(IndexError):
            Stack().pop()

    def test_brackets(self):
        self.assertTrue(balanced_brackets("{[()]}"))
        self.assertFalse(balanced_brackets("(]"))
        self.assertFalse(balanced_brackets("(("))


class TestBST(unittest.TestCase):
    def test_bst(self):
        t = BST()
        for k in [8, 3, 10, 1, 6, 14]:
            t.insert(k)
        self.assertEqual(t.inorder(), [1, 3, 6, 8, 10, 14])
        self.assertTrue(t.contains(6))
        self.assertFalse(t.contains(7))
        self.assertEqual(t.min(), 1)
        self.assertEqual(t.height(), 3)


class TestGraph(unittest.TestCase):
    def test_traversals_and_dijkstra(self):
        g = Graph()
        g.add_edge("A", "B", 4)
        g.add_edge("A", "C", 1)
        g.add_edge("C", "B", 2)
        g.add_edge("B", "D", 5)
        self.assertEqual(set(g.bfs("A")), {"A", "B", "C", "D"})
        self.assertEqual(g.dfs("A")[0], "A")
        dist = g.dijkstra("A")
        self.assertEqual(dist["B"], 3)
        self.assertEqual(dist["D"], 8)


if __name__ == "__main__":
    unittest.main()
