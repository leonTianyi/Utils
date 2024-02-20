import cv2
import numpy as np
from scipy.interpolate import splprep, splev

def detect_white_spline(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Threshold to obtain binary image with white areas
    _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # Filter contours based on area and approximation
    filtered_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # Adjust this threshold based on your image size and noise
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            if len(approx) > 4:  # Assuming the spline has more than 4 points
                filtered_contours.append(contour)
                
    # Assuming there's only one white spline line
    if len(filtered_contours) > 0:
        spline_contour = filtered_contours[0]
        spline_points = np.squeeze(spline_contour)
        return spline_points
    else:
        return None

def generate_waypoints_along_spline(spline_points, num_waypoints=100):
    # Fit a spline to the points
    tck, _ = splprep([spline_points[:, 0], spline_points[:, 1]], s=0)
    
    # Generate equidistant waypoints along the spline
    u = np.linspace(0, 1, num=num_waypoints)
    waypoints = np.column_stack(splev(u, tck))
    
    return waypoints.tolist()

# Example usage:
# Load your input image
input_image = cv2.imread('input_image.jpg')

# Detect white spline line
spline_points = detect_white_spline(input_image)

if spline_points is not None:
    # Generate waypoints along the spline
    waypoints = generate_waypoints_along_spline(spline_points)
    
    # Print the generated waypoints
    print("Generated Waypoints:")
    for i, waypoint in enumerate(waypoints):
        print(f"Waypoint {i+1}: {waypoint}")
else:
    print("No white spline line detected in the image.")
