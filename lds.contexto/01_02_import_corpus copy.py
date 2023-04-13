import glob
from bs4 import BeautifulSoup 

def html_to_plain_text(): 
    '''this function pulls each general conference talk found in the html_files folder and parses the info for the body text. then, it writes it into a file found in the plain_text_files folder. MAKE SURE you have a file already created named "plain_text_files"'''
    for file in glob.glob("/Users/kathleenbrown/Documents/portfolio/lds.contexto/html_files/*.html"):
        with open(file, "r") as h:
            text = h.read()
        soup = BeautifulSoup(text, 'html.parser') 
        data = soup.find("div", class_='body-block')
        file_name = file.replace("html_files", "plain_text_files")
        file_name = file_name.replace(".html", ".txt")

        with open(file_name, "w") as f: 
            try: 
                f.write(data.get_text(" "))
                print(file_name)
            except AttributeError:
                continue
                
html_to_plain_text()