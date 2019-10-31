from .constants import HEAP_TYPE


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

    def is_max_heap(self) -> bool:
        is_max_heap = True

        if self.left_child is not None:
            is_max_heap = (is_max_heap and (
                self.left_child.value <= self.value))

        if self.right_child is not None:
            is_max_heap = (is_max_heap and (
                self.right_child.value <= self.value))

        return is_max_heap

    def is_min_heap(self) -> bool:
        is_min_heap = True

        if self.left_child is not None:
            is_min_heap = (is_min_heap and (
                self.left_child.value >= self.value))

        if self.right_child is not None:
            is_min_heap = (is_min_heap and (
                self.right_child.value >= self.value))

        return is_min_heap

    def heapify(self, heap_type: HEAP_TYPE = HEAP_TYPE.MAX):
        if heap_type is HEAP_TYPE.MAX:
            self._max_heapify()
        elif heap_type is HEAP_TYPE.MIN:
            self._min_heapify()
        pass

    def _max_heapify(self):
        if self.has_left_child():
            if self.left_child.value > self.value:
                self.value, self.left_child.value = self.left_child.value, self.value

        if self.has_right_child():
            if self.right_child.value > self.value:
                self.value, self.right_child.value = self.right_child.value, self.value

    def _min_heapify(self):
        if self.has_left_child():
            if self.left_child.value < self.value:
                self.value, self.left_child.value = self.left_child.value, self.value

        if self.has_right_child():
            if self.right_child.value < self.value:
                self.value, self.right_child.value = self.right_child.value, self.value

    def has_left_child(self):
        return self.left_child is not None and self.left_child.value is not None

    def has_right_child(self):
        return self.right_child is not None and self.right_child.value is not None
