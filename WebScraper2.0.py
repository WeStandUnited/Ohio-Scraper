import os
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse






def getCityList(URL):
    #make csv file named after state
    #f = open(stateName+".csv", "a")


    #extract city names from HTML

    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html,'html.parser')
    #table = soup.table
    table = soup.find('table')
    table_rows =table.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        #if len(row) > 2:
        print(row)
    return 0



#MAX PAGE -> 54

#http://www.icrimewatch.net/results.php?AgencyID=55149&SubmitNameSearch=1&OfndrCity=Columbus&OfndrLast=&OfndrFirst=&level=&AllCity=page+2&altaddr=home_addr&excludeIncarcerated=0&page=54

#http://www.icrimewatch.net/results.php?AgencyID=55149&SubmitNameSearch=1&OfndrCity=

#getCityList("https://en.wikipedia.org/wiki/List_of_cities_in_Ohio")



#link len = 83
#http://www.icrimewatch.net/results.php?AgencyID=55149&SubmitNameSearch=1&OfndrCity=Akron&OfndrLast=&OfndrFirst=&level=&AllCity=page+2&altaddr=home_addr&excludeIncarcerated=0&page=1
#http://www.icrimewatch.net/results.php?AgencyID=55149&SubmitNameSearch=1&OfndrCity=Akron&OfndrLast=&OfndrFirst=&level=&AllCity=page+2&altaddr=home_addr&excludeIncarcerated=0&page=1

#'wget -U "Opera 11.0" '+link+i+link2+str(counter)+' -O '+i+str(counter)+'.html'

def getPages():
    with open("IndianaCities.txt") as f:

        city = f.readlines()

    #print(city)
    #Empty page is 16.9 kB (16,933 bytes)

        for i in city:
            for counter in range(51):
                #counter = 50
                os.system('wget -U "Opera 11.0" "http://www.icrimewatch.net/results.php?AgencyID=54663&SubmitNameSearch=1&OfndrCity=' +i+ '&OfndrLast=&OfndrFirst=&level=&AllCity=&altaddr=home_addr&excludeIncarcerated=0&page='+str(counter)+'"-O '+i+str(counter)+'.html')

#wget -U "Opera 11.0" "http://www.icrimewatch.net/results.php?AgencyID=54663&SubmitNameSearch=1&OfndrCity=Indianapolis&OfndrLast=&OfndrFirst=&level=&AllCity=&altaddr=home_addr&excludeIncarcerated=0&page=1" -O 1.html

#getCityList("https://en.wikipedia.org/wiki/List_of_cities_in_Indiana")


#A1001001A19L30A93400I125021.jpg

#A1001001A19C12B62406F678091.jpg

#getPages()
getCityList("https://en.wikipedia.org/wiki/List_of_counties_in_Maryland")