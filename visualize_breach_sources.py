import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("breached_emails_found.csv")

# Count breaches per source
breach_counts = df["breach_source"].value_counts()

# Plot
breach_counts.plot(kind="bar", title="Breached Emails by Source", figsize=(8,5))
plt.ylabel("Number of Emails")
plt.xlabel("Breach Source")
plt.tight_layout()
plt.show()

