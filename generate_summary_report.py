import pandas as pd

# Load the filtered breaches from the last 5 years
df = pd.read_csv("breached_last_5_years.csv")

# Total number of breached emails
total_breached = len(df)

# Most common email domains
df['domain'] = df['email'].apply(lambda x: x.split('@')[-1])
top_domains = df['domain'].value_counts().head(5)

# Most common breach sources
top_sources = df['breach_source'].value_counts().head(5)

# Save summary to CSV
summary_data = {
    "Metric": ["Total Breached Emails", "Top Domain", "Second Domain", "Top Breach Source", "Second Breach Source"],
    "Value": [
        total_breached,
        top_domains.index[0] if len(top_domains) > 0 else "N/A",
        top_domains.index[1] if len(top_domains) > 1 else "N/A",
        top_sources.index[0] if len(top_sources) > 0 else "N/A",
        top_sources.index[1] if len(top_sources) > 1 else "N/A",
    ]
}

summary_df = pd.DataFrame(summary_data)
summary_df.to_csv("breach_summary_report.csv", index=False)

print("📄 Summary report saved to 'breach_summary_report.csv'")

