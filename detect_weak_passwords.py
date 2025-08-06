import pandas as pd

# List of weak passwords
weak_passwords = ["123456", "password", "qwerty", "letmein", "admin123", "12345678"]

# Load the breach dataset
breach_df = pd.read_csv("simulated_breach_data.csv")

# Check for weak passwords
weak_df = breach_df[breach_df["password"].isin(weak_passwords)]

print("🔐 Weak Passwords Detected:\n")
print(weak_df)

# Save the results
weak_df.to_csv("weak_passwords_found.csv", index=False)
print("\n📁 Saved to 'weak_passwords_found.csv'")

