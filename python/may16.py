import datetime

# print(dir(datetime))

krushnam = datetime.datetime(2006, 9, 17, 12, 13)
khush = datetime.datetime(2003, 12, 25)

# print(krushnam)
# print(krushnam - khush)

# nihar = datetime.date(2004, 7, 1)
# gap = datetime.timedelta(100)
# print(nihar + gap)

# gap = datetime.timedelta(-100)
# print(nihar - gap)

# print(krushnam.day)
# print(krushnam.month)
# print(krushnam.year)
# print(krushnam.date())

# exam_time = datetime.time(14, 00, 00)

aaj_ni_tarikh = datetime.datetime.today()
# print(aaj_ni_tarikh)
nihar = datetime.datetime(2004, 7, 1)

# print(f"Khush: {aaj_ni_tarikh - khush} Days")
# print(f"Nihar: {aaj_ni_tarikh - nihar} Days")
# print(f"Krushnam: {aaj_ni_tarikh - krushnam} Days")

dob_year = int(input("Year of birth:"))
dob_month = int(input("Month of birth:"))
dob_date = int(input("Date of birth:"))
dob = datetime.datetime(dob_year, dob_month, dob_date)
# print(f"Your age: {aaj_ni_tarikh - dob} Days")

print(dob.date())
# Next Class: strptime, strftime