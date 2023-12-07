from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms

class CocktailSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        self.cocktail_sort(arr)

    def cocktail_sort(self, arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            # Mover de izquierda a derecha
            swapped = False
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    # Intercambio múltiple de Python
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            if not swapped:
                break

            end -= 1

            # Mover de derecha a izquierda
            swapped = False
            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    # Intercambio múltiple de Python
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            start += 1
