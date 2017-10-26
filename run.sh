import csv
import json
import time
import requests


 
f = open('tbl_skpd.csv')
csv_f = csv.reader(f)
next(csv_f)


for row in csv_f:
  time.sleep(30) 
  if row[7] != "":
  	 
  	filename = "json/" + row[0] + ".json"
  
  	url =  "http://maps.google.com/maps/api/geocode/json?address=" +  row[7] + "&sensor=false"

   	loc = requests.get(url)

  	data = loc.json()

   	dataFile = open(filename, 'w')
   	dataFile.write(json.dumps(data, indent=4))	
   	dataFile.close()