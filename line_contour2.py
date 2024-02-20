import cv2
import numpy as np

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

def generate_equidistant_points(points, num_points):
    # Calculate the total length of the contour
    arc_lengths = np.cumsum(np.sqrt(np.sum(np.diff(points, axis=0)**2, axis=1)))
    total_length = arc_lengths[-1]
    
    # Generate equidistant waypoints along the contour
    equidistant_points = []
    for i in range(num_points):
        target_length = i * total_length / (num_points - 1)
        idx = np.searchsorted(arc_lengths, target_length)
        t = (target_length - arc_lengths[idx-1]) / (arc_lengths[idx] - arc_lengths[idx-1])
        point = (1 - t) * points[idx-1] + t * points[idx]
        equidistant_points.append(point)
    
    return np.array(equidistant_points)

# Example usage:
# Load your input image
input_image = cv2.imread('input_image.jpg')

# Detect white spline line
spline_points = detect_white_spline(input_image)

if spline_points is not None:
    # Generate equidistant waypoints along the spline
    waypoints = generate_equidistant_points(spline_points, num_points=100)
    
    # Print the generated waypoints
    print("Generated Waypoints:")
    for i, waypoint in enumerate(waypoints):
        print(f"Waypoint {i+1}: {waypoint}")
else:
    print("No white spline line detected in the image.")
