import csv, json

cook_geojson_filename = "../../../GeoJSON files/Cook.json"
cook_geojson_f = open(cook_geojson_filename)
cook_json = cook_geojson_f.readline()
cook_r = json.loads(cook_json)
cook_names = {}
for feature in cook_r['features']:
	cook_names[feature['properties']['name'].title() + " " + feature['properties']['num']] = feature['properties']['idpct_txt']

counties = ["Cook","Dupage","Kane","Lake","McHenry"]

precincts = {"cook": {}, "kane": {}, "lake": {}, "dupage": {}, "mchenry": {}}
dem_candidates = ['Kelly Mazeski','Amanda Howland','Sean Casten','Jennifer Zordani','Becky Anderson Wilkins','Ryan Huffman','Carole Cheney']

def floatize(s):
	s = str(s)
	if s=='': return float(0)
	return float(s.translate(None, ','))

for county in counties:
	filename = county + "Dem.csv"
	f = open(filename)
	reader = csv.DictReader(f)
	for row in reader:
		precinct_name = row['Precinct']
		if county=='Dupage' or county=='McHenry': precinct_name = precinct_name.title()
		if county=="Cook": precinct_name = cook_names[precinct_name]
		if county=="McHenry": precincts[county.lower()][precinct_name] = {cand: row[cand + " Number"] for cand in dem_candidates}
		else: precincts[county.lower()][precinct_name] = {cand: row[cand] for cand in dem_candidates}
		precincts[county.lower()][precinct_name]['Dem Turnout'] = floatize(sum(int(precincts[county.lower()][precinct_name][c]) for c in dem_candidates)) / floatize(row['Registered Voters']) * 100
	filename = county + "Rep.csv"
	f = open(filename)
	reader = csv.DictReader(f)
	for row in reader:
		precinct_name = row['Precinct']
		if county=='Dupage' or county=='McHenry': precinct_name = precinct_name.title()
		if county=='Cook': precinct_name = cook_names[precinct_name]
		if county=="McHenry": precincts[county.lower()][precinct_name]['Peter J. Roskam'] = row['Peter J. Roskam Number']
		else: precincts[county.lower()][precinct_name]['Peter J. Roskam'] = row['Peter J. Roskam']

for county in counties:
	for p in precincts[county.lower()].keys():
		precincts[county.lower()][p]['Dem Percent'] = floatize(sum(int(precincts[county.lower()][p][c]) for c in dem_candidates)) / (floatize(sum(int(precincts[county.lower()][p][c]) for c in dem_candidates)) + floatize(precincts[county.lower()][p]['Peter J. Roskam'])) * 100

output_filename = "2018PrimaryCongressional.csv"
output_f = open(output_filename, "w")
output_w = csv.DictWriter(output_f, fieldnames=["County","Precinct",'Kelly Mazeski','Amanda Howland','Sean Casten','Jennifer Zordani','Becky Anderson Wilkins','Ryan Huffman','Carole Cheney','Peter J. Roskam','Dem Turnout', 'Dem Percent'])
output_w.writeheader()

counties = ["cook", "kane", "lake", "dupage", "mchenry"]

for county in counties:
	for precinct in precincts[county]:
		if county=='dupage': print precincts[county][precinct]
		r = precincts[county][precinct]
		r['County'] = county
		r['Precinct'] = precinct
		output_w.writerow(r)









