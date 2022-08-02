def add_time(time, hours, day=None):
    dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    getHour = ""
    enter = True
    sum = time_to_int(time) + time_to_int(hours)
    getMin = str(sum)
    x = len(getMin)
    getMin = getMin[x - 2] + getMin[x - 1]
    (getMin, secondI) = whileGetHour(int(getMin), 60)
    sum = sum + secondI * 100

    # for a in range(0, x - 2):
    #     getHour = getHour + str(sum)[a]

    (hour, i) = whileGetHour(sum, 1200)
    if len(str(hour)) < 3:
        getHour = "12"
    for a in range(0, len(str(hour))-2):
        getHour = getHour + str(hour)[a]
    superI = secondI + i
    (state, day, nextDay) = getDay(dayList, superI, day, time)
    getMin = str(getMin)

    if len(getMin) == 1:
        getMin = "0" + getMin
    if int(getHour) > 12:
        getHour = str(int(getHour) - 12)
    final = getHour + ":" + getMin + " "

    if i % 2 == 0:
        final = final + state
    else:
        final = final + defState(state)
    if day != None:
        final = final + " " + day
        if superI / 2 > 1:
            final = final + " (" + str((superI / 2) + 0.5)[0] + " days later)"
            enter = False
    if enter:
        if day == "":
            if nextDay or (i == 1 and state == "PM"):
                final = final + " (next day)"
            elif i > 1:
                final = final + " " + str(i) + "days later"

    print(final)


def time_to_int(str):
    number = ""
    for a in str:
        if a.isdigit():
            number = number + a

    return int(number)


def getDay(dayList, i, day, time):
    nextDay = False
    if time.__contains__("PM"):
        state = "PM"
    else:
        state = "AM"
    if day != None:
        findDay = dayList.index(day)

        if i != 0:
            if state == "AM":
                (sum, i) = whileGetHour(i, 2)
                i = i - 1
                nextDay = True;
            else:
                if i > 1:
                    (sum, i) = whileGetHour(i, 2)
                    i = i + 1
                nextDay = True;

        i = i % 7
        return state, dayList[i], nextDay
    return state, "", nextDay


def whileGetHour(sum, size):
    i = 0
    while sum >= size:
        sum = sum - size
        i = i + 1

    return sum, i


def defState(state):
    state = "AM" if state == "PM" else "PM"
    return state


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

#
add_time("11:43 PM", "24:20", "Tuesday")
# # Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
