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
            # Move from left to right
            swapped = False
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    self.swap(arr, i, i + 1)
                    swapped = True

            if not swapped:
                break

            end -= 1

            # Move from right to left
            swapped = False
            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    self.swap(arr, i, i + 1)
                    swapped = True

            start += 1

    @staticmethod
    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
