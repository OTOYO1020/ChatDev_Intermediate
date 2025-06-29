'''
Module for managing family relationships and calculating insurance coverage.
'''
class FamilyTree:
    def __init__(self, n, parents):
        self.n = n
        self.parents = parents
        self.children = {i: [] for i in range(1, n + 1)}  # Initialize children mapping
        for child in range(2, n + 1):
            parent = parents[child]
            if parent > 0:
                self.children[parent].append(child)  # Map parent to child
    def get_covered_people(self, x, y):
        # Validate input
        if y < 0:
            raise ValueError("The number of generations (y) must be non-negative.")
        if x < 1 or x > self.n:
            raise ValueError(f"Person {x} is not a valid person.")
        covered = set()
        covered.add(x)  # Add the starting person immediately
        if y == 0:  # Check for zero generations
            return covered  # Return only the starting person
        current_generation = [x]
        for _ in range(y):  # Only go down y generations
            next_generation = []
            for person in current_generation:
                if person <= self.n:  # Ensure we don't go out of bounds
                    children = self.children.get(person, [])
                    next_generation.extend(children)  # Always extend with children
            if not next_generation:  # Stop if there are no more generations to traverse
                break
            covered.update(next_generation)  # Add all persons in the last generation
            current_generation = next_generation  # Move to the next generation
        return covered