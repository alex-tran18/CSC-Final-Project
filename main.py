import csv
from data import User

# Convert Debt String into Boolean
def convert_bool(tf:str) -> bool:
    tf = str(tf).strip().lower()
    if tf == "true":
        return True
    elif tf == "false":
        return False
    else:
        return False

# Load the CSV File
def load_users(filename):
    users = []
    file = open(filename, 'r')
    reader = csv.DictReader(file)

    for row in reader:
        user = User(
            int(row["user_id"]),
            float(row["total_time_spent"]),
            float(row["productivity_loss"]),
            row["watch_reason"],
            convert_bool(row["Debt"])
        )
        users.append(user)
    file.close()
    return users

# Calculate Average Screen Time of Each User
def average_time(users):
    total = 0
    for user in users:
        total += user.total_time_spent
    return total / len(users)

# Find the highest and lowest usage
def highest_and_lowest(users):
    highest = users[0]
    lowest = users[0]
    for user in users:
        if user.total_time_spent > highest.total_time_spent:
            highest = user
        if user.total_time_spent < lowest.total_time_spent:
            lowest = user
    return highest, lowest