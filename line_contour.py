import numpy as np
import cv2

def find_waypoints(image):
    # Threshold the grayscale image to obtain binary image
    _, thresh = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize an empty list to store waypoints
    waypoints = []

    # Iterate through contours to find waypoints
    for contour in contours:
        # Calculate the centroid of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            waypoints.append((cX, cY))

    return waypoints

# Example usage:
# Load your output image here
output_image = cv2.imread('output_image.jpg', cv2.IMREAD_GRAYSCALE)

# Get waypoints
waypoints = find_waypoints(output_image)

# Print the detected waypoints
print("Detected Waypoints:")
for i, waypoint in enumerate(waypoints):
    print(f"Waypoint {i+1}: {waypoint}")
