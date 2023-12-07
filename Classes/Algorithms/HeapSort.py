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
            arr[0], arr[i] = arr[i], arr[0]

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
            # Intercambio múltiple de Python
            arr[i], arr[largest] = arr[largest], arr[i]

            # Recursivamente heapify el subárbol afectado
            HeapSort.heapify(arr, n, largest)
