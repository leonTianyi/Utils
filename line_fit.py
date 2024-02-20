import numpy as np
import cv2
from scipy.optimize import curve_fit

def fit_line(image):
    # Find non-zero pixels (white) in the input image
    nonzero = cv2.findNonZero(image)
    # Extract x and y coordinates of non-zero pixels
    points = np.squeeze(nonzero)

    # Fit a polynomial function to the points
    coefficients = np.polyfit(points[:, 0], points[:, 1], 2)
    fitted_line = np.poly1d(coefficients)

    return fitted_line

def generate_waypoints(fitted_line, num_waypoints_per_segment=10):
    waypoints = []
    # Calculate the length of the line segment
    line_length = np.max(fitted_line.x) - np.min(fitted_line.x)

    # Divide the line into smaller segments and generate waypoints
    for i in range(num_waypoints_per_segment, int(line_length), num_waypoints_per_segment):
        # Sample points along the segment
        x_values = np.linspace(i - num_waypoints_per_segment, i, num=num_waypoints_per_segment)
        y_values = fitted_line(x_values)
        # Append waypoints
        waypoints.extend(zip(x_values, y_values))

    return waypoints

# Example usage:
# Load your output image here
output_image = cv2.imread('output_image.jpg', cv2.IMREAD_GRAYSCALE)

# Fit a polynomial function to the white line
fitted_line = fit_line(output_image)

# Generate waypoints along the fitted line
waypoints = generate_waypoints(fitted_line)

# Print the generated waypoints
print("Generated Waypoints:")
for i, waypoint in enumerate(waypoints):
    print(f"Waypoint {i+1}: {waypoint}")
