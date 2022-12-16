SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

day = (1 * DAY) // SECOND
week = (7 * DAY) // MINUTE
month = (31 * DAY) // HOUR
workday = (8 * HOUR) // SECOND
workweek = (5 * workday) // MINUTE
workmonth = (22 * workday) // HOUR

print(day, week, month, workday, workweek, workmonth)