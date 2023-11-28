### dayOfTheWeek 
import datetime
from typing import *
def f_gold(day: int, month: int, year: int) -> str:
    return datetime.date(year, month, day).strftime('%A')