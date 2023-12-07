from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class CombSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        n = len(arr)

        # Inicializar el tamaño del salto
        gap = n

        # Factor de reducción
        shrink = 1.3

        swapped = False

        while gap > 1 or swapped:
            # Aplicar un salto mínimo de 1
            if gap > 1:
                gap = int(gap / shrink)

            swapped = False

            # Realizar comparaciones y swaps
            for i in range(n - gap):
                if arr[i] > arr[i + gap]:
                    self.swap(arr, i, i + gap)
                    swapped = True

    @staticmethod
    def swap(arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
