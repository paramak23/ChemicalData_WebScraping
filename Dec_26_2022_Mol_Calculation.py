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

mass = m.split("g")
mass = float(mass[0])
#print(type(mass), mass)

for i in chem_data:
    try:
        if i == d:
            density = d.split("g")
            density = float(density[0])
#            print(type(density), density)
    except NameError:
        print("No density value is given in the wikipedia")

g_or_ml = input("Is the weight of the compound given in g or ml: ")

if g_or_ml == 'g':

    val_1 = input('Enter the weight of the compound: ')
   
if g_or_ml == 'ml':
   
    val_1 = input("Enter the volume of the compound: ")
     
if g_or_ml == "g":
   
    class MolCalculation:
        n = 1000
        def __init__(self, weight, mass):
            self.weight = weight
            self.mass = mass
        def mol(self):
            wt = self.weight
            mwt = self.mass
            return wt / mwt
        def mmol(self):
            wt = self.weight
            mwt = self.mass
            return (wt / mwt) * self.n
       
if g_or_ml == "ml":
   
    class MolCalculation:
        n = 1000
        def __init__(self, weight, mass):
            self.weight = weight
            self.mass = mass
        def mol(self):
            wt = self.weight * density
            mwt = self.mass
            return wt / mwt
        def mmol(self):
            wt = self.weight * density
            mwt = self.mass
            return (wt / mwt) * self.n  

calculator = MolCalculation(weight = float(val_1),
mass = float(mass))

print(f'The chemical name of the compound you have entered is: {chem_name}')
print(f'The chemical formula of the compound from wikipedia is: {cf}')  
print(f'The molecular weight of the compound from wikipedia is: {m}')
#print(f'The density of the compound from wikipedia is: {d}')
print(f'The mol of the compound is computed: {calculator.mol():.4f}')
print(f'The mmol of the compound is computed: {calculator.mmol():.2f}')