import os
import csv
import pyautogui
import time
import pyperclip






def ScrapePage():
    #http://www.dpscs.state.md.us/sorSearch/search.do?anchor=offlist&searchType=byCounty&coords=0%2B0&streetAddress=&radius=0.25&firstnm=&lastnm=&county=[COUNTY]
    #&zip=&filter=ALL&category=ALL&start=[INDEX]

    with open("MarylandCounties.txt","r") as f:
        content = f.readlines()

        for i in content:
            print(i.strip())

            index = GetLastIndex(i.strip())

            AutoClicker(i.strip(),index)




#gwt county

#get last index of the county



def GetLastIndex(County):

    pyperclip.copy('http://www.dpscs.state.md.us/sorSearch/search.do?anchor=offlist&searchType=byCounty&coords=0%2B0&streetAddress=&radius=0.25&firstnm=&lastnm=&county='+County+'&zip=&filter=ALL&category=ALL&start='+str(1))

    pyautogui.moveTo(500, 110)

    pyautogui.doubleClick()

    pyautogui.press('backspace')

    pyautogui.hotkey('ctrl', 'v')

    pyautogui.press("enter")

    pyautogui.moveTo(1025,630)

    pyautogui.doubleClick()

    time.sleep(5)

    pyautogui.moveTo(500, 110)

    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl','c')

    index = pyperclip.paste()

    pyautogui.moveTo(500, 110)

    pyautogui.doubleClick()

    pyautogui.press('backspace')

    print(index[index.index('start=')+6:])

    return index[index.index('start=')+6:]
    #returns Last index


def AutoClicker(County,LastIndex):


    Indexref = LastIndex


    while Indexref != -9:




        pyautogui.moveTo(500, 110)

        pyperclip.copy('http://www.dpscs.state.md.us/sorSearch/search.do?anchor=offlist&searchType=byCounty&coords=0%2B0&streetAddress=&radius=0.25&firstnm=&lastnm=&county='+County+'&zip=&filter=ALL&category=ALL&start='+str(Indexref))

        pyautogui.doubleClick()

        pyautogui.press('backspace')

        time.sleep(1)

        pyautogui.hotkey('ctrl','v')

        pyautogui.press("enter")

        time.sleep(6)

        pyautogui.moveTo(1025, 630)

        time.sleep(10)

        pyautogui.hotkey('ctrl','s')

        #type new name
        pyautogui.press('backspace')

        pyperclip.copy(str(Indexref)+County)

        time.sleep(1)

        pyautogui.hotkey('ctrl','v')

        time.sleep(1)

        pyautogui.press("enter")

        time.sleep(3)

        Indexref = int(Indexref) - 10




def MoveImages(dirName,MvDir):
    listOfFile = os.walk(dirName)
    for i in listOfFile:
            print(i[0])
            for j in i:
                for u in j:
                    if '.jpg' in u:
                        print(u)
                        os.system('mv '+i[0]+'/'+u+' '+MvDir)







#time.sleep(2)
#GetLastIndex("Allegany")
#AutoClicker('Allegany',161)
#ScrapePage()
MoveImages('/home/cj/HTML/')