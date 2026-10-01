import pandas as pd

# Load the Netflix dataset
df = pd.read_csv("netflix_titles.csv")

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["date_added"] = df["date_added"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")
df["duration"] = df["duration"].fillna("Unknown")

# Check missing values after cleaning
print("MISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Display first 5 rows
print("\nFIRST 5 ROWS:")
print(df.head())
# Save the cleaned dataset
df.to_csv("netflix_titles_cleaned.csv", index=False)

print("\nCLEANED DATASET SAVED SUCCESSFULLY!")