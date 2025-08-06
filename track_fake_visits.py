import pandas as pd

# Load the access logs
df = pd.read_csv("access_logs.csv", parse_dates=["timestamp"])

# ✅ Mock IP geolocation — add fake country info
ip_country_map = {
    "192.168.1.10": "Russia",
    "10.0.0.5": "China",
    "172.16.0.2": "Iran"
}
df["country"] = df["ip"].map(ip_country_map).fillna("Unknown")
df.to_csv("access_logs_with_country.csv", index=False)

# ✅ Count total visits per URL
url_counts = df['url'].value_counts()
print("\n📊 Total Visits Per URL:\n")
print(url_counts)

# ✅ Detect IPs that visit more than 5 times
ip_counts = df['ip'].value_counts()
suspicious_ips = ip_counts[ip_counts > 5]
print("\n🚨 Suspicious IPs (More than 5 visits):\n")
print(suspicious_ips)

# ✅ Detect visits to fake login pages
fake_login_keywords = ['login', 'trap']
fake_logins = df[df['url'].str.contains('|'.join(fake_login_keywords))]
top_fake_pages = fake_logins['url'].value_counts()
print("\n🎯 Most Accessed Fake Login Pages:\n")
print(top_fake_pages)

# ✅ Save results
url_counts.to_csv("url_visit_counts.csv")
suspicious_ips.to_csv("suspicious_ips.csv")
top_fake_pages.to_csv("fake_login_pages.csv")

# ✅ Detect burst attacks (10+ hits in 1 minute)
df['minute'] = df['timestamp'].dt.floor('min')  # Round to minute
burst_counts = df.groupby(['ip', 'minute']).size().reset_index(name='hit_count')
burst_ips = burst_counts[burst_counts['hit_count'] >= 10]
print("\n🕒 Burst Attack Detection (10+ hits/min):")
print(burst_ips)
burst_ips.to_csv("burst_attacks.csv", index=False)

# ✅ Add logic: IPs hitting multiple fake login pages
multi_fake_hits = fake_logins.groupby("ip")["url"].nunique().reset_index(name="unique_fake_pages")
multi_fake_hits = multi_fake_hits[multi_fake_hits["unique_fake_pages"] > 1]
print("\n👀 IPs Hitting Multiple Fake Login Pages:")
print(multi_fake_hits)
multi_fake_hits.to_csv("multiple_fake_page_hits.csv", index=False)

# ✅ Add logic: IPs with high visits AND burst attacks
high_volume_ips = set(suspicious_ips.index)
burst_ip_list = set(burst_ips['ip'])
combined = list(high_volume_ips & burst_ip_list)
print("\n🔥 IPs with High Visits AND Burst Attacks:")
print(combined)

# ✅ Bonus logic: suspicious countries hitting fake login pages
suspicious_countries = fake_logins[fake_logins['country'] != 'Unknown']
print("\n🌍 Suspicious Countries Accessing Fake Login Pages:")
print(suspicious_countries[['ip', 'url', 'country', 'timestamp']])
suspicious_countries.to_csv("fake_login_suspicious_countries.csv", index=False)

