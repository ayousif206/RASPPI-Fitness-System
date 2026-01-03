from cryptography.exceptions import InvalidSignature
from cryptography.fernet import InvalidToken
from tkinter import ttk
from math import isnan
import tkinter as tk
import challenges
import binascii
import grapher
import active
import camera
import encdec
import random
import reglog
import time
import sys
import os

def createregisterframe(notebook, switcher):
    registerframe = ttk.Frame(notebook)

    failedattempt1 = tk.Label(registerframe, text="")

    usernamelabel = tk.Label(registerframe, text="Username")
    usernameentry = tk.Entry(registerframe, width=30)

    passwordlabel = tk.Label(registerframe, text="Password")
    passwordentry = tk.Entry(registerframe, width=30, show="*")

    confirmpasswordlabel = tk.Label(registerframe, text="Confirm Password")
    confirmpasswordentry = tk.Entry(registerframe, width=30, show="*")

    registerbutton = tk.Button(registerframe, text="Register", command=lambda: getregisterinputs(failedattempt1, usernameentry.get(), passwordentry.get(), confirmpasswordentry.get()))

    switchtologinbutton = tk.Label(registerframe, text="Already have an account? Click here to login", fg="blue", cursor="hand2")
    switchtologinbutton.bind("<Button-1>", switcher)

    usernamelabel.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    usernameentry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    passwordlabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    passwordentry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    confirmpasswordlabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    confirmpasswordentry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    failedattempt1.place(relx=0.5, rely=0.665, anchor=tk.CENTER)

    registerbutton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    switchtologinbutton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    return registerframe

def createloginframe(notebook, switcher, switcher2, root):
    loginframe = ttk.Frame(notebook)

    failedattempt2 = tk.Label(loginframe, text="", fg="red")

    usernamelabel = tk.Label(loginframe, text="Username")
    usernameentry = tk.Entry(loginframe, width=30)

    passwordlabel = tk.Label(loginframe, text="Password")
    passwordentry = tk.Entry(loginframe, width=30, show="*")

    loginbutton = tk.Button(loginframe, text="Login", command=lambda: getlogininputs(root, switcher2, failedattempt2, usernameentry.get(), passwordentry.get()))

    switchtoregisterbutton = tk.Label(loginframe, text="Don't have an account? Click here to register", fg="blue", cursor="hand2")
    switchtoregisterbutton.bind("<Button-1>", switcher)

    usernamelabel.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    usernameentry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    passwordlabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    passwordentry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    failedattempt2.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    loginbutton.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    switchtoregisterbutton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    return loginframe

