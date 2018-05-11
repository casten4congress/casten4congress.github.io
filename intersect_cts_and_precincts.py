import json, operator
from shapely.geometry import shape

precincts_filename = "GeoJSON files/CDLMKnoextra.json"
precincts_f = open(precincts_filename)
precincts = json.loads(precincts_f.readline())

cts_filename = "census/illinois_censustracts_2016/illinois_census_tracts.json"
cts_f = open(cts_filename)
cts = json.loads(cts_f.readline())

precinct_to_ct_dict = {}

for precinct in precincts['features']:
	precinct_name = ""
	if 'idpct_txt' in precinct['properties']: precinct_name = precinct['properties']['idpct_txt']
	elif 'PrecinctNa' in precinct['properties']: precinct_name = precinct['properties']['PrecinctNa']
	elif 'TWP_PCT' in precinct['properties']: precinct_name = precinct['properties']['TWP_PCT']
	else:
		if " " in precinct['properties']['PRECINCT']: precinct_name = precinct['properties']['PRECINCT']
		else: precinct_name = precinct['properties']['PRECINCT'][:2] + "00" + precinct['properties']['PRECINCT'][2:]
	print precinct_name
	precinct_shape = shape(precinct['geometry'])
	if not precinct_shape.is_valid: precinct_shape = precinct_shape.buffer(0)
	possibilities = {}
	for ct in cts['features']:
		ct_shape = shape(ct['geometry'])
		if ct_shape.overlaps(precinct_shape) or ct_shape.contains(precinct_shape):
			intscn = ct_shape.intersection(precinct_shape)
			if not intscn.is_empty:
				if intscn.area>=(0.5*precinct_shape.area):
					precinct_to_ct_dict[precinct_name] = ct['properties']['TRACTCE']
				else: possibilities[ct['properties']['TRACTCE']] = intscn.area
	if precinct_name not in precinct_to_ct_dict: precinct_to_ct_dict[precinct_name] = max(possibilities.iteritems(), key=operator.itemgetter(1))[0]


output_filename = "precinct_to_ct.json"
output_f = open(output_filename, 'w')
output_f.write(json.dumps(precinct_to_ct_dict))