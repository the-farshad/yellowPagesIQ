import requests
import bs4
import urllib.parse
import csv

preURL = "http://www.yellowpages.com.iq/search-result.php?id="
csvFile = open('IraqCompanyInformation', 'a')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['','','',''])
csvArray = [None]*100

for i in range(10500,10569):
    counter = 0
    pageGet = requests.get(preURL+str(i))
    soupReady = bs4.BeautifulSoup(pageGet.content, 'lxml')
    companyName = soupReady.find('h2')
    csvArray[counter] = companyName
    counter +=1
    companyCategory = soupReady.find('h5')
    csvArray[counter] = companyCategory
    counter +=1
    companyInformationDetails = soupReady.select('div p span')
    for companyDetails in companyInformationDetails:
        csvArray[counter] = companyDetails.text
        counter +=1
    counter = 30
    contactDetails = soupReady.select('div ul li span')
    for detail in contactDetails:
        csvArray[counter] = detail
        counter +=1
        print (detail.text)
    print (csvArray)

print(i)
csvFile.close()
