# COVID-19 Data Analysis
# Step 1: Load and Clean Data

import pandas as pd

# --------------------------------------------------
# 1. Load the dataset
# --------------------------------------------------

file_path = r"C:\Users\likit\OneDrive\Documents\covid 19\data\Covid19 India (Jan 20 - Mar 20).csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("-" * 50)

# --------------------------------------------------
# 2. Display first 5 rows
# --------------------------------------------------

print("\nFirst 5 rows:")
print(df.head())

# --------------------------------------------------
# 3. Display number of rows and columns
# --------------------------------------------------

print("\nDataset shape:")
print(df.shape)

# --------------------------------------------------
# 4. Display column names
# --------------------------------------------------

print("\nColumn names:")
print(df.columns.tolist())

# --------------------------------------------------
# 5. Check data types
# --------------------------------------------------

print("\nData types:")
print(df.dtypes)

# --------------------------------------------------
# 6. Check missing values
# --------------------------------------------------

print("\nMissing values:")
print(df.isnull().sum())

# --------------------------------------------------
# 7. Check duplicate rows
# --------------------------------------------------

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# --------------------------------------------------
# 8. Remove duplicate rows
# --------------------------------------------------

df = df.drop_duplicates()

print("\nDuplicates removed.")

# --------------------------------------------------
# 9. Convert Date column
# --------------------------------------------------

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# --------------------------------------------------
# 10. Fill missing numerical values
# --------------------------------------------------

numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(0)

# --------------------------------------------------
# 11. Check cleaned data
# --------------------------------------------------

print("\nCleaned dataset:")
print(df.head())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --------------------------------------------------
# 12. Save cleaned dataset
# --------------------------------------------------

df.to_csv(r"C:\Users\likit\OneDrive\Documents\covid 19\data\covid19_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")