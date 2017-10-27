from pathlib import Path
import json
import csv
import os 

pathlist = Path("json").glob('**/*.json')

fd = open('list.csv','a')
writer = csv.writer(fd, delimiter=',',
                lineterminator='\r\n',
                quotechar = '"'
                )

column_names = ["skpID", "lng", "lat", "place_id", "formatted_address", "administrative_area_level_3" ]

writer.writerow(column_names)

for path in pathlist:
    files = str(path)
    with open(str(path)) as data_file:
    	
    	
    	filename = str(path).split('/')[-1]
    	print (filename)

    	data = json.load(data_file)
    	
    	if data["status"] == "OK":
	    	latitude = (data["results"][0]["geometry"]["location"]["lat"])
	    	lng = (data["results"][0]["geometry"]["location"]["lng"])
	    	
	    	place_id = (data["results"][0]["place_id"])
	    	
	    	formatted_address = (data["results"][0]["formatted_address"])
	    	address_components = (data["results"][0]["address_components"])

	    	for item in address_components:
	    		if 'administrative_area_level_3' in (item["types"]):
	    			administrative_area_level_3 = (item["long_name"])

	    	myCsvRow = [filename, latitude,  lng , place_id , formatted_address, administrative_area_level_3]
	    	
	    	writer.writerow(myCsvRow)


print ("done")
fd.close()