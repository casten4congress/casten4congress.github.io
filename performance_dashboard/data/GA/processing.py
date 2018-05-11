import json
municipalities_list = ['Bartlett', 'Palatine', 'Lisle', 'Lakewood', 'Winfield', 'Carol Stream', 'Downers Grove', 'Westmont', 'Kildeer', 'Glen Ellyn', 'Burr Ridge', 'Long Grove', 'Barrington Hills', 'Wayne', 'Naperville', 'Forest Lake', 'Trout Valley', 'Rolling Meadows', 'Inverness', 'Clarendon Hills', 'St. Charles', 'South Barrington', 'Deer Park', 'Algonquin', 'Hoffman Estates', 'Wheaton', 'Lombard', 'Lake Zurich', 'Port Barrington', 'Hawthorn Woods', 'East Dundee', 'Fox River Grove', 'Lake in the Hills', 'Crystal Lake', 'Darien', 'Oakwood Hills', 'West Dundee', 'Oakbrook Terrace', 'Sleepy Hollow', 'Hinsdale', 'South Elgin', 'Lake Barrington', 'Gilberts', 'Tower Lakes', 'Cary', 'Willowbrook', 'North Barrington', 'Carpentersville', 'Oak Brook', 'Warrenville', 'Elgin', 'Willowbrook', 'West Chicago', 'Barrington']

input_filename = 'L.json'
input_f = open(input_filename)
d = json.loads(input_f.readline())
total = 0
for city in d.keys(): total = total + d[city]
for city in d.keys(): d[city] = float(d[city])/total
for city in municipalities_list: 
	if city not in d.keys(): d[city] = 0
output_filename = 'L.js'
output_f = open(output_filename, 'w')
output_f.write('var l = ' + json.dumps(d) + ';')

input_filename = 'LG.json'
input_f = open(input_filename)
d = json.loads(input_f.readline())
total_female = 0
total_male = 0
for city in d.keys(): 
	total_female = total_female + d[city].get('female',0)
	total_male = total_male + d[city].get('male',0)
for city in d.keys(): 
	d[city]['female'] = float(d[city].get('female',0))/total_female
	d[city]['male'] = float(d[city].get('male',0))/total_male
for city in municipalities_list: 
	if city not in d.keys(): 
		d[city] = {}
		d[city]['female'] = 0
		d[city]['male'] = 0
output_filename = 'LG.js'
output_f = open(output_filename, 'w')
output_f.write('var lg = ' + json.dumps(d) + ';')

input_filename = 'LA.json'
input_f = open(input_filename)
d = json.loads(input_f.readline())
total_18_24 = 0
total_25_34 = 0
total_35_44 = 0
total_45_54 = 0
total_55_64 = 0
total_65 = 0
for city in d.keys(): 
	print city
	total_18_24 += int(d[city].get('18-24',0))
	total_25_34 += int(d[city].get('25-34',0))
	total_35_44 += int(d[city].get('35-44',0))
	total_45_54 += int(d[city].get('45-54',0))
	total_55_64 += int(d[city].get('55-64',0))
	total_65 += int(d[city].get('65+',0))
for city in d.keys(): 
	d[city]['18-24'] = float(d[city].get('18-24',0))/total_18_24
	d[city]['25-34'] = float(d[city].get('25-34',0))/total_25_34
	d[city]['35-44'] = float(d[city].get('35-44',0))/total_35_44
	d[city]['45-54'] = float(d[city].get('45-54',0))/total_45_54
	d[city]['55-64'] = float(d[city].get('55-64',0))/total_55_64
	d[city]['65+'] = float(d[city].get('65+',0))/total_65
for city in municipalities_list: 
	if city not in d.keys(): 
		d[city] = {}
		d[city]['18-24'] = 0
		d[city]['25-34'] = 0
		d[city]['35-44'] = 0
		d[city]['45-54'] = 0
		d[city]['55-64'] = 0
		d[city]['65+'] = 0
output_filename = 'LA.js'
output_f = open(output_filename, 'w')
output_f.write('var la = ' + json.dumps(d) + ';')