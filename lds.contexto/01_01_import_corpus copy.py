import requests
import re
import datetime
from bs4 import BeautifulSoup

url = "https://www.churchofjesuschrist.org"
header = {'user-agent': 'Kathleen Brown (kmbrown101@gmail.com)'} 

def get_hrefs():
    '''this function loops through each general conference page on the church's website and scrape it for the href of each individual general conference talk'''
    filtered_hrefs = []

    year = datetime.date.today().year

    # for year in range(1971, year + 1): 
    for year in range(2022, year + 1): 
        for month in ['04', '10']:
            print("Getting year: " + str(year) + " month: " + month)

            req = requests.get(url + "/study/general-conference/" + str(year) + "/" + month + "?lang=eng")
            soup = BeautifulSoup(req.text, 'html.parser')
            talk_tags = soup.find_all("a")

            hrefs = []
            for tag in talk_tags:
                hrefs.append(tag.get('href'))

            r = re.compile("\/study\/general-conference\/\d{4}\/\d{2}\/(?!.*-session).*") 
            step1 = list(filter(r.match, hrefs))
            step2 = [*set(step1)]
            filtered_hrefs.extend(step2)   
        #     break # will test one loop
        # break # will test one loop
    return filtered_hrefs

all_hrefs = get_hrefs()
print(len(all_hrefs)) # unnecessary... just helpful to know how many hrefs it's sucessfully pulling

def href_to_html(placeholder_array):
    '''this function takes each href and converts it to a full url, scrapes the whole page and writes it into a file in the html_files folder. MAKE SURE you have a file already created named "html_files"'''
    
    for href in placeholder_array:
        page = url + href
        title = href.replace("/", "_")
        title = title.replace("_study_general-conference_", "")
        title = title.replace("?lang=eng", "")
        print("href: " + href)
        print("full url: " + page)
        response = requests.get(page)
        src = response.text.encode('latin1').decode('utf-8')
        
        with open("/Users/kathleenbrown/Documents/portfolio/lds.contexto/html_files/" + title + ".html", "w") as f:
            f.write(src)    
            f.close()
        # break # will test one loop

href_to_html(all_hrefs)