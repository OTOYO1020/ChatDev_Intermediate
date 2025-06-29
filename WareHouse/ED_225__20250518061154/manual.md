Here's a detailed user manual for the visible sevens calculator software, formatted in Markdown as requested:

```markdown
# Visible Sevens Calculator

A Python application for calculating the maximum number of visible sevens based on their coordinates.

## Quick Install

To run the Visible Sevens Calculator, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install typing
```

## 🤔 What is this?

The Visible Sevens Calculator allows users to determine how many '7's can be seen from the origin (0, 0) based on their coordinates. The application checks for visibility by evaluating the intersections of quadrilaterals formed by the origin and the coordinates of the '7's.

### Main Functions

1. **max_visible_sevens(N: int, coordinates: List[Tuple[int, int]]) -> int**: 
   - This function calculates the maximum number of visible '7's from the origin.
   - **Parameters**:
     - `N`: The number of '7's (integer).
     - `coordinates`: A list of tuples containing the coordinates of each '7' (List[Tuple[int, int]]).
   - **Returns**: An integer representing the maximum count of visible '7's.

2. **is_visible(origin: Tuple[int, int], point: Tuple[int, int], other_points: List[Tuple[int, int]]) -> bool**:
   - This function checks if a specific '7' is visible from the origin by determining if the quadrilateral formed by the origin and the '7' intersects with any other '7's.
   - **Parameters**:
     - `origin`: The origin point (Tuple[int, int]).
     - `point`: The coordinates of the '7' being checked (Tuple[int, int]).
     - `other_points`: A list of other '7' coordinates (List[Tuple[int, int]]).
   - **Returns**: A boolean indicating visibility.

3. **intersects(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int], p4: Tuple[int, int]) -> bool**:
   - This function checks if two line segments intersect.
   - **Parameters**:
     - `p1`, `p2`: The endpoints of the first line segment (Tuple[int, int]).
     - `p3`, `p4`: The endpoints of the second line segment (Tuple[int, int]).
   - **Returns**: A boolean indicating whether the segments intersect.

4. **on_segment(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> bool**:
   - This function checks if a point lies on a given line segment.
   - **Parameters**:
     - `p`, `q`: The endpoints of the segment (Tuple[int, int]).
     - `r`: The point being checked (Tuple[int, int]).
   - **Returns**: A boolean indicating if the point is on the segment.

## How to Use

1. **Run the Application**:
   - Execute the `main.py` file in your terminal or command prompt:
   ```bash
   python main.py
   ```

2. **Input Data**:
   - When prompted, enter the number of '7's you want to input.
   - Then, enter the coordinates of the '7's in the format `(x,y)` separated by semicolons. For example:
   ```
   Enter number of 7's: 3
   Enter coordinates (x,y) separated by semicolons: 1,2; 2,3; 3,1
   ```

3. **View Results**:
   - The application will calculate and display the maximum number of visible '7's based on the provided coordinates.

## Edge Cases

- If `N` is 0, the application will return 0 as there are no '7's to evaluate.
- If all '7's are positioned in a way that they are all visible, the application will return the total count of '7's.

## Conclusion

The Visible Sevens Calculator is a powerful tool for analyzing the visibility of points in a 2D space. By following the instructions above, users can easily install the application and determine the maximum number of visible '7's from the origin.
```

This manual provides a comprehensive overview of the software, its functions, installation instructions, and usage guidelines, ensuring that users can effectively utilize the Visible Sevens Calculator.