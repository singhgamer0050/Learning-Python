import    module
import random

courses = ["History", "Math", "Physics", "CompSci"]
index = module.find_index(courses,"CompSci")
print(index)
print(module.test)

random_courses = random.choice(courses)
print(random_courses)

import math
rads = math.radians(90)
print(math.sin(rads))

import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2017))

import os
print(os.getcwd)
print(os.__file__)