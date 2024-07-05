class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_center(rectangle):
    # Calculate the center coordinates
    center_x = rectangle.x + (rectangle.width / 2)
    center_y = rectangle.y + (rectangle.height / 2)

    # Create a Point object to store the center coordinates
    center_point = Point(center_x, center_y)

    return center_point

# Example usage:
rect = Rectangle(10, 20, 30, 40)
center = find_center(rect)
print(f"Center coordinates: ({center.x}, {center.y})")
