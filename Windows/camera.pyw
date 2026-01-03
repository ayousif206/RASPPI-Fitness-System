from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
from tkinter import NW
import requests
import cv2
import json

def checkconnection():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except (requests.ConnectionError, requests.exceptions.ReadTimeout) as e:
        if isinstance(e, requests.ConnectionError):
            return False

def disablecamera():
    global vid
    try:
        if vid != None:
            vid.release()
            vid = None
    except NameError:
        vid = None

def enablecamera(campermbutton, scanbutton, noticelabel, canvas, root):
    global vid, frame
    vid = None
    success = False
    if checkconnection():
        try:
            vid = cv2.VideoCapture(0)
            success = True
            if not vid.isOpened():
                success = False
        except IndexError:
            pass
        if success:
            campermbutton.place_forget()
            noticelabel.place_forget()
            scanbutton.config(state="normal")
            updater(canvas, root)

def updater(canvas, root):
    global vid, frame
    if vid != None:
        ret, frame = vid.read()
        if ret:
            photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            canvas.create_image(0, 0, image=photo, anchor=NW)
            canvas.photo = photo
        root.after(750, updater, canvas, root)

def makeapirequest(resultslabel, endpoint, params=None):
    oauthtoken = "93743A7491C7C344534B44016501562A"
    baseurl = "https://api.upcdatabase.org"
    url = f"{baseurl}/{endpoint}"
    headers = {"Authorization": f"Bearer {oauthtoken}"}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, json.JSONDecodeError) as e:
        if isinstance(e, requests.exceptions.HTTPError):
            resultslabel.config(text=f"HTTP Error: {e}")
        elif isinstance(e, requests.exceptions.RequestException):
            resultslabel.config(text=f"Request Error: {e}")
        elif isinstance(e, json.JSONDecodeError):
            resultslabel.config(text=f"JSON Decode Error: {e}")

def decodebarcode(frame):
    barcodes = decode(frame)
    if barcodes:
        barcodedata = barcodes[0].data.decode("utf-8")
        return barcodedata
    else:
        return None

def barcodeapisearch(resultslabel, barcode):
    barcode = barcode.zfill(13)
    return makeapirequest(resultslabel, f"product/{barcode}")

def nameapisearch(resultslabel, foodname):
    return makeapirequest(resultslabel, f"search/", params={"query": foodname, "page": 1})

def energydisplay(displaytext, energykcalvalue, energykcal100g, energykcalserving):
    if energykcalvalue + energykcal100g + energykcalserving != 0:
        if energykcal100g != energykcalvalue:
            displaytext += f"Energy (kcal) value: {energykcalvalue}\n"
        if energykcal100g != energykcalserving:
            displaytext += f"Energy (kcal) per 100g: {energykcal100g}\n"
        if energykcalserving != 0:
            displaytext += f"Energy (kcal) per serving: {energykcalserving}"
    else:
        displaytext += f"Data not found"
    return displaytext

def searchbyname(foodname, resultslabel):
    if foodname:
        nameresult = nameapisearch(resultslabel, foodname)
        if nameresult:
            try:
                firstitem = nameresult["items"][0]
            except KeyError:
                firstitem = None
            energykcalvalue, energykcal100g, energykcalserving = getcalories(firstitem)
            displaytext = f"Food Name: {foodname}\n"
            displaytext = energydisplay(displaytext, energykcalvalue, energykcal100g, energykcalserving)
            resultslabel.config(text=displaytext)
        else:
            resultslabel.config(text="Data not found")

def searchbybarcode(barcode, resultslabel):
    if barcode:
        barcoderesult = barcodeapisearch(resultslabel, barcode)
        if barcoderesult:
            energykcalvalue, energykcal100g, energykcalserving = getcalories(barcoderesult)
            displaytext = f"Barcode: {barcode}\n"
            displaytext = energydisplay(displaytext, energykcalvalue, energykcal100g, energykcalserving)
            resultslabel.config(text=displaytext)
        else:
            resultslabel.config(text="Data not found")

def scanbarcode(resultslabel):
    if vid:
        barcodedata = decodebarcode(frame)
        if barcodedata: 
            barcoderesult = barcodeapisearch(resultslabel, barcodedata)
            energykcalvalue, energykcal100g, energykcalserving = getcalories(barcoderesult)
            displaytext = f"Barcode: {barcodedata}\n"
            displaytext = energydisplay(displaytext, energykcalvalue, energykcal100g, energykcalserving)
            resultslabel.config(text=displaytext)
        else:
            resultslabel.config(text="Data not found")
    else:
        resultslabel.config(text="Camera error")

def validateenergy(currentenergy):
    try:
        return float(currentenergy)
    except ValueError:
        return 0

def getcalories(data):
    if data and "metanutrition" in data:
        metanutrition = data["metanutrition"]
        if metanutrition:
            energykcalvalue = validateenergy(metanutrition.get("energy-kcal_value", 0))
            energykcalserving = validateenergy(metanutrition.get("energy-kcal_serving", 0))
            energykcal100g = validateenergy(metanutrition.get("energy-kcal_100g", 0))
            return energykcalvalue, energykcal100g, energykcalserving
    return 0, 0, 0

