import rosbag

# Function to get the list of topics from a ROS bag
def get_rosbag_topics(bag_file):
    with rosbag.Bag(bag_file, 'r') as bag:
        topics = bag.get_type_and_topic_info().topics.keys()
    return topics

# Function to read the list of expected topics from a text file
def read_expected_topics(file_path):
    with open(file_path, 'r') as file:
        expected_topics = [line.strip() for line in file.readlines()]
    return expected_topics

# Function to calculate the expected message count with a margin of error
def calculate_expected_message_count(bag_duration, margin=0.05):
    expected_count = int(bag_duration * 10)  # Calculate the expected count without margin
    lower_bound = int(expected_count * (1 - margin))
    upper_bound = int(expected_count * (1 + margin))
    return lower_bound, upper_bound

# Main function
def main():
    # Specify the path to your ROS bag file
    bag_file = 'your_rosbag.bag'

    # Specify the path to your text file containing the expected topics
    expected_topics_file = 'expected_topics.txt'

    # Get the list of topics from the ROS bag
    rosbag_topics = get_rosbag_topics(bag_file)

    # Read the list of expected topics from the text file
    expected_topics = read_expected_topics(expected_topics_file)

    # Check if any expected topics are missing from the ROS bag
    missing_topics = [topic for topic in expected_topics if topic not in rosbag_topics]

    if missing_topics:
        print("The following topics are missing from the ROS bag:")
        for topic in missing_topics:
            print(topic)
    else:
        print("All expected topics are present in the ROS bag.")

    # Check if topics have messages within an acceptable margin of error
    with rosbag.Bag(bag_file, 'r') as bag:
        bag_duration = bag.get_end_time() - bag.get_start_time()
        lower_bound, upper_bound = calculate_expected_message_count(bag_duration, margin=0.05)

        for topic in rosbag_topics:
            message_count = sum(1 for _ in bag.read_messages(topics=[topic]))
            if not (lower_bound <= message_count <= upper_bound):
                print(f"Topic '{topic}' does not have messages within an acceptable margin of error.")
                print(f"Expected: {lower_bound} <= Actual: {message_count} <= {upper_bound}")

if __name__ == "__main__":
    main()
