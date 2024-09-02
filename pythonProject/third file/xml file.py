import xml.etree.ElementTree as ET
data = ''' 
<person>
	<name>Emeka</name>
	<phone type="intl"> +1 734 303 4456 </phone> 
	<email hide="yes"/>
	<name> Habeeb </name>
</person>'''
tree = ET.fromstring(data)          # this fromstring is used to convert the string to XML
print("name: ", tree.find("name").text) #text is used to convert your output to text
print("Phone", tree.find("phone").text)

# name = tree.findall("name")
# for name in name:
#     print(name.text)


name = tree.findall("name")
myNameList = []
for name in name:
    myNameList.append(name.text)
print(myNameList[1])

