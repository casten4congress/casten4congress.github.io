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
	precincts["cook"][cook_names[row['Precinct']]] = {"Leslie Coolidge": row["Leslie Coolidge"], "Peter J. Roskam": row["Peter J. Roskam"]}

for row in kane_r:
	precincts["kane"][row['Precinct']] = {"Leslie Coolidge": row["LESLIE COOLIDGE"], "Peter J. Roskam": row["PETER J. ROSKAM"]}

for row in lake_r:
	precincts['lake'][row['Precinct']] = {"Leslie Coolidge": row["Leslie Cooldige"], "Peter J. Roskam": row["Peter J. Roskam"]}

for row in dupage_r:
	precincts['dupage'][row['Precinct']] = {"Leslie Coolidge": row["Leslie Coolidge"], "Peter J. Roskam": row["Peter J. Roskam"]}

for row in mchenry_r:
	precincts['mchenry'][row['Precinct'].title()] = {"Leslie Coolidge": row["Leslie Coolidge Number"], "Peter J. Roskam": row["Peter J. Roskam Number"]}

output_filename = "2012GeneralCongressional.csv"
output_f = open(output_filename, "w")
output_w = csv.DictWriter(output_f, fieldnames=["County","Precinct","Leslie Coolidge", "Peter J. Roskam"])
output_w.writeheader()

counties = ["cook", "kane", "lake", "dupage", "mchenry"]

for county in counties:
	for precinct in precincts[county]:
		output_w.writerow({"County": county, "Precinct": precinct, "Leslie Coolidge": precincts[county][precinct]["Leslie Coolidge"], "Peter J. Roskam": precincts[county][precinct]['Peter J. Roskam']})









