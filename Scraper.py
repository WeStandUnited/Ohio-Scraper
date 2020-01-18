import os
import csv
import pyautogui
import time
import pyperclip



#Indiana
#http://www.icrimewatch.net/results.php?AgencyID=54663&SubmitNameSearch=1&OfndrCity=
#Indianapolis
#&OfndrLast=&OfndrFirst=&level=&AllCity=&altaddr=home_addr&excludeIncarcerated=0&
#page=76








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

        #1553850
        
        
        for i in reader:#turns reader into a iterable list
            #print(len(i))
            q = i.index('1553850')
            for j in range(len(i)):#iterates through the cell rows
                #print(len(i))
                j = j + q
                LookupandSaveHTML(i[j])




#time.sleep(3)


#getImages()


#http://www.isp.state.il.us/sor/offenderdetails.cfm?SORID=E17B6303&CFID=154221021&CFTOKEN=7e50730cdfeb1bf0-6C9C44D8-EFE5-5C6F-50B8CC622D624AD4&jsessionid=ec30ac2a4c96b0f0d8447323f604161b91b7
#http://www.isp.state.il.us/sor/offenderdetails.cfm?SORID=E17B2548&CFID=154221021&CFTOKEN=7e50730cdfeb1bf0-6C9C44D8-EFE5-5C6F-50B8CC622D624AD4&jsessionid=ec30ac2a4c96b0f0d8447323f604161b91b7

#time.sleep(3)
#LookupandSaveHTML("1553850")
#LookupandSaveHTML('1537785')