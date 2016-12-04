daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(y1,y2):



    if y1 % 400 == 0 or y2 % 400 == 0:
        return True
    if y1 % 100 == 0 or y2 % 100 == 0:
        return False
    if y1 % 4 == 0 or y2 % 4 == 0:
        return True
    else:
        return False


    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##

def daysBetweenDates(y1, m1, d1, y2, m2, d2):


    totalDays = 0

    while y1 != y2:
        if isLeapYear(y1,y2) == True:
            daysOfYear = 366
        if isLeapYear(y1,y2) == False:
            daysOfYear = 365
        totalDays = totalDays + daysOfYear
        y2 = y2 - 1



    daysLefty1 = 0
    i = 0

    while i < m1:

        if isLeapYear(y1,y2) == True:
            daysOfMonths[1] = 29

        daysLefty1 = daysLefty1 + daysOfMonths[i-1]


        i = i + 1


    daysLefty2 = 0
    e = 0

    while e < m2:

        if isLeapYear(y1,y2) == True:
            daysOfMonths[1] = 29

        daysLefty2 = daysLefty2 + daysOfMonths[e-1]

        e = e + 1



    days = totalDays + daysLefty2 + d2 - daysLefty1 - d1

    return days


print (daysBetweenDates(1987, 3, 20, 2016, 6, 8))
