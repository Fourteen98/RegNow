from enum import Enum

import pycountry


class Nationality(str, Enum):
    @classmethod
    def choices(cls):
        return [(country.alpha_2, country.name)
                for country in pycountry.countries]


class Gender(str, Enum):
    Boy = "Male"
    Girl = "Female"
    other = "Others"


class ProgrammeName(str, Enum):
    Computer_Network = "Computer Network"
    Computer_Science = "Computer Science"
    Hospitality = "Hospitality"
    Mech_Engineering = "Mechanical Engineering"
    Food_Science = "Food Science"


class Stream(str, Enum):
    Regular = "Regular"
    Evening = "Evening"
    Weekends = "Weekends"


class EntryLevel(str, Enum):
    Level_100 = "Level 100"
    Level_200 = "Level 200"
    Level_300 = "Level 300"
    Level_400 = "Level 400"


class Hall(str, Enum):
    hall_1 = "Afrifa"
    hall_2 = "Bosco"
    hall_3 = "McArthur"
    hall_4 = "Godwell"