def createtrackerframe(notebook, username):
    trackerframe = ttk.Frame(notebook)

    target1 = tk.Label(trackerframe, text="", fg="lime")
    target2 = tk.Label(trackerframe, text="", fg="lime")
    target3 = tk.Label(trackerframe, text="", fg="red", font=("Helvetica", 15, "bold"))
    target4 = tk.Label(trackerframe, text="", fg="red", font=("Helvetica", 15, "bold"))

    grapher.graphdatahandler(username, target1, target2, target3, target4, None, None, trackerframe, True, 1)
    grapher.graphdatahandler(username, target1, target2, target3, target4, None, None, trackerframe, True, 2)
    
    graph1 = tk.Label(trackerframe, text="Weight over Time", font=("Helvetica", 10, "bold"))
    graph1.place(relx=0.25, rely=0.475, anchor=tk.CENTER)

    xaxis1 = tk.Label(trackerframe, text="Time in Days", font=("Helvetica", 10, "bold"))
    xaxis1.place(relx=0.25, rely=0.975, anchor=tk.CENTER)

    yaxis1canvas = tk.Canvas(trackerframe, width=30, height=200)
    yaxis1canvas.place(relx=0.025, rely=0.7, anchor=tk.CENTER)
    yaxis1 = yaxis1canvas.create_text(15, 100, text="Weight in Kilograms", anchor=tk.CENTER, font=("Helvetica", 10, "bold"))
    yaxis1canvas.itemconfigure(yaxis1, angle=90)

    graph2 = tk.Label(trackerframe, text="Calories over Time", font=("Helvetica", 10, "bold"))
    graph2.place(relx=0.75, rely=0.475, anchor=tk.CENTER)

    xaxis2 = tk.Label(trackerframe, text="Time in Hours", font=("Helvetica", 10, "bold"))
    xaxis2.place(relx=0.75, rely=0.975, anchor=tk.CENTER)

    yaxis2canvas = tk.Canvas(trackerframe, width=30, height=200)
    yaxis2canvas.place(relx=0.525, rely=0.7, anchor=tk.CENTER)
    yaxis2 = yaxis2canvas.create_text(15, 100, text="Calories in Kilocalories", anchor=tk.CENTER, font=("Helvetica", 10, "bold"))
    yaxis2canvas.itemconfigure(yaxis2, angle=90)

    desiredweightlabel = tk.Label(trackerframe, text="Desired Weight")
    desiredweightentry = tk.Entry(trackerframe, width=30)

    weightinputlabel = tk.Label(trackerframe, text="Weight Input")
    weightinputentry = tk.Entry(trackerframe, width=30)

    desiredcalorieslabel = tk.Label(trackerframe, text="Caloric Expenditure")
    desiredcaloriesentry = tk.Entry(trackerframe, width=30)

    caloriesinputlabel = tk.Label(trackerframe, text="Calories Input")
    caloriesinputentry = tk.Entry(trackerframe, width=30)

    updateweightbutton = tk.Button(trackerframe, text="Update Desired Weight", command=lambda: passtographhandle(username, target1, target2, target3, target4, desiredweightentry.get(), 1, trackerframe, 1))
    addweightbutton = tk.Button(trackerframe, text="Add New Weight", command=lambda: passtographhandle(username, target1, target2, target3, target4, weightinputentry.get(), 2, trackerframe, 1))
    resetweightbutton = tk.Button(trackerframe, text="Reset Weight", fg="red", command=lambda:passtographhandle(username, target1, target2, target3, target4, 0, 3, trackerframe, 1))

    updatecaloriesbutton = tk.Button(trackerframe, text="Update Caloric Expenditure", command=lambda: passtographhandle(username, target1, target2, target3, target4, desiredcaloriesentry.get(), 1, trackerframe, 2))
    addcaloriesbutton = tk.Button(trackerframe, text="Add Caloric Intake", command=lambda: passtographhandle(username, target1, target2, target3, target4, caloriesinputentry.get(), 2, trackerframe, 2))
    resetcaloriesbutton = tk.Button(trackerframe, text="New Day", fg="red", command=lambda:passtographhandle(username, target1, target2, target3, target4, 0, 3, trackerframe, 2))
    
    desiredweightlabel.place(relx=0.2, rely=0.1, anchor=tk.CENTER)
    desiredweightentry.place(relx=0.2, rely=0.15, anchor=tk.CENTER)
    updateweightbutton.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

    weightinputlabel.place(relx=0.2, rely=0.25, anchor=tk.CENTER)
    weightinputentry.place(relx=0.2, rely=0.3, anchor=tk.CENTER)
    addweightbutton.place(relx=0.2, rely=0.35, anchor=tk.CENTER)
    
    resetweightbutton.place(relx=0.4, rely=0.225, anchor=tk.CENTER)

    desiredcalorieslabel.place(relx=0.7, rely=0.1, anchor=tk.CENTER)
    desiredcaloriesentry.place(relx=0.7, rely=0.15, anchor=tk.CENTER)
    updatecaloriesbutton.place(relx=0.7, rely=0.2, anchor=tk.CENTER)

    caloriesinputlabel.place(relx=0.7, rely=0.25, anchor=tk.CENTER)
    caloriesinputentry.place(relx=0.7, rely=0.3, anchor=tk.CENTER)
    addcaloriesbutton.place(relx=0.7, rely=0.35, anchor=tk.CENTER)
    
    resetcaloriesbutton.place(relx=0.9, rely=0.225, anchor=tk.CENTER)

    target1.place(relx=0.25, rely=0.425, anchor=tk.CENTER)
    target2.place(relx=0.75, rely=0.425, anchor=tk.CENTER)
    target3.place(relx=0.2, rely=0.05, anchor=tk.CENTER)
    target4.place(relx=0.7, rely=0.05, anchor=tk.CENTER)
    
    return trackerframe

