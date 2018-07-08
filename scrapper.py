from selenium import webdriver
import re
import pandas as pd
chrome_path = r"C:\Users\ajite\Desktop\web scraping\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.makemytrip.com/blog/best-party-places-in-goa')

try:
    parent = driver.find_element_by_xpath('/html/body/div[6]/div')
    place = []
    Location = []
    discription = []
    boolean = True
    skip = False
    for child in parent.find_elements_by_xpath('./child::*'):
        if "Book Your Flight to Goa" in child.text:
            break
        if skip == False:
            skip = True
            
            continue
            
        if "Read more" in child.text:
            continue
        if child.text == "":
            continue
        if boolean == True:
            place.append(child.text)
            #print(place[-1])
            boolean = False
        else:
            text = child.text
            if "Location" in text:
                Location.append(text[10:])
                #print(Location[-1])
                boolean = True
            else:
                discription.append(text)
                #print(discription[-1])
        
    
except Exception as e:
    print('Exception found', format(e))

df = pd.DataFrame({'Place': place,
                  'Location': Location,
                  'discription': discription})
df.to_csv(r'C:\Users\ajite\Desktop\web scraping\data.csv')


