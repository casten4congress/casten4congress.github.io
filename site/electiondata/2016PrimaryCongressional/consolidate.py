import csv 

rep_filename = "2016PrimaryCongressionalRep.csv"
dem_filename = "2016PrimaryCongressionalDem.csv"

rep_f = open(rep_filename)
dem_f = open(dem_filename)

rep_r = csv.DictReader(rep_f)
dem_r = csv.DictReader(dem_f)

precincts = {"cook": {}, "kane": {}, "lake": {}, "dupage": {}, "mchenry": {}}

for row in rep_r:
	precinct_name = row['Precinct']
	if row['County']=='McHenry': precinct_name = "Algonquin " + precinct_name.split()[1]
	precincts[row['County'].lower()][precinct_name] = {'Peter J. Roskam': row['PETER J. ROSKAM'], 'Gordon (Jay) Kinzler': row['GORDON (JAY) KINZLER']}
for row in dem_r:
	precinct_name = row['Precinct']
	if row['County']=='McHenry': precinct_name = "Algonquin " + precinct_name.split()[1]
	if precinct_name in precincts[row['County'].lower()].keys():
		precincts[row['County'].lower()][precinct_name]['Robert Marshall'] = row['ROBERT MARSHALL']
		precincts[row['County'].lower()][precinct_name]['Amanda Howland'] = row['AMANDA HOWLAND']
	else:
		precints[row['County'].lower()][precinct_name] = {'Robert Marshall': row['ROBERT MARSHALL'], 'Amanda Howland': row['AMANDA HOWLAND']}

output_filename = '2016PrimaryCongressional.csv'
output_f = open(output_filename,"w")
output_w = csv.DictWriter(output_f, fieldnames=['County','Precinct','Peter J. Roskam', 'Gordon (Jay) Kinzler', 'Robert Marshall', 'Amanda Howland'])
output_w.writeheader()

for county in precincts.keys():
	for precinct in precincts[county].keys():
		r = precincts[county][precinct]
		r['Precinct'] = precinct
		r['County'] = county 
		output_w.writerow(r)