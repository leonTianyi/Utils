# Function to combine data from multiple CSV files
def combine_csv_files(folder_path):
    combined_x = []
    combined_y = []
    combined_pot = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            metric_df = pd.read_csv(file_path)

            x = metric_df[metric_df.columns[0]].values
            y = metric_df[metric_df.columns[1]].values
            pot = metric_df[metric_df.columns[2]].values

            combined_x.extend(x)
            combined_y.extend(y)
            combined_pot.extend(pot)

    return np.array(combined_x), np.array(combined_y), np.array(combined_pot)
