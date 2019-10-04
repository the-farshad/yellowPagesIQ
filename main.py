import requests
import bs4
import urllib.parse
import csv

preURL = "http://www.yellowpages.com.iq/search-result.php?id="
csvFile = open('IraqCompanyInformation.csv', 'a')
csvWriter = csv.writer(csvFile)
csvArray = [None]*30

for i in range(1,10569):
    counter = 0
    pageGet = requests.get(preURL+str(i))
    soupReady = bs4.BeautifulSoup(pageGet.content, 'lxml')
    if soupReady.select('script')[0].text == "window.location.href='index.php';":
       continue
    companyName = soupReady.find('h2')
    csvArray[counter] = companyName.text
    counter +=1
    companyCategory = soupReady.find('h5')
    csvArray[counter] = companyCategory.text
    counter +=1
    companyInformationDetails = soupReady.select('div p span')
    for companyDetails in companyInformationDetails:
        csvArray[counter] = companyDetails.text
        counter +=1
    counter = 18
    contactDetails = soupReady.select('div ul li span')
    for detail in contactDetails:
        csvArray[counter] = detail.text
        counter +=1
        print (detail.text)
    print (csvArray)
    csvWriter.writerow(csvArray)

print(i)
csvFile.close()
