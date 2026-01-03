import bcrypt
import os

def deleter(datafile1, datafile2, datafile3, datafile4, datafile5):
    def removefiles(datafile):
        try:
            os.remove(datafile)
        except FileNotFoundError:
            pass
    removefiles(datafile1)
    removefiles(datafile2)
    removefiles(datafile3)
    removefiles(datafile4)
    removefiles(datafile5)

def loaddata():
  usersdata = {}
  try:
    with open("storage.txt", "r+") as file:
      lines = file.readlines()
      file.seek(0)
      file.truncate()
      for line in lines:
        try:
            username, storedsalt, storedhash = line.strip().split(",")
            usersdata[username] = {"salt": storedsalt, "password": storedhash}
            file.write(line)
        except ValueError:
            continue
  except FileNotFoundError:
    pass
  return usersdata

def hashpass(password):
    salt = bcrypt.gensalt()
    hashedpass = bcrypt.hashpw(password.encode("utf-8"), salt)
    return salt, hashedpass

def registeruser(failedattempt, username, password, confirmpassword):
  usersdata = loaddata()
  passpass = passwordrequirementscheck(None, password, confirmpassword, failedattempt)
  userpass = usernamerequirementscheck(username, usersdata, failedattempt)
  if userpass and passpass:
    salt, hashedpass = hashpass(password)
    salt = str(salt)[2:-1]
    with open("storage.txt", "a") as file:
      file.write(f"{username},{salt},{hashedpass}\n")
    failedattempt.config(text="Registration successful", fg="green")

def usernamerequirementscheck(username, usersdata, failedattempt):
    passed = False
    while passed == False:
      if str(username):
        passed = True
      else:
        failedattempt.config(text="Enter a username", fg="red")
        passed = False
        break
      if (username.lower() not in (asavedusername.lower() for asavedusername in usersdata)):
        passed = True
      else:
        failedattempt.config(text="This username is already taken", fg="red")
        passed = False
        break
      if username.isalnum():
        passed = True
      else:
        failedattempt.config(text="This username has special characters", fg="red")
        passed = False
        break
      if len(username) >= 3:
        passed = True
      else:
        failedattempt.config(text="This username is not 3+ characters long", fg="red")
        passed = False
        break
      if len(username) <= 20:
        passed = True
      else:
        failedattempt.config(text="This username is more than 20 characters long", fg="red")
        passed = False
        break
    return passed

def passwordrequirementscheck(oldpassword, password, confirmpassword, failedattempt):
  passed = False
  while passed == False:
    if str(password):
      passed = True
    else:
      failedattempt.config(text="Enter a password", fg="red")
      passed = False
      break
    if password != oldpassword:
      passed = True
    else:
      failedattempt.config(text="New password cannot be the same as old password", fg="red")
      passed = False
      break
    if any(char.isalpha() for char in password):
      passed = True
    else:
      failedattempt.config(text="This password does not contain any letters", fg="red")
      passed = False
      break
    if any(char.islower() for char in password):
      passed = True
    else:
      failedattempt.config(text="This password does not contain any lowercase", fg="red")
      passed = False
      break
    if any(char.isupper() for char in password):
      passed = True
    else:
      failedattempt.config(text="This password does not contain any uppercase", fg="red")
      passed = False
      break
    if any(char.isdigit() for char in password):
      passed = True
    else:
      failedattempt.config(text="This password does not contain any numbers", fg="red")
      passed = False
      break
    if any(not char.isalnum() for char in password):
      passed = True
    else:
      failedattempt.config(text="This password does not contain a special character", fg="red")
      passed = False
      break
    if len(password) >= 7:
      passed = True
    else:
      failedattempt.config(text="This password is not 7 characters or above long", fg="red")
      passed = False
      break
    if confirmpassword == password:
      passed = True
    else:
      failedattempt.config(text="Password confirmation does not match", fg="red")
      passed = False
      break
  return passed

def logincheck(username, password):
  usersdata = loaddata()
  if username in usersdata:
    try:
      storedsalt = usersdata[username]["salt"].encode("utf-8")
      storedhash = usersdata[username]["password"]
      hashedinputpassword = bcrypt.hashpw(password.encode("utf-8"), storedsalt)
      return str(hashedinputpassword) == str(storedhash)
    except BaseException as e:
      if str(type(e)) == "<class 'pyo3_runtime.PanicException'>" or isinstance(e, ValueError):
        datafile1 = f"{username}1.txt"
        datafile2 = f"{username}2.txt"
        datafile3 = f"{username}3.txt"
        datafile4 = f"{username}4.txt"
        datafile5 = f"{username}.key"
        deleter(datafile1, datafile2, datafile3, datafile4, datafile5)
        deleteaccount(None, username, False)
      else:
        raise e
      return False
  else:
    return False

def changeusername(failedattempt, oldusername, newusername):
  usersdata = loaddata()
  userpass = usernamerequirementscheck(newusername, usersdata, failedattempt)
  if userpass:
    usersdata[newusername] = usersdata.pop(oldusername)
    saveafterupdate(usersdata)
    failedattempt.config(text="Username changed successfully and files updated as well", fg="green")
    return True
  else:
    return False

def changepassword(failedattempt, username, password, newpassword, confirmnewpassword):
  usersdata = loaddata()
  passpass = passwordrequirementscheck(password, newpassword, confirmnewpassword, failedattempt)
  if passpass:
    usersdata[username]["salt"], usersdata[username]["password"] = hashpass(newpassword)
    saveafterupdate(usersdata)
    failedattempt.config(text="Password changed successfully and files updated as well", fg="green")
    return True
  else:
    return False

def deleteaccount(failedattempt, username, settingspath):
  usersdata = loaddata()
  if username in usersdata:
    del usersdata[username]
    saveafterupdate(usersdata)
    if settingspath:
      failedattempt.config(text="Account deleted!", fg="red")

def saveafterupdate(usersdata):
  with open("storage.txt", "w") as file:
      for username, userdata in usersdata.items():
          salt = userdata["salt"]
          hashedpass = userdata["password"]
          file.write(f"{username},{salt},{hashedpass}\n")
