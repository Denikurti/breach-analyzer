import pandas as pd

# Load the data
df = pd.read_csv("breach_data.csv")
print("🔢 Rows loaded:", len(df))

# Show first few rows
print("\n🧾 Sample rows:")
print(df.head())

# Remove duplicates
df = df.drop_duplicates()

# Check for missing values
print("\n❓ Missing values:")
print(df.isnull().sum())

# Normalize email domain
df["domain"] = df["email"].apply(lambda x: x.split("@")[-1].lower())

# Save cleaned version
df.to_csv("breach_data_cleaned.csv", index=False)
print("\n✅ Cleaned data saved as 'breach_data_cleaned.csv'")

