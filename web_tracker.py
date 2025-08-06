import random
from datetime import datetime

# Define fake paths
fake_paths = ["/login", "/dashboard", "/logout", "/settings", "/profile"]

# Simulate fake visitors (IP + Path)
fake_ips = ["192.168.1." + str(i) for i in range(1, 6)]  # Simulate IPs from .1 to .5

# Log file
log_file = "access_logs.txt"

# Write simulated logs
with open(log_file, "a") as f:
    for _ in range(20):
        ip = random.choice(fake_ips)
        path = random.choice(fake_paths)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {ip} visited {path}\n")

print("✅ 20 fake visits logged to access_logs.txt")
