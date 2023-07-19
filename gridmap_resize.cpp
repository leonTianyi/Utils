#include <grid_map_core/grid_map_core.hpp>

// Function to resize the GridMap
grid_map::GridMap resizeGridMap(const grid_map::GridMap& originalGridMap, double scale_factor);

int main() {
    // Read original GridMap data (assuming you already have originalGridMap object)
    grid_map::GridMap originalGridMap; // Replace with your original GridMap object

    // Define the scale factor
    double scale_factor = 2.0; // You can adjust this as needed

    // Resize the GridMap
    grid_map::GridMap resizedGridMap = resizeGridMap(originalGridMap, scale_factor);

    // Now you have the resized GridMap with preserved data

    return 0;
}

grid_map::GridMap resizeGridMap(const grid_map::GridMap& originalGridMap, double scale_factor) {
    // Create a new grid map with the desired dimensions and resolution based on the scale factor
    grid_map::GridMap newGridMap(originalGridMap.getGeometry().getSize() * scale_factor, originalGridMap.getResolution() / scale_factor);

    // Iterate through each cell in the new grid map
    for (grid_map::GridMapIterator iterator(newGridMap); !iterator.isPastEnd(); ++iterator) {
        const grid_map::Index index(*iterator);

        // Determine the corresponding location in the original grid map using the scale factor
        grid_map::Position originalPosition = newGridMap.getPosition(index) / scale_factor;

        // Interpolate data from the original grid map to assign values to the cells in the new grid map
        // You will need to implement an appropriate interpolation method based on your data type (e.g., bilinear interpolation for elevation data)

        // Example: Bilinear interpolation for elevation layer (adjust as needed for other layers)
        double interpolatedElevation = interpolateBilinear(originalGridMap, "elevation", originalPosition);

        // Set the interpolated elevation value to the corresponding cell in the new grid map
        newGridMap.at("elevation", index) = interpolatedElevation;
    }

    // Copy other layers from the original grid map to the corresponding layers in the new grid map
    // You can use grid_map::copyLayer() function for this purpose if the layers have the same name in both grid maps

    return newGridMap;
}
