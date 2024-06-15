import math

# Function to take 5 points from the user and add them to a list
def get_points():
    points = []

    for i in range(5):
        point_x = int(input(f"Enter x coordinate for point {i+1}: "))
        point_y = int(input(f"Enter y coordinate for point {i+1}: "))

        points.append((point_x, point_y))

    return points

# Function to calculate the distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Function to calculate distances between each pair of points
def calculate_distances(points):
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calculate_distance(points[i], points[j])
            print(f"Distance between point {i+1} and point {j+1}: {distance}")

def main():
    user_points = get_points()
    calculate_distances(user_points)

main()
