import re
from collections import defaultdict

failed_logins = defaultdict(int)

log_file = input("Enter log file name: ")

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if ip_match:
                ip = ip_match.group()
                failed_logins[ip] += 1

print("\nSuspicious Activity Report\n")

for ip, count in failed_logins.items():
    if count >= 3:
        print(f"IP: {ip} | Failed attempts: {count}")
