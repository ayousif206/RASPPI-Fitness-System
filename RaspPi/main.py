def notfounderror():
    from datetime import datetime
    currenttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("errorlog.txt", "a") as logfile:
        logfile.write(f"{currenttime} ERR - A FILE MAY BE CORRUPTED OR MISSING\n")
    if os.path.exists("instance.lock"):
        os.remove("instance.lock")

def startup(lockstart):
    if lockstart:
        if os.path.exists("instance.lock"):
            sys.exit()
        with open("instance.lock", "w"):
            pass
    if not os.path.exists("readme.txt"):
        with open("readme.txt", "w") as notefile:
            notefile.write("**RASPBERRY PI EDITION CODE NOTE\n-IF NOT RUNNING DELETE INSTANCE.LOCK\n-OPEN TERMINAL AND RUN source venv/bin/activate (only for creator’s use due to errors unless you have used a virtual environment for your modules as well)\n-I AM USING .PY BECAUSE .PYW HAS ISSUES ON THE OS\n-USE GEANY PREFERABLY AND IGNORE (.sh) TERMINAL THAT OPENS ALONG INSTEAD\n-RASP PI TKINTER IS ODD SO YOU CAN RESIZE THE WINDOW FREELY (EVEN THOUGH I LOCKED IT) FOR TEXT VISIBILITY BUT THERE MAY BE ALIGNMENT ISSUES OUT OF MY CONTROL SO PLEASE TAKE CARE**")
try:
    import sys
    import os
    allcodefiles = ["active.py", "camera.py", "challenges.py", "encdec.py", "grapher.py", "reglog.py"]
    for codefile in allcodefiles:
        if not os.path.exists(codefile):
            notfounderror()
            sys.exit()
    startup(True)
    import menu
    menu.menumain()
except (ModuleNotFoundError, AttributeError):
    startup(False)
    notfounderror()
