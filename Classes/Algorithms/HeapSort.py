from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class HeapSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        n = len(arr)

        # Construir un heap (montículo) máximo
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extraer elementos uno por uno del heap
        for i in range(n - 1, 0, -1):
            # Mover la raíz actual al final
            self.swap(arr, 0, i)

            # Llamar a heapify en el subárbol reducido
            self.heapify(arr, i, 0)

    @staticmethod
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Comparar con el hijo izquierdo
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Comparar con el hijo derecho
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Si el mayor no es la raíz
        if largest != i:
            HeapSort.swap(arr, i, largest)

            # Recursivamente heapify el subárbol afectado
            HeapSort.heapify(arr, n, largest)

    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