def createactiveframe(notebook, username, root):
    activeframe = ttk.Frame(notebook)
    
    grapher.graphthree([], [], activeframe, True)
    grapher.graphfour([], [], activeframe, True)
    grapher.graphfive([], [], activeframe, True)

    alertlabel1 = tk.Label(activeframe, fg="orange", text="NOTE: IF YOU DON'T KNOW YOUR CALORIC EXPENDITURE, PRESS GO TO CALCULATE IT", font=("Helvetica", 12, "bold"))
    alertlabel1.place(relx=0.5, rely=0.025, anchor=tk.CENTER)

    alertlabel2 = tk.Label(activeframe, text="", font=("Helvetica", 15, "bold"))
    alertlabel2.place(relx=0.75, rely=0.95, anchor=tk.CENTER)

    alertlabel3 = tk.Label(activeframe, font=("Helvetica", 10), text="**How Activity Factor Works**\n -If you wanna be more specific then estimate the value using below info\n-Sedentary (little or no exercise): 1.2\n-Lightly Active (light exercise/sports 1-3 days a week): 1.375\n-Moderately Active (mod. exercise/sports 3-5 days a week): 1.55\n-Very Active (hard exercise/sports 6-7 days a week): 1.725\n-Extremely Active (harder and physical job/x2 training): 1.9")
    alertlabel3.place(relx=0.725, rely=0.85, anchor=tk.CENTER)
    
    distancelabel = tk.Label(activeframe, text="Distance: 0", font=("Helvetica", 10, "bold"))
    distancelabel.place(relx=0.125, rely=0.125, anchor=tk.CENTER)
    stepstakenlabel = tk.Label(activeframe, text="Steps: 0", font=("Helvetica", 10, "bold"))
    stepstakenlabel.place(relx=0.3, rely=0.125, anchor=tk.CENTER)
    avgspeedlabel = tk.Label(activeframe, text="Average Speed: 0", font=("Helvetica", 10, "bold"))
    avgspeedlabel.place(relx=0.5, rely=0.125, anchor=tk.CENTER)
    atspeedlabel = tk.Label(activeframe, text="Current Speed: 0", font=("Helvetica", 10, "bold"))
    atspeedlabel.place(relx=0.7, rely=0.125, anchor=tk.CENTER)
    caloriesburnedlabel = tk.Label(activeframe, text="Calories Burned: 0", font=("Helvetica", 10, "bold"))
    caloriesburnedlabel.place(relx=0.875, rely=0.125, anchor=tk.CENTER)
    elapsedtimelabel = tk.Label(activeframe, text="Elapsed Time: 0", font=("Helvetica", 20, "bold"))
    elapsedtimelabel.place(relx=0.75, rely=0.58, anchor=tk.CENTER)

    missingweightinfolabel = tk.Label(activeframe, text="Weight:", font=("Helvetica", 8, "bold"))
    missingweightinfoentry = tk.Entry(activeframe, width=5)
    missingweightinfobutton = tk.Button(activeframe, fg="green", text="Enter", font=("Helvetica", 8, "bold"), command=lambda: missingweightget(missingweightinfoentry.get(), missingweightinfolabel, missingweightinfoentry, missingweightinfobutton, lambda weighttoday: activepaths(username, 1, ontopalertlabel, gobutton, endbutton, submitbutton, alertlabel2, missingweightinfolabel, missingweightinfoentry, missingweightinfobutton, atspeedlabel, avgspeedlabel, distancelabel, caloriesburnedlabel, stepstakenlabel, elapsedtimelabel, activeframe, root)))

    heightinfolabel = tk.Label(activeframe, text="Height (cm):", font=("Helvetica", 12, "bold"))
    heightinfoentry = tk.Entry(activeframe, width=10)
    ageinfolabel = tk.Label(activeframe, text="Age (yr):", font=("Helvetica", 12, "bold"))
    ageinfoentry = tk.Entry(activeframe, width=10)
    sexinfolabel = tk.Label(activeframe, text="Sex:", font=("Helvetica", 12, "bold"))
    sexinfoentry = tk.Entry(activeframe, width=10)
    activityfactorinfolabel = tk.Label(activeframe, text="Activity Factor:", font=("Helvetica", 12, "bold"))
    activityfactorinfoentry = tk.Entry(activeframe, width=10)
    submitbutton = tk.Button(activeframe, fg="green", text="Submit", font=("Helvetica", 12, "bold"), command=lambda: activesubmitbutton(username, heightinfoentry.get(), ageinfoentry.get(), sexinfoentry.get(), activityfactorinfoentry.get(), alertlabel2))
    heightinfolabel.place(relx=0.65, rely=0.62, anchor=tk.CENTER)
    heightinfoentry.place(relx=0.8, rely=0.62, anchor=tk.CENTER)
    ageinfolabel.place(relx=0.65, rely=0.65, anchor=tk.CENTER)
    ageinfoentry.place(relx=0.8, rely=0.65, anchor=tk.CENTER)
    sexinfolabel.place(relx=0.65, rely=0.68, anchor=tk.CENTER)
    sexinfoentry.place(relx=0.8, rely=0.68, anchor=tk.CENTER)
    activityfactorinfolabel.place(relx=0.65, rely=0.71, anchor=tk.CENTER)
    activityfactorinfoentry.place(relx=0.8, rely=0.71, anchor=tk.CENTER)
    submitbutton.place(relx=0.75, rely=0.75, anchor=tk.CENTER)

    gobutton = tk.Button(activeframe, text="GO", fg="green", font=("Helvetica", 15, "bold"), command=lambda: activepaths(username, 1, ontopalertlabel, gobutton, endbutton, submitbutton, alertlabel2, missingweightinfolabel, missingweightinfoentry, missingweightinfobutton, atspeedlabel, avgspeedlabel, distancelabel, caloriesburnedlabel, stepstakenlabel, elapsedtimelabel, activeframe, root))
    gobutton.place(relx=0.45, rely=0.065, anchor=tk.CENTER)
    endbutton = tk.Button(activeframe, text="END", fg="red", font=("Helvetica", 15, "bold"), command=lambda: activepaths(username, 2, ontopalertlabel, gobutton, endbutton, submitbutton, alertlabel2, missingweightinfolabel, missingweightinfoentry, missingweightinfobutton, atspeedlabel, avgspeedlabel, distancelabel, caloriesburnedlabel, stepstakenlabel, elapsedtimelabel, activeframe, root))
    endbutton.config(state=tk.DISABLED)
    endbutton.place(relx=0.55, rely=0.065, anchor=tk.CENTER)

    graph3 = tk.Label(activeframe, text="Distance over Time", font=("Helvetica", 10, "bold"))
    graph3.place(relx=0.25, rely=0.175, anchor=tk.CENTER)
    
    xaxis3 = tk.Label(activeframe, text="Time in Seconds", font=("Helvetica", 10, "bold"))
    xaxis3.place(relx=0.25, rely=0.54, anchor=tk.CENTER)

    yaxis3canvas = tk.Canvas(activeframe, width=30, height=200)
    yaxis3canvas.place(relx=0.025, rely=0.35, anchor=tk.CENTER)
    yaxis3 = yaxis3canvas.create_text(15, 100, text="Distance in Miles", anchor=tk.CENTER, font=("Helvetica", 10, "bold"))
    yaxis3canvas.itemconfigure(yaxis3, angle=90)

    graph4 = tk.Label(activeframe, text="Speed over Time", font=("Helvetica", 10, "bold"))
    graph4.place(relx=0.75, rely=0.175, anchor=tk.CENTER)

    xaxis4 = tk.Label(activeframe, text="Time in Seconds", font=("Helvetica", 10, "bold"))
    xaxis4.place(relx=0.75, rely=0.54, anchor=tk.CENTER)

    yaxis4canvas = tk.Canvas(activeframe, width=30, height=200)
    yaxis4canvas.place(relx=0.525, rely=0.35, anchor=tk.CENTER)
    yaxis4 = yaxis4canvas.create_text(15, 100, text="Speed in Miles Per Hour", anchor=tk.CENTER, font=("Helvetica", 10, "bold"))
    yaxis4canvas.itemconfigure(yaxis4, angle=90)

    graph5 = tk.Label(activeframe, text="Calories Burned over Time", font=("Helvetica", 10, "bold"))
    graph5.place(relx=0.25, rely=0.6, anchor=tk.CENTER)

    xaxis5 = tk.Label(activeframe, text="Time in Seconds", font=("Helvetica", 10, "bold"))
    xaxis5.place(relx=0.25, rely=0.965, anchor=tk.CENTER)

    yaxis5canvas = tk.Canvas(activeframe, width=30, height=200)
    yaxis5canvas.place(relx=0.025, rely=0.775, anchor=tk.CENTER)
    yaxis5 = yaxis5canvas.create_text(15, 100, text="Calories Burned in Kilocalories", anchor=tk.CENTER, font=("Helvetica", 10, "bold"))
    yaxis5canvas.itemconfigure(yaxis5, angle=90)
    
    ontopalertlabel = tk.Label(activeframe, fg="brown", text="", font=("Helvetica", 20, "bold"))
    
    return activeframe

