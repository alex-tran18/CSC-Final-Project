class User:
    # Initializes a new User object
    # input: the user's ID as an integer
    # input: the total time spent on social media(in hours per month) as a float or integer
    # input: productivity loss score as a float or integer
    # input: watch reason as a string
    # input: debt status as a boolean
    def __init__(self, user_id, total_time_spent, productivity_loss, watch_reason, debt):
        self.user_id = user_id
        self.total_time_spent = total_time_spent
        self.productivity_loss = productivity_loss
        self.watch_reason = watch_reason
        self.debt = debt

    #Provide a developer-friendly string representation of the object User.
    # input: User object for which a string representation is desire
    # output: string representation
    def __repr__(self):
        return 'User({}, {}, {}, {}, {})'.format(
            self.user_id,
            self.total_time_spent,
            self.productivity_loss,
            self.watch_reason,
            self.debt
        )
    # Assign the user to usage level
    def assign_usage_level(self):
        if self.total_time_spent < 100:
            return "low"
        if self.total_time_spent < 200:
            return "medium"
        else:
            return "high"

    def calculate_productivity_ratio(self):
        if self.total_time_spent == 0:
            return 0
        return self.productivity_loss / self.total_time_spent

    def high_risk(self):
        return self.assign_usage_level() == "high" and self.debt == True
