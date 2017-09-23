#NOTE ENCODING OF TEXT FILE MUST BE ANSI
import csv
import html.parser
import tkinter as tk
from tkinter import filedialog

print("This program automatically creates a csv file for emails received from the Global Cache Control Tower Database.  To use this program we must save the text version of the email, in Gmail this would be the Arrow_Down (next to the reply arrow),  Select show_original, Click Download_Original. \n")

root = tk.Tk()
root.withdraw()

print("Pick the ANSI raw text file created from the email sent by Global Cache. \n")
file_path = filedialog.askopenfilename()
if file_path is "":
    print("No file selected")
    exit()
#The file
f = open(file_path, 'r')

#Input this data
Brand = input("Enter Brand Name: ")
if Brand is "":
    Brand = "Brand Name"
#print("Brand is>",Brand, "<")

Device = input("Enter Device Type: ")
if Device is "":
    Device = "Device Name"

Model = input("Enter Device Model: ")
if Model is "":
    Model = "Model Name"

unicodefile = f.read()
html_parser = html.parser.HTMLParser()
file = html_parser.unescape(unicodefile)


#This splits the ir codes from the email data
email = file.split('''<p>function, code1, hexcode1, code2, hexcode2</p><p>''')
#this removes the email data from the array
email = email.pop(1)

#print(email)

#the list used for each of the ir code data
listforcsv = []

#headings
listforcsv.append(["Brand", "Device", "Model", "Button","GC code 1", "hex Code 1", "GC code 2", "hex code 2" ])


#split the email by ir code data
email = email.replace('''=''', "")
email = email.replace('''\n''', "")
ircodes = email.split('''</p>''')
#remove the last item as it will be blank
ircodes.pop(-1)


for ircodedata in ircodes:
    ircodedata = ircodedata.replace('''<p>''', "")
    #print (ircodedata)

    ircode = ircodedata.split('''","''')
    #clean the unused chars out array


    try:
        buttonName = ircode[0].replace('''",,''', "").replace('''",''', "").replace('''"''', "")
    except:
        buttonName = "None"
    #print(buttonName)
    try:
        gccodeone = ircode[1].replace('''",,''', "").replace('''",''', "").replace('''"''', "")
    except:
        gccodeone = "None"
    #print (gccodeone)
    try:
        hexcodeone = ircode[2].replace('''",,''', "").replace('''",''', "").replace('''"''', "")
    except:
        hexcodeone = "None"
    #print (hexcodeone)
    try :
        gccodetwo = ircode[3].replace('''",,''', "").replace('''",''', "").replace('''"''', "")
    except:
        gccodetwo = "None"
    #print  (gccodetwo)
    try:
        hexcodetwo = ircode[4].replace('''",,''', "").replace('''",''', "").replace('''"''', "")
    except:
        hexcodetwo = "None"
    #print (hexcodetwo)

    listforcsv.append([Brand, Device, Model, buttonName, gccodeone, hexcodeone, gccodetwo, hexcodetwo ])

#print(listforcsv)
#create csv file
try:
    fileName = filedialog.asksaveasfilename()
    fileName = fileName + ".csv"
    if fileName is "":
        print("Could not get a file name to save file")
        exit()
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(listforcsv)
        print("Done")
except:
    print("ERROR: Could not write to .csv file, .csv may be in use by another program, user cancel")
    

    
