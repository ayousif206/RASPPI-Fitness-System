from cryptography.fernet import Fernet

def loadkey(username):
  keyfile = f"{username}.key"
  try:
    with open(keyfile, "rb") as file:
      return file.read()
  except FileNotFoundError:
    key = Fernet.generate_key()
    with open(keyfile, "wb") as keyfile:
      keyfile.write(key)
    return key

def getcipherer(username):
  key = loadkey(username)
  return Fernet(key)

def encrypt(data, cipherer):
  return cipherer.encrypt(data.encode())

def decrypt(data, cipherer):
  return cipherer.decrypt(data).decode()

def savevalue(username, values, cipherer, graphnumber):
  if graphnumber == 1:
    userfile = f"{username}1.txt"
  elif graphnumber == 2:
    userfile = f"{username}2.txt"
  elif graphnumber == 3:
    userfile = f"{username}3.txt"
  data = ",".join(map(str, values))
  encrypteddata = encrypt(data, cipherer)
  with open(userfile, "wb") as file:
    file.write(encrypteddata)

def readvalues(username, cipherer, graphnumber):
  if graphnumber == 1 or graphnumber == 10:
    userfile = f"{username}1.txt"
  elif graphnumber == 2:
    userfile = f"{username}2.txt"
  elif graphnumber == 3 or graphnumber == 30:
    userfile = f"{username}3.txt"
  values = []
  try:
    with open(userfile, "rb") as file:
      encrypteddata = file.read()
      decrypteddata = decrypt(encrypteddata, cipherer)
      valuesplit = decrypteddata.strip().split(",")
      for value in valuesplit:
        try:
          floatvalue = float(value)
          values.append(floatvalue)
        except ValueError:
          values.append(value)
  except FileNotFoundError:
    if graphnumber != 10 and graphnumber != 30:
      values = [0.0]
      savevalue(username, values, cipherer, graphnumber)
  return values

def updatedesiredvalue(username, newdesiredvalue, cipherer, graphnumber):
  values = readvalues(username, cipherer, graphnumber)
  values[0] = newdesiredvalue
  savevalue(username, values, cipherer, graphnumber)

def addnewvalue(username, newvalue, cipherer, graphnumber):
  values = readvalues(username, cipherer, graphnumber)
  values.append(newvalue)
  savevalue(username, values, cipherer, graphnumber)

def resetvalue(username, cipherer, graphnumber):
  if graphnumber == 1:
    userfile = f"{username}1.txt"
  elif graphnumber == 2:
    userfile = f"{username}2.txt"
  elif graphnumber == 3:
    userfile = f"{username}3.txt"
  values = [0.0]
  savevalue(username, values, cipherer, graphnumber)
