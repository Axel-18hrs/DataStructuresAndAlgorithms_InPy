from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class SelectionSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            # Encontrar el índice del elemento mínimo en el subarreglo no ordenado
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Intercambiar el elemento mínimo encontrado con el primer elemento del subarreglo no ordenado
            arr[i], arr[min_index] = arr[min_index], arr[i]
