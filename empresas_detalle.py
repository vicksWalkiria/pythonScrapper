from csv import reader
import requests
from bs4 import BeautifulSoup
import csv
 
 
def search( str, table ):
    for elements in table:
        if(elements.find("th").text == str):
            if(str != "Domicilio Social"):
                return elements.find("td").text.strip().replace("\n\t\t\t\t\t\t\t\t\t\t\t\t(CIF)", "")
            else:
                div = elements.find("div", class_="adr")
                address = ""
                for span in div:
                    address += " "+ span.text.strip()
                return address
    return "-"
 
 
# open file in read mode
with open('urls_empresas_navarra.csv', 'r') as read_obj:
# pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
# Iterate over each row in the csv using reader object
    for row in csv_reader:
# row variable is a list that represents a row in csv
        print(row[0])
        for url in row:
            URL = url
            headers = {'User-Agent': 'Mozilla/6.0'}
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")
            #print(soup)
            #soup = BeautifulSoup(open("detalle.html"), "html.parser")
            companies = {}
            table = soup.find("table", class_="vcard datos_ppales")
            print(table)
            
            if 'denominacion' not in companies:
                companies['denominacion'] = search("Denominación", table)
            if 'domicilio_social' not in companies:
                companies['domicilio_social'] = search("Domicilio Social", table)
            if 'telefono' not in companies:
                companies['telefono'] = search("Teléfono", table)
            if 'urls' not in companies:
                companies['urls'] = search("URLS", table)
 
            with open('detalle_empresas.csv', 'a', newline='') as csvfile:
                w = csv.DictWriter(csvfile, companies.keys())
                w.writerow(companies)
 
            print(companies)
