import os
import csv
import pyautogui
import time
import pyperclip

def removeBlankPages(dir):

    arr = os.listdir(dir)
    for i in arr:

        b = os.path.getsize(dir + i)

        if b == 16920:

            os.system("rm "+i)




#removeBlankPages("/home/cj/plex/DB Scraping/OhioScraper2.0/")



def pullIDs(dir):
    IDset = set()

    #open CSV up here

    csv = open("IDs.csv","a")



    arr = os.listdir(dir)

    for i in arr:

        #if i is not a directory and if i is not have the file extension .py or csv



        #swap this out on server
        #if ".html" in i:# or just have all files in the folder be what needs to be parsed
        #if i is  os.path.isdir(i) or ".py" not in i or ".csv" not in i:
        if os.path.isdir(i) is False:
            if ".py" not in i:
                if ".csv" not in i:
                    print(i)
                    lines = list(open(i,"r"))

                    for line in lines:
                        if '<a href="offenderdetails.php?OfndrID=' in line and 'img src' not in line:
                            x = line.index('OfndrID=')
                            y = line.index('&AgencyID')

                            IDset.add(line[x+8:y]+',')

    for j in IDset:
        csv.write(j)

#pullIDs("/home/cj/PycharmProjects/OhioScraper2.0/")



def LookupandSaveHTML(id):
    print('[Current ID]'+id)
    #http://www.icrimewatch.net/offenderdetails.php?OfndrID=1571559&AgencyID=55149
    #http://www.icrimewatch.net/offenderdetails.php?OfndrID=
    pyperclip.copy('http://www.icrimewatch.net/offenderdetails.php?OfndrID='+str(id)+'&AgencyID=55149')
    screenWidth, screenHeight = pyautogui.size()
    #print(pyautogui.size())
    currentMouseX, currentMouseY = pyautogui.position()
   # print(pyautogui.position())
    pyautogui.moveTo(599, 111)
    pyautogui.doubleClick()
    pyautogui.press('backspace')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl','s')
    pyperclip.copy(id)
    pyautogui.press('backspace')
    time.sleep(3)
    #pyperclip.paste(id)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)










def getImages():

    with open('IDs.csv', 'r') as f:
        # check LastLocal.txt for place in CSV file
        #   placeholder = open('LastLocal.txt','r')

      #  placeholderint = placeholder.readline()

        reader = csv.reader(f)
        #size = list

        for i in reader:#turns reader into a iterable list
            for j in range(len(i)):#iterates through the cell rows
                LookupandSaveHTML(i[j])




time.sleep(3)


getImages()