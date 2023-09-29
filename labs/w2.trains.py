import requests
import csv
from xml.dom.minidom import parseString

page = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML")
doc = parseString(page.content)

'''#print(doc.toprettyxml())
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)'''
'''
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
print (traincode)'''

TrainLatitudeNodes = doc.getElementsByTagName("TrainLatitude")
for TrainLatitudeNode in TrainLatitudeNodes:
    traincodenode = TrainLatitudeNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
print (traincode)