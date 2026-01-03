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
            notefile.write("pls save me")
try:
    import sys
    import os
    allcodefiles = ["active.pyw", "camera.pyw", "challenges.pyw", "encdec.pyw", "grapher.pyw", "reglog.pyw"]
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
