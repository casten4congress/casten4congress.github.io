import json, csv 

geojson_input_filename = 'GeoJSON files/CDLMKnoextra.json'
geojson_input_f = open(geojson_input_filename)
geojson_input = json.loads(geojson_input_f.readline())
new_features = []

election_data_input_filename = 'electiondata/2016GeneralPresidential.csv'
election_data_input_f = open(election_data_input_filename)
election_data_input_r = csv.DictReader(election_data_input_f)

candidates = election_data_input_r.fieldnames - ['County','PrecinctName','Total']
election_data = {row['PrecinctName']: {cand: row[cand] for cand in candidates} for row in election_data_input_r}
for f in geojson_input['features']:
	precinct_name = # FIND THIS 
	f['Name'] = precinct_name
	for cand in candidates: f[cand] = electiondata[precinct_name][cand]
	new_features.append(f)

geojson_input['features'] = new_features

geojson_output_filename = 'GeoJSON files/CDLMKnoextra_xkcd.json'
geojson_output_f = open(geojson_output_filename, 'w')
geojson_output_f.write(json.dumps(geojson_input))