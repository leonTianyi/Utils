#include <opencv2/opencv.hpp>
#include <grid_map_cv/grid_map_cv.hpp> // Required for grid_map conversion to OpenCV image

// Function to convert grid_map::GridMap to OpenCV image
cv::Mat gridMapToImage(const grid_map::GridMap& gridMap);

// Function to convert sensor_msgs::PointCloud2 to PointCloudData
PointCloudData pointCloudToData(const sensor_msgs::PointCloud2& pointCloud);

int main() {
    // Read GridMap data (assuming you already have gridMap object)
    grid_map::GridMap gridMap; // Replace with your GridMap object

    // Read PointCloud data (assuming you already have pointCloud object)
    sensor_msgs::PointCloud2 pointCloud; // Replace with your PointCloud object

    // Convert GridMap to OpenCV image
    cv::Mat gridMapImage = gridMapToImage(gridMap);

    // Convert PointCloud to PointCloudData
    PointCloudData pointCloudData = pointCloudToData(pointCloud);

    // Draw the PointCloud on the GridMap image
    for (const auto& point : pointCloudData.points) {
        int x = static_cast<int>(point.x);
        int y = static_cast<int>(point.y);

        // Adjust the color according to elevation value
        double elevation = point.z; // Replace this with your elevation value
        double minElevation = 0.0; // Set your minimum elevation value
        double maxElevation = 5.0; // Set your maximum elevation value
        int colorValue = static_cast<int>((elevation - minElevation) / (maxElevation - minElevation) * 255);

        // Draw a colored point representing the PointCloud data
        cv::circle(gridMapImage, cv::Point(x, y), 2, cv::Scalar(0, 0, colorValue), -1);
    }

    // Display the visualization image
    cv::imshow("Visualization", gridMapImage);

    // Wait for a key press and close the window
    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}

cv::Mat gridMapToImage(const grid_map::GridMap& gridMap) {
    cv::Mat image;
    grid_map::GridMapCvConverter::toImage<unsigned char, 3>(gridMap, "elevation", CV_8UC3, image, 0.0, 5.0); // Replace "elevation" with your actual layer name
    return image;
}

PointCloudData pointCloudToData(const sensor_msgs::PointCloud2& pointCloud) {
    // Implement your code to convert sensor_msgs::PointCloud2 to PointCloudData
    // Extract the points from the PointCloud2 message and store them in the PointCloudData structure
    // The PointCloudData structure should have a vector of points (x, y, z) or a similar representation
}
