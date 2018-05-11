import csv, json

cook_geojson_filename = "../../GeoJSON files/Cook.json"
cook_geojson_f = open(cook_geojson_filename)
cook_json = cook_geojson_f.readline()
cook_r = json.loads(cook_json)
cook_names = {}
for feature in cook_r['features']:
	cook_names[feature['properties']['name'].title() + " " + feature['properties']['num']] = feature['properties']['idpct_txt']

counties = ["Cook","Dupage","Kane","Lake","McHenry"]

precincts = {"cook": {}, "kane": {}, "lake": {}, "dupage": {}, "mchenry": {}}
dem_candidates = ["Michael Mason"]

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
	filename = county + "Rep.csv"
	f = open(filename)
	reader = csv.DictReader(f)
	for row in reader:
		precinct_name = row['Precinct']
		if county=='Dupage' or county=='McHenry': precinct_name = precinct_name.title()
		if county=='Cook': precinct_name = cook_names[precinct_name]
		if county=="McHenry": precincts[county.lower()][precinct_name]['Peter J. Roskam'] = row['Peter J. Roskam Number']
		else: precincts[county.lower()][precinct_name]['Peter J. Roskam'] = row['Peter J. Roskam']

output_filename = "2014PrimaryCongressional.csv"
output_f = open(output_filename, "w")
output_w = csv.DictWriter(output_f, fieldnames=["County","Precinct","Michael Mason",'Peter J. Roskam'])
output_w.writeheader()

counties = ["cook", "kane", "lake", "dupage", "mchenry"]

for county in counties:
	for precinct in precincts[county]:
		r = {'County': county, 'Precinct': precinct, 'Peter J. Roskam': precincts[county][precinct]['Peter J. Roskam'], 'Michael Mason': precincts[county][precinct]['Michael Mason']}
		output_w.writerow(r)









