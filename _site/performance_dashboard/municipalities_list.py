import json 

municipalities_list = ['Bartlett', 'Palatine', 'Lisle', 'Lakewood', 'Winfield', 'Carol Stream', 'Downers Grove', 'Westmont', 'Kildeer', 'Glen Ellyn', 'Burr Ridge', 'Long Grove', 'Barrington Hills', 'Wayne', 'Naperville', 'Forest Lake', 'Trout Valley', 'Rolling Meadows', 'Inverness', 'Clarendon Hills', 'St. Charles', 'South Barrington', 'Deer Park', 'Algonquin', 'Hoffman Estates', 'Wheaton', 'Lombard', 'Lake Zurich', 'Port Barrington', 'Hawthorn Woods', 'East Dundee', 'Fox River Grove', 'Lake in the Hills', 'Crystal Lake', 'Darien', 'Oakwood Hills', 'West Dundee', 'Oakbrook Terrace', 'Sleepy Hollow', 'Hinsdale', 'South Elgin', 'Lake Barrington', 'Gilberts', 'Tower Lakes', 'Cary', 'Willowbrook', 'North Barrington', 'Carpentersville', 'Oak Brook', 'Warrenville', 'Elgin', 'Willowbrook', 'West Chicago', 'Barrington']

geojson_filename = 'IL_municipalities/municipalities.json'
geojson_f = open(geojson_filename)
geojson_dict = json.loads(geojson_f.readline())
new_features = []
for m in geojson_dict['features']:
	if m['properties']['NAME'] in municipalities_list: new_features.append(m)
geojson_dict['features']=new_features

geojson_f_w = open(geojson_filename, 'w')
geojson_f_w.write(json.dumps(geojson_dict))