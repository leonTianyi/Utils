import csv
import os
import matplotlib.pyplot as plt

# Specify the folder path containing the CSV files
folder_path = "path/to/folder"

# Initialize a dictionary to store the computation times for each setting
computation_times = {}

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        # Extract the setting from the file name
        setting = filename.split(".")[0]  # Assuming the file name is in the format "setting.csv"
        # Open the CSV file
        with open(file_path, "r") as csvfile:
            # Read the CSV file as a dictionary
            reader = csv.DictReader(csvfile)
            # Initialize variables for calculating the average per file
            total = 0
            count = 0
            # Loop through each row in the CSV file
            for row in reader:
                # Check if the "GroundSurface" item exists in the row
                if "GroundSurface" in row and row["GroundSurface"]:
                    # Add the value to the total
                    total += float(row["GroundSurface"])
                    # Increment the count
                    count += 1
            # Calculate the average per file
            if count > 0:
                average = total / count
                computation_times[setting] = average

# Create a bar plot of the computation times
settings = computation_times.keys()
times = computation_times.values()

plt.figure(figsize=(12, 6))
plt.bar(settings, times)
plt.axhline(y=10, color='red', linestyle='--')
plt.xticks(rotation=45)
plt.xlabel("Setting")
plt.ylabel("Computation Time (seconds)")
plt.title("Computation Times for Different Settings")
plt.show()