def createscannerframe(notebook, root):
    scannerframe = ttk.Frame(notebook)
    
    scancanvas = tk.Canvas(scannerframe, width=640, height=480)
    scancanvas.pack()
    scancanvas.create_rectangle(0, 0, 640, 480, fill="black")

    generalentry = tk.Entry(scannerframe)
    generalentry.place(relx=0.35, rely=0.86, anchor=tk.CENTER)

    resultslabel = tk.Label(scannerframe, text="")
    resultslabel.place(relx=0.35, rely=0.935, anchor=tk.CENTER)

    noticelabel = tk.Label(scannerframe, fg="orange", text="Make sure your default camera is the camera you want to use", font=("Helvetica", 12, "bold"))
    noticelabel.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    campermbutton = tk.Button(scannerframe, text="Grant Camera Permission", command=lambda: camera.enablecamera(campermbutton, scanbutton, noticelabel, scancanvas, root))
    campermbutton.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    barsearchbutton = tk.Button(scannerframe, text="Search by Barcode (likely)", command=lambda: camera.searchbybarcode(generalentry.get(), resultslabel))
    barsearchbutton.place(relx=0.575, rely=0.86, anchor=tk.CENTER)

    namesearchbutton = tk.Button(scannerframe, text="Search by Name (unlikely)", command=lambda: camera.searchbyname(generalentry.get(), resultslabel))
    namesearchbutton.place(relx=0.575, rely=0.91, anchor=tk.CENTER)

    scanbutton = tk.Button(scannerframe, text="Scan Barcode (likely)", state=tk.DISABLED, command=lambda: camera.scanbarcode(resultslabel))
    scanbutton.place(relx=0.575, rely=0.96, anchor=tk.CENTER)
    
    connectedlabel = tk.Label(scannerframe, fg="red", text="", font=("Helvetica", 15, "bold"))

    internetconnectioncheck(barsearchbutton, namesearchbutton, scanbutton, connectedlabel, root)

    return scannerframe

