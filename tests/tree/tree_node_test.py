
import unittest
from DS.tree.tree_node import AbstractTreeNode


class AbstractTreeNodeTests(unittest.TestCase):

    def test_empty_value_raises_TypeError(self):
        self.assertRaises(TypeError, AbstractTreeNode, None)

    def test_node_with_no_children(self):
        node = AbstractTreeNode('value')
        self.assertEqual('value', node.value)
        self.assertIsNone(node.left_child)
        self.assertIsNone(node.right_child)

    def test_node_with_left_child(self):
        node = AbstractTreeNode('root', AbstractTreeNode('left'))
        self.assertEqual('root', node.value)
        self.assertIsNone(node.right_child)
        self.assertIsNotNone(node.left_child)
        self.assertEqual('left', node.left_child.value)

    def test_node_with_right_child(self):
        node = AbstractTreeNode('root', None, AbstractTreeNode('right'))
        self.assertEqual('root', node.value)
        self.assertIsNone(node.left_child)
        self.assertIsNotNone(node.right_child)
        self.assertEqual('right', node.right_child.value)

    def test_node_with_both_children(self):
        node = AbstractTreeNode('root',
                                AbstractTreeNode('left'),
                                AbstractTreeNode('right'))
        self.assertIsNotNone(node.right_child)
        self.assertIsNotNone(node.left_child)
        self.assertEqual('right', node.right_child.value)
        self.assertEqual('left', node.left_child.value)

if __name__ == "__main__":
    unittest.main()