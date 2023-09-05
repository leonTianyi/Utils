#!/bin/bash

# Check if ROS workspace is sourced
if [ -z "$ROS_DISTRO" ]; then
  echo "Error: ROS workspace is not sourced. Run 'source /opt/ros/<your-ros-distro>/setup.bash' first."
  exit 1
fi

# Check if the 'rosbag' package is installed
if ! command -v rosbag &>/dev/null; then
  echo "Error: 'rosbag' command not found. Make sure ROS is installed."
  exit 1
fi

# Check if the topics file and output bag file arguments are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <topics_file> <output_bag_file>"
  exit 1
fi

TOPICS_FILE="$1"
OUTPUT_BAG="$2"

# Check if the topics file exists and read topics from it
if [ ! -f "$TOPICS_FILE" ]; then
  echo "Error: Topics file '$TOPICS_FILE' not found."
  exit 1
fi

# Read topics from the file into an array
TOPICS=($(<"$TOPICS_FILE"))

# Check if any topics are specified
if [ ${#TOPICS[@]} -eq 0 ]; then
  echo "Error: No topics specified for recording in '$TOPICS_FILE'."
  exit 1
fi

# Start recording the bag file
rosbag record -O "$OUTPUT_BAG" ${TOPICS[@]}

echo "Recording topics from '$TOPICS_FILE' to '$OUTPUT_BAG'"