def createchallengesframe(notebook, username):
    challengesframe = ttk.Frame(notebook)

    athleticchallengelines = {
    "Distance": ["1 mile", "2 miles", "5 miles", "10 miles"],
    "Speed": ["2 mph", "3 mph", "4.5 mph", "6 mph"],
    "Duration": ["5 minutes", "10 minutes", "30 minutes", "1 hour"]
    }

    calisthenicschallengelines = {
        "Pull ups": ["5 reps", "10 reps", "15 reps", "25 reps"],
        "Planks": ["30 seconds", "2 minutes", "5 minutes", "10 minutes"],
        "Push ups": ["10 reps", "20 reps", "30 reps", "50 reps"]
    }

    weightchallengelines = {
        "Squats": ["5 kg", "10 kg", "15 kg", "20 kg"],
        "Bench Press": ["8 kg", "16 kg", "20 kg", "25 kg"],
        "Curls": ["5 kg", "8 kg", "10 kg", "12 kg"]
    }

    athleticchallenges = ["Distance", "Speed", "Duration"]
    calisthenicschallenges = ["Pull ups", "Planks", "Push ups"]
    weightchallenges = ["Squats", "Bench Press", "Curls"]

    failedlabel = tk.Label(challengesframe, fg="red", text="", font=("Helvetica", 20, "bold"))
    challenge1label = tk.Label(challengesframe, text="Cardiovascular Challenge\nType: None\nLevel: None", font=("Helvetica", 15, "bold"))
    challenge2label = tk.Label(challengesframe, text="Calisthenics Challenge\nType: None\nLevel: None", font=("Helvetica", 15, "bold"))
    challenge3label = tk.Label(challengesframe, text="Weights Challenge\nType: None\nLevel: None", font=("Helvetica", 15, "bold"))

    shufflechallengesbutton = tk.Button(challengesframe, fg="blue", text="Shuffle Challenges", font=("Helvetica", 20, "bold"), command=lambda: shufflechallenges(challenge1button, challenge2button, challenge3button, username, athleticchallengelines, calisthenicschallengelines, weightchallengelines, challenge1label, challenge2label, challenge3label, athleticchallenges, calisthenicschallenges, weightchallenges, failedlabel))
    resetchallengesbutton = tk.Button(challengesframe, fg="red", text="Reset Challenges", font=("Helvetica", 20, "bold"), command=lambda: (challenges.resetcontents(username),shufflechallenges(challenge1button, challenge2button, challenge3button, username, athleticchallengelines, calisthenicschallengelines, weightchallengelines, challenge1label, challenge2label, challenge3label, athleticchallenges, calisthenicschallenges, weightchallenges, failedlabel)))
    challenge1button = tk.Button(challengesframe, state="disabled", fg="green", text="I did it!", font=("Helvetica", 15, "bold"), command=lambda: challenges.receivechallenge(username, athleticchallengelines, True, challenge1label, athleticchallenges, calisthenicschallenges, weightchallenges, failedlabel))
    challenge2button = tk.Button(challengesframe, state="disabled", fg="green", text="I did it!", font=("Helvetica", 15, "bold"), command=lambda: challenges.receivechallenge(username, calisthenicschallengelines, True, challenge2label, athleticchallenges, calisthenicschallenges, weightchallenges, failedlabel))
    challenge3button = tk.Button(challengesframe, state="disabled", fg="green", text="I did it!", font=("Helvetica", 15, "bold"), command=lambda: challenges.receivechallenge(username, weightchallengelines, True, challenge3label, athleticchallenges, calisthenicschallenges, weightchallenges, failedlabel))

    failedlabel.place(relx=0.5, rely=0.04, anchor=tk.CENTER)
    challenge1label.place(relx=0.5, rely=0.135, anchor=tk.CENTER)
    challenge1button.place(relx=0.5, rely=0.235, anchor=tk.CENTER)
    challenge2label.place(relx=0.5, rely=0.385, anchor=tk.CENTER)
    challenge2button.place(relx=0.5, rely=0.485, anchor=tk.CENTER)
    challenge3label.place(relx=0.5, rely=0.635, anchor=tk.CENTER)
    challenge3button.place(relx=0.5, rely=0.735, anchor=tk.CENTER)
    shufflechallengesbutton.place(relx=0.5, rely=0.825, anchor=tk.CENTER)
    resetchallengesbutton.place(relx=0.5, rely=0.925, anchor=tk.CENTER)

    return challengesframe

def createsettingsframe(notebook, root, startpage, style, username, password):
    settingsframe = ttk.Frame(notebook)

    warninglabel = tk.Label(settingsframe, fg="red", text="WARNING: YOU WILL BE SIGNED OUT", font=("Helvetica", 15, "bold"))

    warninglabel.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    failedattempt3 = tk.Label(settingsframe, text="", font=("Helvetica", 15, "bold"))

    failedattempt3.place(relx=0.5, rely=0.465, anchor=tk.CENTER)

    failedattempt4 = tk.Label(settingsframe, text="", font=("Helvetica", 15, "bold"))

    failedattempt4.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    changeusernameentry = tk.Entry(settingsframe, width=30)
    changeusernamebutton = tk.Button(settingsframe, text="Change Username", fg="blue", font=("Helvetica", 12, "bold"), command=lambda: settingspaths(username, password, failedattempt3, failedattempt4, changeusernameentry.get(), None, 1, notebook, style, startpage, settingsframe))

    changeusernameentry.place(relx=0.5, rely=0.125, anchor=tk.CENTER)
    changeusernamebutton.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    changepasswordentry = tk.Entry(settingsframe, width=30, show="*")
    changepasswordconfirmentry = tk.Entry(settingsframe, width=30, show="*")
    changepasswordbutton = tk.Button(settingsframe, text="Change Password", fg="blue", font=("Helvetica", 12, "bold"), command=lambda: settingspaths(username, password, failedattempt3, failedattempt4, changepasswordentry.get(), changepasswordconfirmentry.get(), 2, notebook, style, startpage, settingsframe))

    changepasswordentry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    changepasswordconfirmentry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    changepasswordbutton.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    signoutbutton = tk.Button(settingsframe, text="Sign Out", fg="red", font=("Helvetica", 20, "bold"), command=lambda: startpage(notebook, style, False))

    signoutbutton.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    deletefilesbutton = tk.Button(settingsframe, text="Delete Data", fg="red", font=("Helvetica", 20, "bold"), command=lambda: settingspaths(username, password, failedattempt3, failedattempt4, None, None, 3, notebook, style, startpage, settingsframe))

    deletefilesbutton.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    deleteaccountbutton = tk.Button(settingsframe, text="Delete Account", fg="red", font=("Helvetica", 20, "bold"), command=lambda: settingspaths(username, password, failedattempt3, failedattempt4, None, None, 4, notebook, style, startpage, settingsframe))

    deleteaccountbutton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    return settingsframe

