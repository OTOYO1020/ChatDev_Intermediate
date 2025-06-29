'''
Module for calculating the K-th smallest product from an array of integers.
'''
class ProductCalculator:
    def __init__(self, array, k):
        self.array = array
        self.k = k
    def get_kth_smallest_product(self):
        if len(self.array) < 2:
            raise ValueError("Array must contain at least two elements to form pairs.")
        products = []
        n = len(self.array)
        # Iterate through all unique pairs (i, j) where 1 ≤ i < j ≤ N
        for i in range(n):
            for j in range(i + 1, n):
                product = self.array[i] * self.array[j]
                products.append(product)
        # Sort the products list to find the K-th smallest product
        products.sort()
        # Check if k is out of bounds before accessing products
        if self.k <= 0 or self.k > len(products):
            raise ValueError("K is out of bounds.")
        return products[self.k - 1]