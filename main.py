import requests
import bs4
import urllib.parse
import csv

preURL = "http://www.yellowpages.com.iq/search-result.php?id="
csvFile = open('IraqCompanyInformation', 'a')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['','','',''])

for i in range(1,10569):
    pageGet = requests.get(preURL+str(i))
    soupReady = bs4.BeautifulSoup(pageGet.content, 'lxml')
    companyName = soupReady.find('h2')
    print (companyName.text)
    # companyCategory =
    # companyAddress =
    # companyContact =
    # companyEmails =
    # companyContactDetails =
    # for companyInformation in


print(i)
csvFile.close()