def shufflechallenges(challenge1button, challenge2button, challenge3button, username, athleticchallengelines, calisthenicschallengelines, weightchallengelines, challenge1label, challenge2label, challenge3label, athleticchallenges, calisthenicschallenges, weightchallenges, failedlabel):
    challenges.receivechallenge(username, athleticchallengelines, False, challenge1label, athleticchallenges, calisthenicschallenges, weightchallenges, failedlabel)
    challenges.receivechallenge(username, calisthenicschallengelines, False, challenge2label, athleticchallenges, calisthenicschallenges, weightchallenges, failedlabel)
    challenges.receivechallenge(username, weightchallengelines, False, challenge3label, athleticchallenges, calisthenicschallenges, weightchallenges, failedlabel)
    challenge1button.config(state="normal")
    challenge2button.config(state="normal")
    challenge3button.config(state="normal")

def internetconnectioncheck(barsearchbutton, namesearchbutton, scanbutton, connectedlabel, root):
    global working, permissiongranted

    if working:
        if scanbutton.cget("state") == "normal":
            permissiongranted = True
            
        if camera.checkconnection():
            barsearchbutton.config(state="normal")
            namesearchbutton.config(state="normal")
            if permissiongranted:
                scanbutton.config(state="normal")
            connectedlabel.place_forget()
            connectedlabel.config(text="")
        else:
            barsearchbutton.config(state="disabled")
            namesearchbutton.config(state="disabled")
            if permissiongranted:
                scanbutton.config(state="disabled")
            connectedlabel.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
            connectedlabel.config(text="No internet connection")
        root.after(1000, internetconnectioncheck, barsearchbutton, namesearchbutton, scanbutton, connectedlabel, root)

def bmrcalculator(weight, height, age, sex, activityfactor):
    if sex.lower() == "male":
        bmr = 88.362 + (13.397*weight) + (4.799*height) - (5.677*age)

    elif sex.lower() == "female":
        bmr = 447.593 + (9.247*weight) + (3.098*height) - (4.330*age)

    bmr *= activityfactor

    return bmr

def missingweightget(inputtedvalue, missingweightinfolabel, missingweightinfoentry, missingweightinfobutton, callback):
    global weighttoday
    try:
        floatvalue = float(inputtedvalue)
        if abs(floatvalue) != float("inf") and isnan(abs(floatvalue)) == False:
            missingweightinfolabel.place_forget()
            missingweightinfoentry.place_forget()
            missingweightinfobutton.place_forget()
            weighttoday = floatvalue
            callback(weighttoday)
    except ValueError:
        pass

