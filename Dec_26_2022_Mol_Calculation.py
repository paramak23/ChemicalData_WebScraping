import requests
import bs4


compound_search = input("Enter the chemical name: ")
source_link = requests.get("https://en.wikipedia.org/wiki/" + compound_search)

chem_name = compound_search

soup = bs4.BeautifulSoup(source_link.text, 'lxml')

table = soup.find("table", class_="infobox ib-chembox")
table_row = table.find_all('tr')
headers = []
for tr_count, row in enumerate(table_row, 1):
    if tr_count == 1:
        continue

    for cell_count, each_cell in enumerate(row, 1):
        if cell_count == 2:
            headers.append(each_cell.text.replace("\n", " ").strip())
            headers.append(each_cell.get_text(strip=True))
        if cell_count == 4:
            headers.append(each_cell.get_text(strip=True))
            headers.append(each_cell.text.replace("\n", " ").strip())
#print(headers)

chem_data = []
#chem_data = {}

for i in range(len(headers)):
    if headers[i] == "Chemical formula":
        cf = headers[i+1]
        chem_data.append(cf)
#        chem_data[headers[i]] = cf
     
    if headers[i] == "Molar mass":
        m = headers[i+1]
        chem_data.append(m)
#        chem_data[headers[i]] = m
     
    if headers[i] == "Density":
        d = headers[i+1]
        chem_data.append(d)
#        chem_data[headers[i]] = d

print(chem_data)
#print(chem_name)
