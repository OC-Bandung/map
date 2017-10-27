import csv
import json
import time
import requests

# read the csv
f = open('tbl_skpd.csv')
csv_f = csv.reader(f)

# skip the first line
next(csv_f)

# for each row in the csv
for row in csv_f:
  time.sleep(3) # first pause (in order not to exceed rate limit or have connection time out)
   # if alamat is not empty, then connect to googmle maps API and save the data in a file with the skpdID.json
  if row[7] != "":
    # create variable for file name
    filename = "json/" + row[0] + ".json"
    # create the request to google maps api
    url =  "https://maps.google.com/maps/api/geocode/json?address=" +  row[7] + "&key=AIzaSyDmGnhhccwog6j_hFmAo8zg1VaYWE_m7Ak&sensor=false"
    #check the url in the terminal to make sure it isok
    print(url)
    # do the request
    loc = requests.get(url)
    # save the request result in variable called data and then write down the variable to a file.
    data = loc.json()
    dataFile = open(filename, 'w')
    # write down the variable, but use json.dump with an indent for pretty printing and good format of json
    dataFile.write(json.dumps(data, indent=4))
    # close the connection to the file and continue the loop
    dataFile.close()