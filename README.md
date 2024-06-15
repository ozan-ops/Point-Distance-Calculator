# Distance Calculation Between Points

## Overview
This Python program allows the user to input coordinates for 5 points in a 2D plane and calculates the distances between each pair of points. The program performs the following main tasks:
1. Takes 5 points as input from the user.
2. Calculates the distance between every pair of points.
3. Prints the calculated distances.

## Functions

### `get_points()`
- Prompts the user to enter the x and y coordinates for 5 points.
- Returns a list of tuples, where each tuple represents a point's coordinates (x, y).

### `calculate_distance(point1, point2)`
- Takes two points as input (each represented as a tuple).
- Calculates and returns the Euclidean distance between these two points using the formula:
  \[
  \text{distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
  \]

### `calculate_distances(points)`
- Takes a list of points as input.
- Iterates through each pair of points and calculates the distance between them.
- Prints the calculated distance for each pair of points.

### `main()`
- Calls `get_points()` to obtain the user-input points.
- Calls `calculate_distances()` to compute and print the distances between each pair of points.

## Usage
To use this program:
1. Run the script.
2. When prompted, input the x and y coordinates for 5 points.
3. The program will then calculate and print the distances between each pair of points.

## Example

Here's an example interaction with the program:
Enter x coordinate for point 1: 1
Enter y coordinate for point 1: 2
Enter x coordinate for point 2: 3
Enter y coordinate for point 2: 4
Enter x coordinate for point 3: 5
Enter y coordinate for point 3: 6
Enter x coordinate for point 4: 7
Enter y coordinate for point 4: 8
Enter x coordinate for point 5: 9
Enter y coordinate for point 5: 10
Distance between point 1 and point 2: 2.8284271247461903
Distance between point 1 and point 3: 5.656854249492381
Distance between point 1 and point 4: 8.48528137423857
Distance between point 1 and point 5: 11.313708498984761
Distance between point 2 and point 3: 2.8284271247461903
Distance between point 2 and point 4: 5.656854249492381
Distance between point 2 and point 5: 8.48528137423857
Distance between point 3 and point 4: 2.8284271247461903
Distance between point 3 and point 5: 5.656854249492381
Distance between point 4 and point 5: 2.8284271247461903


## Note
- Ensure that the inputs for the coordinates are integers.
- The distances calculated are Euclidean distances.

This program provides a simple way to understand and calculate distances between multiple points in a 2D space.
