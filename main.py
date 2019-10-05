import requests
import bs4
import urllib.parse
import csv

preURL = "http://www.yellowpages.com.iq/search-result.php?id="
csvFile = open('IraqCompanyInformation.csv', 'a')
csvWriter = csv.writer(csvFile)
csvTitle = [None]*30
csvTitle [0:9]= ['Company Name', 'Category','Landmark', 'Building', 'Street', 'City', 'Country', 'Mobile', 'Mobile', 'Email']
csvTitle [20:]= ['Company Name', 'Founded', 'Mobile', 'Phone', 'Website', 'Email', 'Views']
csvWriter.writerow(csvTitle)
try:
    for i in range(1,10600):
        csvArray = [None]*30
        counter = 0
        pageGet = requests.get(preURL+str(i))
        soupReady = bs4.BeautifulSoup(pageGet.content, 'lxml')
        if soupReady.select('script')[0].text == "window.location.href='index.php';":
           continue
        companyName = soupReady.find('h2')
        csvArray[counter] = companyName.text
        companyCategory = soupReady.find('h5')
        counter +=1
        csvArray[counter] = companyCategory.text
        companyInformationDetails = soupReady.select('div p span')
        counter +=1
        for companyDetails in companyInformationDetails:
            companyText = str(companyDetails.text)
            index = companyText.find(':')
            if len(companyText) != 0 and index != -1:
                companyText = companyText[index+1:]
                csvArray[counter] = companyText
                counter += 1
            elif len(companyText) != 0:
                csvArray[counter] = companyDetails.text
                counter +=1
        counter = 20
        contactDetails = soupReady.select('div ul li span')
        for detail in contactDetails:
            csvArray[counter] = detail.text
            counter +=1
        cleanData = []
        for value in csvArray:
            if type(value) == str:
                value = value.strip('')
                if (value == '---'):
                    value = ''
                print(value)
            cleanData.append(value)
        print(cleanData)
        csvWriter.writerow(cleanData)
        print(i)
except:
    print(i)
    csvFile.close()
csvFile.close()
