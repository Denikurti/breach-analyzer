import pandas as pd
from datetime import datetime

# Load the list of emails to check
emails_df = pd.read_csv("emails_to_check.csv")

# Load the breach dataset
breach_df = pd.read_csv("simulated_breach_data.csv")

# Convert the 'date' column to datetime format
breach_df["date"] = pd.to_datetime(breach_df["date"], errors="coerce")

# Filter for breaches in the last 5 years
cutoff_date = pd.Timestamp.now() - pd.DateOffset(years=5)
recent_breaches = breach_df[breach_df["date"] >= cutoff_date]

# Merge emails with recent breach data
matched_df = pd.merge(emails_df, recent_breaches, on="email", how="inner")

print("✅ Breached Emails in Last 5 Years:\n")
print(matched_df)

# Save results
matched_df.to_csv("breached_last_5_years.csv", index=False)
print("\n📁 Results saved to 'breached_last_5_years.csv'")

# --- Email Domain Analysis ---
print("\n📊 Email Domain Analysis:")

# Extract domains from email addresses
matched_df["domain"] = matched_df["email"].str.split("@").str[1]

# Count breaches per domain
domain_counts = matched_df["domain"].value_counts()

print(domain_counts)

# Save domain stats to CSV
domain_counts.to_csv("email_domain_stats.csv", header=["count"])
print("\n📁 Domain stats saved to 'email_domain_stats.csv'")

