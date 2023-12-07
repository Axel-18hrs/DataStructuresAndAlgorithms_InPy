from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class Insertionsort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        self.insertion_sort_algorithm(arr)

    def insertion_sort_algorithm(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1

            # Mover los elementos del subarreglo arr[0..i-1] que son mayores que key
            # a una posición adelante de su posición actual
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j = j - 1
            arr[j + 1] = key
