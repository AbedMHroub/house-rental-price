from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import io

#Fetching data via web scraping
#Here is the link to the site that I scraped
url = "https://shobiddak.com/houses/"

out_filename = "dataset.csv"
# header of csv file to be written
headers = "date,houseId,category,city,address,houseType,status,numberRooms,numberBathrooms,numberKitchens,numberBalconies,loungeType,houseSpace,landArea,elevator,carParking,heating,price,priceType \n"
# opens file, and writes headers
f = io.open(out_filename, "w", encoding="utf-8")
f.write(headers)
print("scraping from ", url)
print("Please wait ...")
for page_id in range( 240000, 260087):
    
    page_url = url+str(page_id)
    #send request and fetch html page
    uClient = uReq(page_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    
    header    = page_soup.findAll("h2", {"class": "section_title"})
    #Check the HTML page is blank or not
    if header != []:
        print(page_id)
        category = header[0].text.split()[1]
        homeType = header[0].text.split()[0]
        city     = header[1].findAll("a")[0].text
        if len(header[1].findAll("a")) >= 2 :
            address  = header[1].findAll("a")[1].text
        else :  address  = " "
        #Empty the initial values
        status          = " "
        numberRooms     = " "  
        numberBathrooms = " "
        numberKitchens  = " "
        numberBalconies = " "
        loungeType      = " " 
        houseSpace      = " "
        landArea        = " "
        elevator        = " "
        carParking      = " "
        heating         = " "
        date            = " "
        price           = " "
        priceType       = " "
        #Accessing the necessary data and dealing with it
        tables = page_soup.findAll("tr", {"class": "list-row"})
        for table in tables:
            td = table.findAll("td")
            if td[0].text == 'السعر':
                    price = td[1].text.split()[0]
                    if len(td[1].text.split()) == 2 :
                        priceType = td[1].text.split()[1]
                    else :
                        priceType = " " 
            elif td[0].text == 'عدد الغرف':
                    numberRooms = td[1].text
            elif td[0].text == 'الحالة':
                    status = td[1].text
            elif td[0].text == 'عدد الحمامات':
                    numberBathrooms = td[1].text
            elif td[0].text == 'عدد المطابخ':
                    numberKitchens = td[1].text
            elif td[0].text == 'عدد البرندات':
                    numberBalconies = td[1].text
            elif td[0].text == 'الصالة':
                    loungeType = td[1].text  
            elif td[0].text == 'المساحة':
                    houseSpace = td[1].text.split()[0]  
            elif td[0].text == 'مساحة الأرض':
                    landArea = td[1].text.split()[0]  
            elif td[0].text == 'يوجد مصعد الكتروني':
                    elevator = td[1].text  
            elif td[0].text == 'يوجد موقف سيارات خاص':
                    carParking = td[1].text  
            elif td[0].text == 'يوجد تدفئة مركزية':
                    heating = td[1].text   
            elif td[0].text == 'تاريخ نشر الإعلان':
                    date = td[1].text 
        
        #Save data in csv file
        f = io.open(out_filename, "w", encoding="utf-8")
        f.write( date + "," + str(page_id) + "," + category + "," )
        f.write( city + "," + address + "," + homeType + "," + status + ",") 
        f.write( numberRooms + "," + numberBathrooms + "," + numberKitchens + ",")
        f.write( numberBalconies + "," + loungeType + "," + houseSpace + ",")
        f.write( landArea + "," + elevator + "," + carParking + "," )
        f.write( heating + "," + price + "," + priceType + "\n")
print("File saved successfully")
f.close()
            
  
    