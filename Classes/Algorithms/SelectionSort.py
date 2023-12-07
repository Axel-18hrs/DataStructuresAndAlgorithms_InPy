from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class SelectionSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            # Find the index of the minimum element in the unsorted subarray
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Swap the found minimum element with the first element of the unsorted subarray
            self.swap(arr, i, min_index)

    def sort_double(self, arr):
        pass  # Implement sorting for double array if needed

    @staticmethod
    def swap(arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
