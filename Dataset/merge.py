import pandas as pd
import glob

# Get all gesture CSVs
files = glob.glob("dataset/*.csv")                              #it means “Give me a list of all files inside the dataset folder that end with .csv.”
dfs = [pd.read_csv(f, header=None) for f in files]

# Merge into one DataFrame
full_data = pd.concat(dfs, ignore_index=True)

# Shuffle to prevent model memorizing order
full_data = full_data.sample(frac=1).reset_index(drop=True)

# saving merged dataset 
full_data.to_csv("dataset/all_gestures.csv", index=False)
print(" Merged dataset ready!")
