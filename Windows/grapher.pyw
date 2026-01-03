from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import encdec
from cryptography.exceptions import InvalidSignature
from cryptography.fernet import InvalidToken
from os.path import exists
from datetime import datetime
import binascii

def graphone(x, y, z, frame, creation):
  global fig1, ax1, canvas1
  if creation:
    fig1, ax1 = plt.subplots(figsize=(3.2,3))
    canvas1 = FigureCanvasTkAgg(fig1, master=frame)
    canvaswidget1 = canvas1.get_tk_widget()
    canvaswidget1.place(relx=0.05, rely=0.45)
    
  ax1.clear()
  ax1.grid()
  ax1.plot(x, y, "o", linestyle="solid", color="lime")
  ax1.axhline(y=z, linestyle="dotted", color="blue")
  canvas1.draw()

def graphtwo(x, y, frame, creation):
  global fig2, ax2, canvas2
  if creation:
    fig2, ax2 = plt.subplots(figsize=(3.2,3))
    canvas2 = FigureCanvasTkAgg(fig2, master=frame)
    canvaswidget2 = canvas2.get_tk_widget()
    canvaswidget2.place(relx=0.55, rely=0.45)
    
  ax2.clear()
  ax2.grid()
  ax2.plot(x, y, "o", linestyle="solid", color="lime")
  canvas2.draw()

def graphthree(x, y, frame, creation):
  global fig3, ax3, canvas3
  if creation:
    fig3, ax3 = plt.subplots(figsize=(3.2,3))
    canvas3 = FigureCanvasTkAgg(fig3, master=frame)
    canvaswidget3 = canvas3.get_tk_widget()
    canvaswidget3.place(relx=0.05, rely=0.15)
    
  ax3.clear()
  ax3.grid()
  ax3.plot(x, y, linestyle="solid", color="lime")
  canvas3.draw()

def graphfour(x, y, frame, creation):
  global fig4, ax4, canvas4
  if creation:
    fig4, ax4 = plt.subplots(figsize=(3.2,3))
    canvas4 = FigureCanvasTkAgg(fig4, master=frame)
    canvaswidget4 = canvas4.get_tk_widget()
    canvaswidget4.place(relx=0.55, rely=0.15)
    
  ax4.clear()
  ax4.grid()
  ax4.plot(x, y, linestyle="solid", color="lime")
  canvas4.draw()

def graphfive(x, y, frame, creation):
  global fig5, ax5, canvas5
  if creation:
    fig5, ax5 = plt.subplots(figsize=(3.2,3))
    canvas5 = FigureCanvasTkAgg(fig5, master=frame)
    canvaswidget5 = canvas5.get_tk_widget()
    canvaswidget5.place(relx=0.05, rely=0.575)
    
  ax5.clear()
  ax5.grid()
  ax5.plot(x, y, linestyle="solid", color="lime")
  canvas5.draw()

def graphonehandling(x, y, z, frame, creation, doexist, target1, username, cipherer, graphnumber):
  if doexist:
    for i in range(len(y)):
      x.append(i+1)

    if z != 0 and str(y)[1:-1]:
      percentage = round(100-abs((z-y[-1])/z*100),2)
      target1.config(text=f"Target Percentage: {percentage}%")
      
    else:
      target1.config(text="Update your desired weight or add current weight")

  graphone(x, y, z, frame, creation)

def graphtwohandling(x, y, z, frame, creation, doexist, target2, username, cipherer, graphnumber):
  if doexist:
    uncompressedlist = y
    compressedlist = []
    i = 0
    
    while i < len(uncompressedlist):
      currentvalue = uncompressedlist[i+1]
      sublist = [uncompressedlist[i], currentvalue]
      i += 2
      
      while i < len(uncompressedlist) and uncompressedlist[i+1] == currentvalue:
        sublist[0] += uncompressedlist[i]
        i += 2
        
      compressedlist.extend(sublist)
    
    encdec.resetvalue(username, cipherer, graphnumber)
    encdec.updatedesiredvalue(username, z, cipherer, graphnumber)
    
    if str(compressedlist)[1:-1]:
      encdec.addnewvalue(username, str(compressedlist)[1:-1], cipherer, graphnumber)

    x = encdec.readvalues(username, cipherer, graphnumber)[2::2]
    y = encdec.readvalues(username, cipherer, graphnumber)[1::2]

    if z != 0 and str(y)[1:-1]:
      percentage = round(100-abs((z-sum(y))/z*100),2)
      
      if sum(y) > z:
        caloricstatus = "Caloric Surplus"
        
      elif sum(y) < z:
        caloricstatus = "Caloric Deficit"
        
      else:
        caloricstatus = "Caloric Expenditure"
        
      target2.config(text=f"Total Calories: {sum(y)}/{z} | Status: {caloricstatus} | Percentage: {percentage}%")

    else:
      target2.config(text="Update your desired calories or add current calories")

  graphtwo(x, y, frame, creation)

def graphdatahandler(username, target1, target2, target3, target4, givenvalue, option, frame, creation, graphnumber):
  def variables():
    x = []
    y = []
    z = 0
    doexist = False
    cipherer = None
    
    try: 
      if exists(f"{username}{graphnumber}.txt") or not creation:
        cipherer = encdec.getcipherer(username)
        y = encdec.readvalues(username, cipherer, graphnumber)[1:]
        z = encdec.readvalues(username, cipherer, graphnumber)[0]
        doexist = True
        if graphnumber == 1:
          target3.config(text="")
        elif graphnumber == 2:
          target4.config(text="")
    except (InvalidSignature, InvalidToken, ValueError, binascii.Error):
      if graphnumber == 1:
        target3.config(text="KEY INVALID, RESET DATA")
      elif graphnumber == 2:
        target4.config(text="KEY INVALID, RESET DATA")

    return x, y, z, doexist, cipherer

  x, y, z, doexist, cipherer = variables()

  if creation:
    if graphnumber == 1:
      graphonehandling(x, y, z, frame, creation, doexist, target1, username, cipherer, graphnumber)

    elif graphnumber == 2:
      graphtwohandling(x, y, z, frame, creation, doexist, target2, username, cipherer, graphnumber)

  elif not creation:
    try:
      if option == 1:
        encdec.updatedesiredvalue(username, givenvalue, cipherer, graphnumber)
        
      elif option == 2:
        encdec.addnewvalue(username, givenvalue, cipherer, graphnumber)
        
        if graphnumber == 2:
          currenttime = round((datetime.now().time()).hour + ((datetime.now().time()).minute)/60,2)
          encdec.addnewvalue(username, currenttime, cipherer, graphnumber)

      elif option == 3:
        encdec.resetvalue(username, cipherer, graphnumber)

      x, y, z, doexist, cipherer = variables()

      if graphnumber == 1:
        graphonehandling(x, y, z, frame, creation, doexist, target1, username, cipherer, graphnumber)
        target3.config(text="")
      
      elif graphnumber == 2:
        graphtwohandling(x, y, z, frame, creation, doexist, target2, username, cipherer, graphnumber)
        target4.config(text="")
        
    except (InvalidSignature, InvalidToken, ValueError, binascii.Error):
      if graphnumber == 1:
        target3.config(text="KEY INVALID, RESET DATA")
      elif graphnumber == 2:
        target4.config(text="KEY INVALID, RESET DATA")
