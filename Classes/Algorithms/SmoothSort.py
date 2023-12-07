from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class SmoothSort(ImethodAlgorithms):
    def __init__(self):
        self.heap = []

    def sort(self, arr):
        self.heap = arr
        n = len(arr)

        for i in range(n):
            self.heapify(i)

        for i in range(n - 1, 0, -1):
            self.swap(0, i)
            self.sift_down(0, i - 1)

    def heapify(self, i):
        n = len(self.heap)
        k = 1
        j = i - 1

        while j >= 0 and self.heap[i] != self.heap[j]:
            if self.heap[i] > self.heap[j]:
                self.swap(i, j)
                self.sift_down(k, i - 1)

            i = j
            j = self.right_child(i, k)
            k += 1

    def sift_down(self, l, r):
        while l <= r:
            k = 2
            i = r
            j = r - l

            while j >= 0 and self.heap[i] != self.heap[j]:
                if self.heap[i] > self.heap[j]:
                    self.swap(i, j)
                    self.sift_down(k, i - 1)

                i = j
                j = self.right_child(i, k)
                k += 1

            l -= 1

    def right_child(self, i, k):
        return i - self.fibonacci(k - 1) + self.fibonacci(k - 2)

    def fibonacci(self, n):
        if n <= 1:
            return n

        a, b = 0, 1

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
