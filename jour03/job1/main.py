import xml.etree.ElementTree as ET
mytree = ET.parse('../domains.xml')
root = mytree.getroot()
count=0
for column in root.findall('.//column'):
    if column.get('name') == 'domain':
        print(column.text)
        count += 1
print("total de noms de domaine enregistrés dans le xml:",count)