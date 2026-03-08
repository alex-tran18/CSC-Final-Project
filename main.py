import csv
import math
import data
from data import User

# Convert Debt String into Boolean
def convert_bool(tf:str) -> bool:
    tf = str(tf).strip().lower()
    if tf == "true":
        return True
    elif tf == "false":
        return False