import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("breach_data_cleaned.csv")

# Extract email domain
df["domain"] = df["email"].str.split("@").str[-1]

# Count top domains
print("\n📧 Top email domains:")
print(df["domain"].value_counts())

# Count reused passwords
print("\n🔐 Reused passwords:")
print(df["password"].value_counts())

# Count breach sources
print("\n💥 Breach sources:")
print(df["breach_source"].value_counts())

# Convert to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["year"] = df["date"].dt.year

# Breaches per year
breach_per_year = df["year"].value_counts().sort_index()
print("\n📅 Breaches per year:")
print(breach_per_year)

# 📊 Visualize breaches per year
breach_per_year.plot(kind="bar", title="Breaches Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Breaches")
plt.tight_layout()
plt.show()

