from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class BinarytreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTreeSort(ImethodAlgorithms):
    def __init__(self):
        self.root = None

    def sort(self, arr):
        # Build the binary tree
        for value in arr:
            self.root = self._insert(self.root, value)

        # Traverse the tree in order to get the sorted elements
        index = [0]  # Using a list to simulate a mutable integer (Python doesn't have ref)
        self._in_order_traversal(self.root, arr, index)

    def _insert(self, node, value):
        if node is None:
            return BinarytreeNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node

    def _in_order_traversal(self, node, arr, index):
        if node is not None:
            self._in_order_traversal(node.left, arr, index)
            arr[index[0]] = node.value
            index[0] += 1
            self._in_order_traversal(node.right, arr, index)
