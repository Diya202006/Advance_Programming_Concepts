import math

def calculate_distance(point1, point2):
    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    return distance
 
def farthest_point(points):
    origin = (0, 0)
    farthest = points[0]
    max_distance = calculate_distance(origin, farthest)

    for point in points:
        distance = calculate_distance(origin, point)
        if distance > max_distance:
            max_distance = distance
            farthest = point

    return farthest, max_distance
 
points = []

n = int(input("Enter the number of points: "))

for i in range(n):
    x = float(input(f"Enter x-coordinate of point {i+1}: "))
    y = float(input(f"Enter y-coordinate of point {i+1}: "))
    points.append((x, y))

print("\nList of Points:")
for point in points:
    print(point)
 
index1 = int(input("\nEnter the first point index (starting from 1): ")) - 1
index2 = int(input("Enter the second point index (starting from 1): ")) - 1

distance = calculate_distance(points[index1], points[index2])
print("Distance between", points[index1], "and", points[index2], "=", distance)
 
point, distance = farthest_point(points)
print("\nFarthest Point from Origin:", point)
print("Distance from Origin:", distance)