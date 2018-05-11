import csv, json

cook_filename = "Cook.csv"
kane_filename = "Kane.csv"
lake_filename = "Lake.csv"
dupage_filename = "Dupage.csv"
mchenry_filename = "McHenry.csv"
cook_geojson_filename = "../../GeoJSON files/Cook.json"

cook_geojson_f = open(cook_geojson_filename)
cook_json = cook_geojson_f.readline()
cook_r = json.loads(cook_json)
cook_names = {}
for feature in cook_r['features']:
	cook_names[feature['properties']['name'].title() + " " + feature['properties']['num']] = feature['properties']['idpct_txt']

cook_f = open(cook_filename)
cook_r = csv.DictReader(cook_f)
kane_f = open(kane_filename)
kane_r = csv.DictReader(kane_f)
lake_f = open(lake_filename)
lake_r = csv.DictReader(lake_f)
dupage_f = open(dupage_filename)
dupage_r = csv.DictReader(dupage_f)
mchenry_f = open(mchenry_filename)
mchenry_r = csv.DictReader(mchenry_f)

precincts = {"cook": {}, "kane": {}, "lake": {}, "dupage": {}, "mchenry": {}}

for row in cook_r:
	precincts["cook"][cook_names[row['Precinct']]] = {"Obama": row["Barack Obama"], "Romney": row["Mitt Romney"]}

for row in kane_r:
	precincts["kane"][row['Precinct']] = {"Obama": row["BARACK OBAMA"], "Romney": row["MITT ROMNEY"]}

for row in lake_r:
	precincts['lake'][row['Precinct']] = {"Obama": row["Barack Obama/Joe Biden"], "Romney": row["Mitt Romney/Paul Ryan"]}

for row in dupage_r:
	precincts['dupage'][row['Precinct']] = {"Obama": row["Barack Obama"], "Romney": row["Mitt Romney"]}

for row in mchenry_r:
	precincts['mchenry'][row['Precinct'].title()] = {"Obama": row["Barack Obama Number"], "Romney": row["Mitt Romney Number"]}

output_filename = "2012GeneralPresidential.csv"
output_f = open(output_filename, "w")
output_w = csv.DictWriter(output_f, fieldnames=["County","Precinct","Obama", "Romney"])
output_w.writeheader()

counties = ["cook", "kane", "lake", "dupage", "mchenry"]

for county in counties:
	for precinct in precincts[county]:
		output_w.writerow({"County": county, "Precinct": precinct, "Obama": precincts[county][precinct]["Obama"], "Romney": precincts[county][precinct]['Romney']})









