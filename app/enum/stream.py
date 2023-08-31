from enum import Enum


class Stream(str, Enum):
    REGULAR = "Regular"
    EVENING = "Evening"
    WEEKEND = "Weekend"
