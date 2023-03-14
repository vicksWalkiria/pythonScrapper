import requests
from bs4 import BeautifulSoup
import csv
 
j = 1
#companyIndex = 0;
for j in range(1,51):
	if j == 1:
		URL = "https://www.informa.es/directorio-empresas/Comunidad_NAVARRA.html"
	else:
		URL = "https://www.informa.es/directorio-empresas/Comunidad_NAVARRA/Empresas-"+str(j)+".html#empresa"
 
	print(URL)	
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")
	table = soup.find("table", class_="empresas_directorio")
	rows = table.find_all("tr")
	i = 0
	for row in rows:
		if i != 0:
			#print(row)
			companies = {}
			name = row.find("td", class_="nom_empresa").find("a").text.strip()
			url = row.find("td", class_="nom_empresa").find("a").attrs['href']
 
			companies[0] = url
			#print(companies)
			#print ("------------------------------")
			csv_columns_register = ['url']
			with open('urls_empresas_navarra.csv', 'a', newline='') as csvfile:
				w = csv.DictWriter(csvfile, companies.keys())
				w.writerow(companies)
		i +=1
	j+=1
