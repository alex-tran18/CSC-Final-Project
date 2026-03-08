import csv
import data
from data import User

# Convert Debt String into Boolean
def convert_bool(tf:str) -> bool:
    tf = str(tf).strip().lower()
    if tf == "true":
        return True
    elif tf == "false":
        return False


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

#Main Program
def main():
    filename = "screen_time.data"

    users = load_users_from_screentime_data(filename)

    print("Total users: ", len(users))
    print()

    #Print first 100 users
    print("First 100 users")
    limit = 100
    if len(users) < 100:
        limit = len(users)

    for i in range(limit):
        print("Index:", i, "UserID: ", users[i].user_id)
    print()

    #Average
    average = calculate_average_time(users)
    print("Average Time Spent: ", round(average, 2))
    print()

    #Highest and Lowest
    result = find_highest_and_lowest(users)

    highest = result[0]
    lowest = result[1]

    print("Highest Usage User: ", highest.user_id, highest.total_time_spent)
    print("Lowest Usage User: ", lowest.user_id, lowest.total_time_spent)
    print()

    # Watch reason dictionary
    reasons = count_watch_reasons(users)

    print("Watch Reason Counts: ")
    for reason in reasons:
        print(reason, ";", reasons[reason])

    print()

    # High risk users
    print("High Risk users (High usage and debt): ")
    for user in users:
        if user.high_risk():
            print("User ID: ", user.user_id)

    print()
    print("Tip: LImiting screen time can improve producitivity and financial wellbeing.")

main()