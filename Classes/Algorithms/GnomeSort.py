from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class GnomeSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        n = len(arr)
        index = 0

        while index < n:
            if index == 0:
                index += 1
            if arr[index] >= arr[index - 1]:
                index += 1
            else:
                self.swap(arr, index, index - 1)
                index -= 1

    @staticmethod
    def swap(arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]
