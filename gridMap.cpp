#include <opencv2/opencv.hpp>
#include <grid_map_cv/grid_map_cv.hpp> // Required for grid_map conversion to OpenCV image

// Function to convert grid_map::GridMap to OpenCV image with scaling
cv::Mat toCVImage(const grid_map::GridMap& gridMap, double scale_factor);

int main() {
    // Read GridMap data (assuming you already have gridMap object)
    grid_map::GridMap gridMap; // Replace with your GridMap object

    // Define the scale factor
    double scale_factor = 2.0; // You can adjust this as needed

    // Convert the GridMap to an OpenCV image with scaling
    cv::Mat scaledImage = toCVImage(gridMap, scale_factor);

    // Display the scaled image
    cv::imshow("Scaled GridMap", scaledImage);

    // Wait for a key press and close the window
    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}

cv::Mat toCVImage(const grid_map::GridMap& gridMap, double scale_factor) {
    cv::Mat image;
    grid_map::GridMapCvConverter::toImage<unsigned char, 3>(gridMap, "elevation", CV_8UC3, image, 0.0, 5.0); // Replace "elevation" with your actual layer name

    // Resize the image based on the scale factor
    cv::resize(image, image, cv::Size(), scale_factor, scale_factor, cv::INTER_LINEAR);

    return image;
}
