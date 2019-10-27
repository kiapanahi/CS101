class AbstractTreeNode(object):
    """
    the abstraction of a tree node containing a generic value and 
    optional left/right children
    """

    # type hinting is done in strings due to the 'forward referencing' problem
    # https://www.python.org/dev/peps/pep-0484/#id28

    def __init__(self, value=None, left: 'AbstractTreeNode' = None, right: 'AbstractTreeNode' = None):
        if value is None:
            raise TypeError('node value cannot be None')

        self.value = value
        self.left_child = left
        self.right_child = right
