import os
from bs4 import BeautifulSoup




def GetHtml():


    for i in range(664):

        os.system('wget https://www.offenderradar.com/offender/state-california/'+str(i) +' -P /home/cj/CaliHTML')









def ParseHTML(directory):#TODO edit this script use bs4 to

    links = set()
    
    with open(directory,'r')as f:
        soup = BeautifulSoup(f, 'html.parser')

        #print(soup.prettify())
        #find figure tag

        #get all instnces a <a href= "Some String we want"...</a>

        #(eg)<a href="https://www.offenderradar.com/offender-details/jimmy-ray-odom-of-california-146613" target="_blank">

        #put it in the set
        mod = list(soup.find_all('figure'))

        print(mod[1])





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








ParseHTML('/home/cj/CaliTest/1')