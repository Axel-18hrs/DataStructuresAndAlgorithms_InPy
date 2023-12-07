from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class MergeSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        self.merge_sort(arr)

    @staticmethod
    def merge_sort(arr):
        if len(arr) < 2:
            return

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        MergeSort.merge_sort(left)
        MergeSort.merge_sort(right)
        MergeSort.merge(arr, left, right)

    @staticmethod
    def merge(arr, left, right):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
