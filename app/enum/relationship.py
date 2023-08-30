from enum import Enum

class Relationship(str, Enum):
    FATHER = "father"
    MOTHER = "mother"
    GUARDIAN = "guardian"
    BROTHER = "brother"
    SISTER = "sister"
    OTHER = "other"

