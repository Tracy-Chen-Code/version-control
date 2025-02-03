from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("version.md", "w") as f:
    f.write(f"Last updated: {timestamp}
")

print("version.md updated")
