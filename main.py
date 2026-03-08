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

# Load the CSV File to Read
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

#Count watch reasons
def count_watch_reasons(users):

    reason_count = {}

    for user in users:
        reason = user.watch_reason

        if reason not in reason_count:
            reason_count[reason] = 1
        else:
            reason_count[reason] += 1

    return reason_count

def build_summary_text(users) -> str:

    lines = []
    lines.append("Social Media Screen Time Analysis")
    lines.append("=================================")
    lines.append(f"Total users: {len(users)}")

    # Overall average
    avg = average_time(users)
    lines.append(f"Overall average usage (hours/month): {avg:.2f}")

    # Highest and Lowest
    highest, lowest = highest_and_lowest(users)

    if highest is not None:
        lines.append("")
        lines.append("Highest Usage User:")
        lines.append(
            f"User {highest.user_id} — {highest.total_time_spent} hours/month"
        )

        lines.append("")
        lines.append("Lowest Usage User:")
        lines.append(
            f"User {lowest.user_id} — {lowest.total_time_spent} hours/month"
        )

#Main Program
def main():

    filename = "screen_time.data"  # change if your file is named differently

    users = load_users(filename)

    print("Total Users:", len(users))
    print()

    # Print first 1000 users
    print("First 1000 Users:")
    limit = 1000
    if len(users) < 1000:
        limit = len(users)

    for i in range(limit):
        print("Index:", i, "UserID:", users[i].user_id)

    print()

    # Average
    average = average_time(users)
    print("Average Time Spent:", round(average, 2))
    print()

    # Highest & Lowest
    highest, lowest = highest_and_lowest(users)

    print("Highest Usage User:", highest.user_id, highest.total_time_spent)
    print("Lowest Usage User:", lowest.user_id, lowest.total_time_spent)
    print()

    # Watch reason dictionary
    reasons = count_watch_reasons(users)

    print("Watch Reason Counts:")
    for reason in reasons:
        print(reason, ":", reasons[reason])

    print()

    # High risk users
    print("High Risk Users (High usage + Debt):")
    for user in users:
        if user.high_risk():
            print("UserID:", user.user_id)

    print()
    print("Tip: Limiting screen time can improve productivity and financial wellbeing.")

    write_summary_file(users)

if __name__ == "__main__":
    main()

