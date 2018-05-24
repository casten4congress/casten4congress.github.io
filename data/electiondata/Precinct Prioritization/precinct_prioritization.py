import csv, json

# INPUTS
primary_congressional_2018_filename = '../2018PrimaryCongressional/2018PrimaryCongressional.csv'
general_congressional_2016_filename = '../2016GeneralCongressional.csv'
general_presidential_2016_filename = '../2016GeneralPresidential.csv'
cook_geojson_filename = "../../../GeoJSON files/Cook.json"

# SCORE WEIGHTS 
score_weights = {'2016GPP': 20, '2016GCP': 20, '2016GPV': 1, '2018PCT': 1, '2018PCP':20}

# OUTPUTS
csv_output = True 
output_filename = 'PrecinctPrioritization.csv'
json_output = True 
json_output_filename = 'PrecinctPrioritization.json'

cook_geojson_f = open(cook_geojson_filename)
cook_json = cook_geojson_f.readline()
cook_r = json.loads(cook_json)
cook_names = {}
for feature in cook_r['features']:
	cook_names[feature['properties']['name'].title() + " " + feature['properties']['num']] = feature['properties']['idpct_txt']

def name_normalize(s):
	while ' 0' in s:
		s = s[0:s.find(' 0')+1]+s[s.find(' 0')+2:]
	if 'ALG' in s:
		s = 'Algonquin ' + s.split()[1]
	return s

offices = ['Barrington', 'Downers Grove', 'Elgin', 'West Chicago']
precincts_to_offices = {}

for o in offices: 
	for row in csv.DictReader(open(o+'.csv')):
		if row['Township'] in cook_names.keys(): precincts_to_offices[cook_names[row['Township']]] = o
		else: precincts_to_offices[row['Township']] = o

precincts = {}

def floatize(s):
	if s=='': return float(0)
	else: return float(s)

for row in csv.DictReader(open(general_congressional_2016_filename)):
	if row['Precinct'] not in precincts.keys(): precincts[row['Precinct']] = {'2016GCP': row['Amanda Howland Percent']}
	else: precincts[row['Precinct']]['2016GCP'] = row['Amanda Howland Percent']

for row in csv.DictReader(open(general_presidential_2016_filename)):
	if row['PrecinctName'] not in precincts.keys(): continue 
	else: 
		precincts[row['PrecinctName']]['2016GPP'] = floatize(row['HILLARY CLINTON'])/floatize(row['Total'])*100
		precincts[row['PrecinctName']]['2016GPV'] = row['HILLARY CLINTON']

for row in csv.DictReader(open(primary_congressional_2018_filename)):
	if row['Precinct'] not in precincts.keys(): continue
	else: 
		precincts[row['Precinct']]['2018PCT'] = row['Dem Turnout']
		precincts[row['Precinct']]['2018PCP'] = row['Dem Percent']

if csv_output:
	output_rows = []
	for p in precincts.keys():
		to_append = {k:precincts[p][k] for k in precincts[p].keys()}
		to_append['Precinct'] = p 
		to_append['Office'] = precincts_to_offices[p]
		to_append['Weighted Score'] = sum([floatize(to_append.get(c,0))*score_weights[c] for c in ['2016GPP', '2016GCP', '2016GPV', '2018PCT', '2018PCP']])
		output_rows.append(to_append)
	w = csv.DictWriter(open(output_filename, 'w'), fieldnames=['Precinct', '2016GPP', '2016GCP', '2016GPV', '2018PCT', '2018PCP', 'Office', 'Weighted Score'])
	w.writeheader()
	output_rows = sorted(output_rows, key=lambda x:x['Weighted Score'], reverse=True)
	for r in output_rows: w.writerow(r)

if json_output:
	to_output_json = {}
	for r in output_rows: 
		precinct_name = name_normalize(r['Precinct'])
		del r['Precinct']
		# if precinct_name in cook_names.values(): 
		# 	print 'in cook / original name: ' + precinct_name
		# 	for cn in cook_names.keys():
		# 		if cook_names[cn]==precinct_name: 
		# 			print 'found name: ' + cn
		# 			precinct_name = cn
		to_output_json[precinct_name] = r
	open(json_output_filename, 'w').write(json.dumps(to_output_json))












