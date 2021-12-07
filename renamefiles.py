import os

folderPath = r'C:\Users\Zakwan\Desktop\604_pages_json\604 pages json'
fileNumber=1

for filename in os.listdir(folderPath):
     os.rename (folderPath + '\\' + filename, folderPath + '\\'+ "page" + str(fileNumber))
     fileNumber +=1
