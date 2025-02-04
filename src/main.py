import datetime

now = datetime.datetime.now()

with open("version.md", "w") as file:
    file.write(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

