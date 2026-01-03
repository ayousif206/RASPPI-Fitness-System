from grapher import graphthree, graphfour, graphfive
import time
import numpy as np

def getmet(speed):
    if speed == 0:
        return 1.8
    if speed < 2.5 and speed != 0:
        return 2.4
    if 2.5 <= speed < 3:
        return 3
    elif 3 <= speed < 3.5:
        return 3.3
    elif 3.5 <= speed < 4:
        return 3.5
    elif 4 <= speed < 4.5:
        return 4.3
    elif 4.5 <= speed < 5:
        return 5.3
    elif 5 <= speed < 6:
        return 6
    elif 6 <= speed < 6.7:
        return 8.3
    elif 6.7 <= speed < 7:
        return 9
    elif 7 <= speed < 7.5:
        return 9.8
    elif 7.5 <= speed < 8:
        return 10.5
    elif 8 <= speed < 8.6:
        return 11
    elif 8.6 <= speed < 9:
        return 11.5
    elif 9 <= speed < 10:
        return 11.8
    elif 10 <= speed < 11:
        return 12.3
    elif 11 <= speed < 12:
        return 12.8
    elif 12 <= speed < 13:
        return 14.5
    elif 13 <= speed < 14:
        return 16
    elif speed >= 14:
        return 19.8
    else:
        return 0

def caloriesspeedcalc(dataranges, weight, distance, elapsedtime, bmr):
    elapsedtimehours = elapsedtime/3600
    
    if elapsedtimehours != 0:
        avgspeed = (distance/elapsedtimehours)

    else:
        avgspeed = 0

    if len(dataranges["distance"]) >= 2:
        speed = ((dataranges["distance"][-1] - dataranges["distance"][-2])/(dataranges["time"][-1] - dataranges["time"][-2]))*3600

    else:
        speed = 0

    met = getmet(speed)
    
    if len(dataranges["caloriesburned"]) == 0:
           burnedcal = 0
    else:
        burnedcal = dataranges["caloriesburned"][-1]

    if len(dataranges["time"]) >= 2:
        burnedcal += ((met*bmr)/24*((dataranges["time"][-1] - dataranges["time"][-2])/3600))
    elif len(dataranges["time"]) == 1:
        burnedcal = ((met*bmr)/24*elapsedtimehours)
    else:
        burnedcal = 0

    return burnedcal, speed, avgspeed

def updatedata(dataranges, elapsedtime, distance, speed, burnedcal):
    dataranges["time"].append(elapsedtime)
    dataranges["distance"].append(distance)
    dataranges["speed"].append(speed)
    dataranges["caloriesburned"].append(burnedcal)
    return dataranges

def updatevisual(frame, dataranges, atspeedlabel, avgspeedlabel, distancelabel, caloriesburnedlabel, stepstakenlabel, elapsedtimelabel, elapsedtime, distance, steps, caloriesburned, speed, avgspeed):
    stepstakenlabel.config(text=f"Steps: {round(steps, 2)}")
    distancelabel.config(text=f"Distance: {round(distance, 2)}")
    avgspeedlabel.config(text=f"Average Speed: {round(avgspeed, 2)}")
    atspeedlabel.config(text=f"Current Speed: {round(speed, 2)}")
    caloriesburnedlabel.config(text=f"Calories Burned: {round(caloriesburned, 2)}")
    elapsedtimelabel.config(text=f"Elapsed Time: {round(elapsedtime, 2)}")
    graphthree(dataranges["time"], dataranges["distance"], frame, False)
    graphfour(dataranges["time"], dataranges["speed"], frame, False)
    graphfive(dataranges["time"], dataranges["caloriesburned"], frame, False)
