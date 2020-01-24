import os
from bs4 import BeautifulSoup




def GetHtml():


    for i in range(664):

        os.system('wget https://www.offenderradar.com/offender/state-california/'+str(i) +' -P /home/cj/CaliHTML')









def ParseHTML(directory):#TODO edit this script use bs4 to

    links = set()
    


    return links


def PutSetinFile():
    with open('Cali.csv','w+') as f:

        #print(len(ParseHTML('/home/cj/CaliHTML/')))
        links2 = ParseHTML('/home/cj/CaliHTML/')


        for i in links2:
            print(i)
            f.write(i+',')





def getImages():

    with open('Cali.csv','r') as f:
        print()








