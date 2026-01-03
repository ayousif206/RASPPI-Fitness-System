import random
import os

def savecontents(username, values):
    challengedata = f"{username}4.txt"
    with open(challengedata, "w") as datafile:
        datafile.write(",".join(map(str, values)))

def readcontents(username):
    challengedata = f"{username}4.txt"
    if not os.path.exists(challengedata):
        savecontents(username, ["0","0","0","0","0","0","0","0","0"])
    with open(challengedata, "r") as datafile:
      contents = datafile.read().strip().split(",")
    return contents

def resetcontents(username):
    savecontents(username, ["0","0","0","0","0","0","0","0","0"])

def receivechallenge(username, challengelines, complete, challengelabel, athleticchallenges, calisthenicschallenges, weightchallenges, failedlabel):
    global levelindex1, levelindex2, levelindex3, readindex1, readindex2, readindex3
    try:
        isathletics = False
        iscalisthenics = False
        isweights = False

        contents = readcontents(username)
        getkeys = list(challengelines.keys())
        challengetype = random.choice(getkeys)
        currentindex = getkeys.index(challengetype)

        if challengetype in athleticchallenges:
            if complete:
                if levelindex1 != 4:
                    levelindex1 += 1
                contents[readindex1] = levelindex1
            readindex1 = currentindex
            levelindex1 = int(contents[readindex1])
            levelindex = levelindex1
            isathletics = True
            
        elif challengetype in calisthenicschallenges:
            if complete:
                if levelindex2 != 4:
                    levelindex2 += 1
                contents[readindex2] = levelindex2
            readindex2 = currentindex
            readindex2 += 3
            levelindex2 = int(contents[readindex2])
            levelindex = levelindex2
            iscalisthenics = True
            
        elif challengetype in weightchallenges:
            if complete:
                if levelindex3 != 4:
                    levelindex3 += 1
                contents[readindex3] = levelindex3
            readindex3 = currentindex
            readindex3 += 6
            levelindex3 = int(contents[readindex3])
            levelindex = levelindex3
            isweights = True

        savecontents(username, contents)
        
        if levelindex != 4:
            progressionline = challengelines[challengetype]
            level = progressionline[levelindex]
            if isathletics:
                challengelabel.config(text=f"Cardiovascular Challenge\nType: {challengetype}\nLevel: {level}")
            elif iscalisthenics:
                challengelabel.config(text=f"Calisthenics Challenge\nType: {challengetype}\nLevel: {level}")
            elif isweights:
                challengelabel.config(text=f"Weights Challenge\nType: {challengetype}\nLevel: {level}")
        else:
            if isathletics:
                challengelabel.config(text=f"Cardiovascular Challenge\nType: {challengetype}\nLevel: Wow, complete!")
            elif iscalisthenics:
                challengelabel.config(text=f"Calisthenics Challenge\nType: {challengetype}\nLevel: Wow, complete!")
            elif isweights:
                challengelabel.config(text=f"Weights Challenge\nType: {challengetype}\nLevel: Wow, complete!")

        failedlabel.config(text="") 

    except (IndexError, TypeError, ValueError):
        failedlabel.config(text="READ FAILED, RESET DATA")