def activepaths(username, path, ontopalertlabel, gobutton, endbutton, submitbutton, alertlabel2, missingweightinfolabel, missingweightinfoentry, missingweightinfobutton, atspeedlabel, avgspeedlabel, distancelabel, caloriesburnedlabel, stepstakenlabel, elapsedtimelabel, frame, root):
    global exercising, currentweight, numberstepstaken
    if path == 1:
        readytostart1 = False
        readytostart2 = False
        keyerror = False

        try:
            cipherer = encdec.getcipherer(username)
            acquiredvaluesset1 = encdec.readvalues(username, cipherer, 10)
            acquiredvaluesset2 = encdec.readvalues(username, cipherer, 30)
            if len(acquiredvaluesset2) == 4:
                height = acquiredvaluesset2[0]
                age = acquiredvaluesset2[1]
                sex = acquiredvaluesset2[2]
                activityfactor = acquiredvaluesset2[3]
                readytostart1 = True
                if len(acquiredvaluesset1) > 1:
                    currentweight = acquiredvaluesset1[-1]
                    readytostart2 = True
                else:
                    if weighttoday == None:
                        missingweightinfolabel.place(relx=0.445, rely=0.105, anchor=tk.CENTER)
                        missingweightinfoentry.place(relx=0.5, rely=0.105, anchor=tk.CENTER)
                        missingweightinfobutton.place(relx=0.555, rely=0.105, anchor=tk.CENTER)
                        gobutton.config(state="disabled")
                        endbutton.config(state="disabled")
                        submitbutton.config(state="disabled")
                    if weighttoday != None:
                        currentweight = weighttoday
                        readytostart2 = True
        except (InvalidSignature, InvalidToken, ValueError, binascii.Error):
              alertlabel2.config(text="KEY INVALID, RESET DATA", fg="red")
              keyerror = True
            
        if readytostart1 and readytostart2:
            dataranges = {
                "time": [],
                "distance": [],
                "caloriesburned": [],
                "speed": []
            }
            numberstepstaken = 0
            gobutton.config(state="disabled")
            endbutton.config(state="normal")
            submitbutton.config(state="normal")
            bmr = bmrcalculator(currentweight, height, age, sex, activityfactor)
            alertlabel2.config(text=f"CALORIC EXPENDITURE IS {int(bmr)}", fg="blue")
            root.update_idletasks()
            exercising = True
            starttime = time.time()
            def stepdetection():
                global numberstepstaken
                if exercising:
                    numberstepstaken += random.randint(0,4)
                    root.after(1000, stepdetection)
            def activitytracker():
                if exercising:
                    steps = numberstepstaken
                    distance = ((steps*((76.2/170)*height))/160900)
                    elapsedtime = time.time() - starttime
                    caloriesburned, speed, avgspeed = active.caloriesspeedcalc(dataranges, currentweight, distance, elapsedtime, bmr)
                    newdata = active.updatedata(dataranges, elapsedtime, distance, speed, caloriesburned)
                    active.updatevisual(frame, newdata, atspeedlabel, avgspeedlabel, distancelabel, caloriesburnedlabel, stepstakenlabel, elapsedtimelabel, elapsedtime, distance, steps, caloriesburned, speed, avgspeed)
                    root.after(1000, activitytracker)
            stepdetection()
            activitytracker()
        else:
            if not keyerror:
                alertlabel2.config(text="FILL OUT REQUIRED INFO", fg="red")
            
    elif path == 2:
        exercising = False
        def enablebuttons():
            endbutton.config(state="disabled")
            gobutton.config(state="normal")
        root.after(1500, enablebuttons)

def activesubmitbutton(username, height, age, sex, activityfactor, alertlabel):
    try:
        height = float(height)
        age = float(age)
        activityfactor = float(activityfactor)
        if abs(height) != float("inf") and abs(age) != float("inf") and abs(activityfactor) != float("inf") and isnan(abs(height)) == False and isnan(abs(age)) == False and isnan(abs(activityfactor)) == False:
            if str(sex).lower() == "male" or sex == "female":
                cipherer = encdec.getcipherer(username)
                try:
                    encdec.readvalues(username, cipherer, 3)
                    encdec.resetvalue(username, cipherer, 3)
                    encdec.updatedesiredvalue(username, height, cipherer, 3)
                    encdec.addnewvalue(username, age, cipherer, 3)
                    encdec.addnewvalue(username, sex, cipherer, 3)
                    encdec.addnewvalue(username, activityfactor, cipherer, 3)
                    alertlabel.config(text="FILE SAVED", fg="green")
                except (InvalidSignature, InvalidToken, ValueError, binascii.Error):
                      alertlabel.config(text="KEY INVALID, RESET DATA", fg="red")
            else:
                alertlabel.config(text="INVALID INFO, ENTER MALE OR FEMALE", fg="red")
        else:
            alertlabel.config(text="INVALID INFO, NO INF OR NAN VALUES", fg="red")
    except ValueError:
        alertlabel.config(text="INVALID INFO, ENTER NUMBERS", fg="red")

def settingspaths(username, password, failedattempt3, failedattempt4, newvalue, confirmvalue, choice, notebook, style, startpage, frame):
    datafile1 = f"{username}1.txt"
    datafile2 = f"{username}2.txt"
    datafile3 = f"{username}3.txt"
    datafile4 = f"{username}4.txt"
    datafile5 = f"{username}.key"
    
    def renamer():
        newdatafile1 = f"{newvalue}1.txt"
        newdatafile2 = f"{newvalue}2.txt"
        newdatafile3 = f"{newvalue}3.txt"
        newdatafile4 = f"{newvalue}4.txt"
        newdatafile5 = f"{newvalue}.key"
        def renamefiles(old, new):
            try:
                os.rename(old, new)
            except (FileNotFoundError, FileExistsError) as e:
                if isinstance(e, FileExistsError):
                    os.remove(new)
                    renamefiles(old, new)
        renamefiles(datafile1, newdatafile1)
        renamefiles(datafile2, newdatafile2)
        renamefiles(datafile3, newdatafile3)
        renamefiles(datafile4, newdatafile4)
        renamefiles(datafile5, newdatafile5)
    
    if choice == 1:
        if reglog.changeusername(failedattempt3, username, newvalue):
            renamer()
            timebasesignout(notebook, style, frame, startpage)
    elif choice == 2:
        if reglog.changepassword(failedattempt3, username, password, newvalue, confirmvalue):
            timebasesignout(notebook, style, frame, startpage)
    elif choice == 3 or choice == 4:
        reglog.deleter(datafile1, datafile2, datafile3, datafile4, datafile5)
        if choice == 3:
            failedattempt4.config(text="Files deleted!", fg="red")
            timebasesignout(notebook, style, frame, startpage)
        elif choice == 4:
            reglog.deleteaccount(failedattempt4, username, True)
            timebasesignout(notebook, style, frame, startpage)

