import os

from bs4 import BeautifulSoup




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

        #swap this out on server
        #if ".py" or ".csv" not in i:
        if ".html" in i:# or just have all files in the folder be what needs to be parsed
            print(i)
            lines = list(open(i,"r"))

            for line in lines:
                if '<a href="offenderdetails.php?OfndrID=' in line and 'img src' not in line:
                    x = line.index('OfndrID=')
                    y = line.index('&AgencyID')

                    IDset.add(line[x+8:y]+',')

    for j in IDset:
        csv.write(j)

pullIDs("/home/cj/PycharmProjects/OhioScraper2.0/")



