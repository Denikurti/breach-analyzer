import pandas as pd

# Load the email metadata
df = pd.read_csv("emails_metadata.csv")

# Define suspicious patterns
suspicious_domains = ["micros0ft.com", "phishmail.ru"]
suspicious_subject_keywords = ["urgent", "verify", "account", "security", "alert"]
link_threshold = 2  # If email has 2+ links and attachment

# Detection logic
def is_suspicious(row):
    domain = row["sender"].split("@")[-1].lower()
    subject = str(row["subject"]).lower()
    
    if any(word in subject for word in suspicious_subject_keywords):
        return True
    if domain in suspicious_domains:
        return True
    if row["has_attachment"] and row["link_count"] >= link_threshold:
        return True
    return False

# Apply detection
df["suspicious"] = df.apply(is_suspicious, axis=1)

# Show only suspicious ones
suspicious_df = df[df["suspicious"] == True]

print("🚨 Suspicious Emails Detected:\n")
print(suspicious_df[["sender", "subject", "timestamp"]])

# Save to file
suspicious_df.to_csv("suspicious_emails_found.csv", index=False)
print("\n📁 Results saved to 'suspicious_emails_found.csv'")