def timebasesignout(notebook, style, frame, startpage):
    frame.update_idletasks()
    time.sleep(1)
    startpage(notebook, style, False)

def passtographhandle(username, target1, target2, target3, target4, inputtedvalue, option, frame, graphnumber):
    try:
        floatvalue = float(inputtedvalue)
        if abs(floatvalue) != float("inf") and isnan(abs(floatvalue)) == False:
            grapher.graphdatahandler(username, target1, target2, target3, target4, floatvalue, option, frame, False, graphnumber)
    except ValueError:
        pass

def getregisterinputs(failedattempt, username, password, confirmpassword):
    reglog.registeruser(failedattempt, username, password, confirmpassword)

def getlogininputs(root, switcher2, failedattempt2, username, password):
    global fails
    maxattempts = 5
    failedkick(root,fails,maxattempts)
    if reglog.logincheck(username, password):
        fails = 0
        switcher2(None, username, password, True)
    elif fails < 5:
        fails += 1
        failedattempt2.config(text=f"failed attempts: {fails}/{maxattempts}")
        failedkick(root,fails,maxattempts)

def failedkick(root, fails, maxattempts):
    if fails >= maxattempts:
        closecontrol(root)

def indexfinder(keyword, notebook):
    index = None
    for i in range(notebook.index("end")):
        if notebook.tab(i, "text") == keyword:
            index = i
            break
    return index

def closecontrol(root):
    global exercising, working
    exercising = False
    working = False
    if os.path.exists("instance.lock"):
        os.remove("instance.lock")
    root.destroy()
    sys.exit()

def menumain():
    global fails
    fails = 0
    root = tk.Tk()
    style = ttk.Style()
    notebook = ttk.Notebook(root)

    def defaulttab():
        layout = [
            ('Notebook.tab', {
                'sticky': 'nswe', 'children': [
                    ('Notebook.padding', {
                        'side': 'top', 'sticky': 'nswe',
                        'children': [
                            ('Notebook.focus', {
                                'side': 'top', 'sticky': 'nswe',
                                'children': [
                                    ('Notebook.label', {'side': 'left', 'sticky': ''}),
                                    ('Notebook.close', {'side': 'left', 'sticky': ''}),
                                ]
                            }),
                        ]
                    }),
                ]
            })
        ]
        return layout

    def startpage(notebook, style, checkpointstart):
        global exercising, weighttoday, permissiongranted, working
        exercising = False
        working = False
        permissiongranted = False
        weighttoday = None
        registerframe = createregisterframe(notebook, switchtologin)
        loginframe = createloginframe(notebook, switchtoregister, switchtograph, root)
        notebook.add(registerframe, text="Register")
        notebook.add(loginframe, text="Login")
        if checkpointstart != True:
            camera.disablecamera()
            notebook.forget(indexfinder("Tracker", notebook))
            notebook.forget(indexfinder("Active", notebook))
            notebook.forget(indexfinder("Scanner", notebook))
            notebook.forget(indexfinder("Challenges", notebook))
            notebook.forget(indexfinder("Settings", notebook))
        style.layout("TNotebook.Tab", [])
        notebook.select(indexfinder("Register", notebook))

    def switchtoregister(event):
        notebook.select(indexfinder("Register", notebook))

    def switchtologin(event):
        notebook.select(indexfinder("Login", notebook))

    def framesizer():
        currenttab = notebook.tab(notebook.select(), "text")
        if currenttab == "Active":
            root.geometry("800x800")
        elif currenttab == "Tracker" or currenttab == "Scanner" or currenttab == "Challenges" or currenttab == "Settings":
            root.geometry("800x600")
        elif currenttab == "Register" or currenttab == "Login":
            root.geometry("500x300")
        else:
            closecontrol(root)

    def switchtograph(event, username, password, checkpointloggedin):
        global working
        working = True
        if checkpointloggedin:
            trackerframe = createtrackerframe(notebook, username)
            activeframe = createactiveframe(notebook, username, root)
            scannerframe = createscannerframe(notebook, root)
            challengesframe = createchallengesframe(notebook, username)
            settingsframe = createsettingsframe(notebook, root, startpage, style, username, password)
            notebook.add(trackerframe, text="Tracker")
            notebook.add(activeframe, text="Active")
            notebook.add(scannerframe, text="Scanner")
            notebook.add(challengesframe, text="Challenges")
            notebook.add(settingsframe, text="Settings")
            notebook.forget(indexfinder("Login", notebook))
            notebook.forget(indexfinder("Register", notebook))
            style.layout("TNotebook.Tab", defaulttab())
        notebook.select(indexfinder("Tracker", notebook))

    root.title("Fitness Aid Program")
    root.resizable(False, False)
    startpage(notebook, style, True)
    notebook.pack(expand=True, fill="both")
    notebook.bind("<<NotebookTabChanged>>", lambda event: framesizer())
    root.protocol("WM_DELETE_WINDOW", lambda: closecontrol(root))
    root.mainloop()
