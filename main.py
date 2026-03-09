import csv
from data import User

# Convert Debt String into Booleans
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
            int(row["UserID"]),
            float(row["Total Time Spent"]),
            float(row["ProductivityLoss"]),
            convert_bool(row["Debt"])
        )
        users.append(user)
    file.close()
    return users

# Calculate Average Screen Time of Each User
def average_time(users):
    if len(users) == 0:
        return 0

    total = 0
    for user in users:
        total += user.total_time_spent
    return total / len(users)

# Find the highest and lowest usage
def highest_and_lowest(users):
    if len(users) == 0:
        return [None, None]

    highest = users[0]
    lowest = users[0]

    for user in users:
        if user.total_time_spent > highest.total_time_spent:
            highest = user
        if user.total_time_spent < lowest.total_time_spent:
            lowest = user
    return [highest, lowest]

#Correlation between time and debt
def correlation_time_and_debt(users):
    if len(users) == 0:
        return 0

    xs = [] #total_time_spent
    ys = [] #debt as 0/1

    for user in users:
        xs.append(user.total_time_spent)
        ys.append(1 if user.debt else 0)

    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)

    numerator = 0
    denominator_x = 0
    denominator_y = 0

    for i in range(len(xs)):
        dx = xs[i] - mean_x
        dy = ys[i] - mean_y
        numerator += dx * dy
        denominator_x += dx * dx
        denominator_y += dy * dy

    if denominator_x == 0 or denominator_y == 0:
        return 0

    return numerator / ((denominator_x ** 0.5) * (denominator_y ** 0.5))

def average_productivity_ratio(users):
    if not users:
        return 0
    return sum(u.calculate_productivity_ratio() for u in users) / len(users)

def average_time_by_debt(users):
    debt_total = 0
    debt_count = 0
    no_debt_total = 0
    no_debt_count = 0

    for user in users:
        if user.debt:
            debt_total += user.total_time_spent
            debt_count += 1
        else:
            no_debt_total += user.total_time_spent
            no_debt_count += 1

    debt_avg = 0
    if debt_count != 0:
        debt_avg = debt_total / debt_count

    no_debt_avg = 0
    if no_debt_count != 0:
        no_debt_avg = no_debt_total / no_debt_count

    return [debt_avg, no_debt_avg, debt_count, no_debt_count]

#Summary text
def build_summary_text(users) -> str:

    lines = []
    lines.append("Social Media Screen Time Analysis")
    lines.append("=================================")
    lines.append(f"Total users: {len(users)}")

    # Overall average
    avg = average_time(users)
    lines.append(f"Overall average usage (hours/month): {avg:.2f}")

    # Highest and Lowest
    result = highest_and_lowest(users)
    highest = result[0]
    lowest = result[1]

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

    # correlation
    lines.append("")
    corr = correlation_time_and_debt(users)
    lines.append(f"Correlation (Screen Time vs Debt): {corr:.3f}")

    # debt insight
    lines.append("")
    lines.append("Debt vs Screen Time:")
    stats = average_time_by_debt(users)
    lines.append(f"Avg time (Debt): {stats[0]:.2f} hours/month | Users: {stats[2]}")
    lines.append(f"Avg time (No Debt): {stats[1]:.2f} hours/month | Users: {stats[3]}")
    lines.append(f"Difference (Debt - No Debt): {(stats[0] - stats[1]):.2f}")

    # Average Productivity Ratios
    avg_ratio = average_productivity_ratio(users)
    lines.append("")
    lines.append(f"Average Productivity Ratio: {avg_ratio:.3f}")

    # Productivity ratios
    lines.append("")
    lines.append("Productivity Ratios (loss/time):")

    if len(users) == 0:
        lines.append("No users available.")
    else:
        for user in users:
            ratio = user.calculate_productivity_ratio()
            lines.append(f"User {user.user_id}: {ratio:.3f}")

    # Social responsibility message
    lines.append("")
    lines.append("Social Impact Insight:")
    lines.append("Higher screen time appears to be associated with increased likelihood of debt.")
    lines.append("Users with debt tend to spend more time on social media compared to those without debt.")
    lines.append("Encouraging healthier digital habits can improve focus and financial stability and productivity.")

    return "\n".join(lines)

def write_summary_file(users, filename="summary.txt"):
    text = build_summary_text(users)
    with open(filename, "w") as file:
        file.write(text)


#Main Program
def main():

    filename = "screen_time.data"  # change if your file is named differently

    users = load_users(filename)

    print("Total Users:", len(users))
    print()

    # Print first 1000 users
    print("Sample Users: ")
    for u in users[:100]:
        print(u)

    # Average time
    average = average_time(users)
    print("Average Time Spent:", round(average, 2))
    print()

    # Highest & Lowest
    result = highest_and_lowest(users)
    highest = result[0]
    lowest = result[1]

    print("Highest Usage User:", highest.user_id, highest.total_time_spent)
    print("Lowest Usage User:", lowest.user_id, lowest.total_time_spent)
    print()

    # Correlation between screen time and debt
    corr = correlation_time_and_debt(users)

    print("Correlation (Screen Time vs Debt):", round(corr, 3))
    print("Note: positive value means more screen time is associated with higher likelihood of debt.")
    print()

    # High risk users
    print("Users with High Screen Time and Debt:")
    for user in users:
        if user.high_risk():
            print("UserID:", user.user_id)

    print()
    print("Tip: Limiting screen time can improve productivity and financial wellbeing.")

    # Productivity Ratio
    avg_ratio = average_productivity_ratio(users)
    print("Average Productivity Ratio:", round(avg_ratio, 3))
    print()

    # average time w debt
    stats = average_time_by_debt(users)
    avg_debt = stats[0]
    avg_no_debt = stats[1]
    debt_count = stats[2]
    no_debt_count = stats[3]

    print("---- Debt vs Screen Time ----")
    print("Users WITH debt:", debt_count, "| Avg screen time:", round(avg_debt, 2))
    print("Users WITHOUT debt:", no_debt_count, "| Avg screen time:", round(avg_no_debt, 2))
    print("Difference (Debt - No Debt):", round(avg_debt - avg_no_debt, 2))
    print()

    write_summary_file(users)

if __name__ == "__main__":
    main()



