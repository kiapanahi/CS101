
import unittest
from DS.tree.tree_node import AbstractTreeNode as Node

heap_test_cases = [
    {'node': Node(10, left=Node(2), right=Node(1)),
     'is_max_heap': True, 'is_min_heap': False},

    {'node': Node(10, left=Node(20), right=Node(5)),
     'is_max_heap': False, 'is_min_heap': False},

    {'node': Node(10, left=Node(20), right=Node(100)),
     'is_max_heap': False, 'is_min_heap': True}
]


class NodeTests(unittest.TestCase):

    def test_empty_value_raises_TypeError(self):
        self.assertRaises(TypeError, Node, None)

    def test_node_with_no_children(self):
        node = Node('value')
        self.assertEqual('value', node.value)
        self.assertIsNone(node.left_child)
        self.assertIsNone(node.right_child)

    def test_node_with_left_child(self):
        node = Node('root', Node('left'))
        self.assertEqual('root', node.value)
        self.assertIsNone(node.right_child)
        self.assertIsNotNone(node.left_child)
        self.assertEqual('left', node.left_child.value)

    def test_node_with_right_child(self):
        node = Node('root', None, Node('right'))
        self.assertEqual('root', node.value)
        self.assertIsNone(node.left_child)
        self.assertIsNotNone(node.right_child)
        self.assertEqual('right', node.right_child.value)

    def test_node_with_both_children(self):
        node = Node('root',
                    Node('left'),
                    Node('right'))
        self.assertIsNotNone(node.right_child)
        self.assertIsNotNone(node.left_child)
        self.assertEqual('right', node.right_child.value)
        self.assertEqual('left', node.left_child.value)

    def test_single_node_is_max_heap(self):
        node = Node('single')
        self.assertTrue(node.is_max_heap())

    def test_single_node_is_min_heap(self):
        node = Node('single')
        self.assertTrue(node.is_min_heap())

    def test_with_one_smaller_child_is_max_heap(self):
        child_node = Node(5)

        node = Node(10, child_node, None)
        self.assertTrue(node.is_max_heap)

        node = Node(10, None, child_node)
        self.assertTrue(node.is_max_heap)

    def test_with_one_equal_child_is_max_heap(self):
        child_node = Node(10)

        node = Node(10, child_node, None)
        self.assertTrue(node.is_max_heap)

        node = Node(10, None, child_node)
        self.assertTrue(node.is_max_heap)

    def test_with_one_bigger_child_is_min_heap(self):
        child_node = Node(15)

        node = Node(10, child_node, None)
        self.assertTrue(node.is_max_heap)

        node = Node(10, None, child_node)
        self.assertTrue(node.is_max_heap)

    def test_with_one_equal_child_is_min_heap(self):
        child_node = Node(10)

        node = Node(10, child_node, None)
        self.assertTrue(node.is_max_heap)

        node = Node(10, None, child_node)
        self.assertTrue(node.is_max_heap)

    def test_node_with_smaller_children_is_max_heap(self):
        left_child = Node(1)
        right_child = Node(2)

        node = Node(10, left=left_child, right=right_child)
        self.assertTrue(node.is_max_heap())

    def test_node_with_equal_children_is_max_heap(self):
        left_child = Node(10)
        right_child = Node(10)

        node = Node(10, left=left_child, right=right_child)
        self.assertTrue(node.is_max_heap())

    def test_validate_heap_state(self):

        for test_case in heap_test_cases:
            n = test_case['node']
            expected_max_heap = test_case['is_max_heap']
            expected_min_heap = test_case['is_min_heap']
            self.assertEqual(n.is_max_heap(), expected_max_heap)
            self.assertEqual(n.is_min_heap(), expected_min_heap)


if __name__ == "__main__":
    unittest.main()
