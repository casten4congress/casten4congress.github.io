import csv, json, string

filename = "electiondata/2014GeneralCongressional.csv"
f = open(filename)
reader = csv.DictReader(f)
precincts = { "dupage": {" ".join(row['Precinct'].split()[:len(row['Precinct'].split())-1] + [str(int(row['Precinct'].split()[len(row['Precinct'].split())-1]))]):{'2014GeneralCongressional':{'Democrat': row['Michael Mason Percent'], 'Republican': row['Peter J. Roskam Percent']}} for row in reader if row['County']=='DuPage' }}
f.close()
f = open(filename)
reader = csv.DictReader(f)
precincts["cook"] = {row['Precinct']: {'2014GeneralCongressional': {'Democrat': row['Michael Mason Percent'], 'Republican': row['Peter J. Roskam Percent']}} for row in reader if row['County']=='Cook'}
f.close()
f = open(filename)
reader = csv.DictReader(f)
precincts['lake'] = {row['Precinct']: {'2014GeneralCongressional': {'Democrat': row['Michael Mason Percent'], 'Republican': row['Peter J. Roskam Percent']}} for row in reader if (row['County']=='Lake' and row['Precinct']!="")}
f.close()
f = open(filename)
reader = csv.DictReader(f)
precincts['mchenry'] = {"Algonquin " + row['Precinct'].split()[1]: {'2014GeneralCongressional': {'Democrat': row['Michael Mason Percent'], 'Republican': row['Peter J. Roskam Percent']}} for row in reader if (row['County']=='McHenry')}
f.close()
f = open(filename)
reader = csv.DictReader(f)
precincts['kane'] = {row['Precinct']: {'2014GeneralCongressional': {'Democrat': row['Michael Mason Percent'], 'Republican': row['Peter J. Roskam Percent']}} for row in reader if (row['County']=='Kane')}

filename = "electiondata/2016GeneralCongressional.csv"
f = open(filename)
reader = csv.DictReader(f)
for row in reader:
	if row['County']=='DuPage': 
		precinct_name = " ".join(row['Precinct'].split()[:len(row['Precinct'].split())-1] + [str(int(row['Precinct'].split()[len(row['Precinct'].split())-1]))])
		if precinct_name in precincts['dupage'].keys():
			precincts['dupage'][precinct_name]['2016GeneralCongressional'] = {'Democrat': row['Amanda Howland Percent'], 'Republican': row['Peter J. Roskam Percent']}
		else:
			precincts['dupage'][precinct_name] = {'2016GeneralCongressional': {'Democrat': row['Amanda Howland Percent'], 'Republican': row['Peter J. Roskam Percent']}}
	if row['County']=='Cook':
		if row['Precinct'] in precincts['cook'].keys():
			precincts['cook'][row['Precinct']]['2016GeneralCongressional'] = {'Democrat': row['Amanda Howland Percent'], 'Republican': row['Peter J. Roskam Percent']}
		else:
			precincts['cook'][row['Precinct']] = {'2016GeneralCongressional': {'Democrat': row['Amanda Howland Percent'], 'Republican': row['Peter J. Roskam Percent']}}
	if row['County']=='Lake':
		if row['Precinct'] in precincts['lake'].keys():
			precincts['lake'][row['Precinct']]['2016GeneralCongressional'] = {'Democrat': row['Amanda Howland Percent'], 'Republican': row['Peter J. Roskam Percent']}
		else:
			if row['Precinct'] != "": precincts['lake'][row['Precinct']] = {'2016GeneralCongressional': {'Democrat': row['Amanda Howland Percent'], 'Republican': row['Peter J. Roskam Percent']}}
	if row['County']=='McHenry':
		if "Algonquin " + row['Precinct'].split()[1] in precincts['mchenry'].keys():
			precincts['mchenry']["Algonquin " + row['Precinct'].split()[1]]['2016GeneralCongressional'] = {'Democrat': row['Amanda Howland Percent'], 'Republican': row['Peter J. Roskam Percent']}
		else: precincts['mchenry']["Algonquin " + row['Precinct'].split()[1]] = {'2016GeneralCongressional': {'Democrat': row['Amanda Howland Percent'], 'Republican': row['Peter J. Roskam Percent']}}
	if row['County']=='Kane':
		if row['Precinct'] in precincts['kane'].keys():
			precincts['kane'][row['Precinct']]['2016GeneralCongressional'] = {'Democrat': row['Amanda Howland Percent'], 'Republican': row['Peter J. Roskam Percent']}
		else:
			if row['Precinct'] != "": precincts['kane'][row['Precinct']] = {'2016GeneralCongressional': {'Democrat': row['Amanda Howland Percent'], 'Republican': row['Peter J. Roskam Percent']}}
f.close()

filename = 'electiondata/2016GeneralPresidential.csv'
f = open(filename)
reader = csv.DictReader(f)
for row in reader:
	if (len(row['PrecinctName'].split()) > 1 and (row['PrecinctName'].split()[len(row['PrecinctName'].split())-1].isdigit())):
		precinct_name = " ".join(row['PrecinctName'].split()[:len(row['PrecinctName'].split())-1] + [str(int(row['PrecinctName'].split()[len(row['PrecinctName'].split())-1]))])
		if precinct_name in precincts['dupage'].keys():
			precincts['dupage'][precinct_name]['2016GeneralPresidential'] = {'Democrat': (float(row['HILLARY CLINTON']) / float(row['Total']) * 100.0), 'Republican': (float(row['DONALD TRUMP']) / float(row['Total']) * 100.0),}
	if row['PrecinctName'] in precincts['cook'].keys():
		precincts['cook'][row['PrecinctName']]['2016GeneralPresidential'] = {'Democrat': (float(row['HILLARY CLINTON']) / float(row['Total']) * 100.0), 'Republican': (float(row['DONALD TRUMP']) / float(row['Total']) * 100.0),}
	if row['PrecinctName'] in precincts['lake'].keys():
		precincts['lake'][row['PrecinctName']]['2016GeneralPresidential'] = {'Democrat': (float(row['HILLARY CLINTON']) / float(row['Total']) * 100.0), 'Republican': (float(row['DONALD TRUMP']) / float(row['Total']) * 100.0),}
	if row['County']=='McHenry' and "alg" in row['PrecinctName'].lower():
		if "Algonquin " + row['PrecinctName'].split()[1] in precincts['mchenry'].keys():
			precincts['mchenry']["Algonquin " + row['PrecinctName'].split()[1]]['2016GeneralPresidential'] = {'Democrat': (float(row['HILLARY CLINTON']) / float(row['Total']) * 100.0), 'Republican': (float(row['DONALD TRUMP']) / float(row['Total']) * 100.0),}
	if row['PrecinctName'] in precincts['kane'].keys():
		precincts['kane'][row['PrecinctName']]['2016GeneralPresidential'] = {'Democrat': (float(row['HILLARY CLINTON']) / float(row['Total']) * 100.0), 'Republican': (float(row['DONALD TRUMP']) / float(row['Total']) * 100.0),}
f.close()
filename = 'electiondata/2016PrimaryPresidential/2016PrimaryPresidential.csv'
f = open(filename)
reader = csv.DictReader(f)
primary_candidates = ['HILLARY CLINTON','BERNIE SANDERS','WILLIE L_ WILSON',"MARTIN J_ O'MALLEY",'LARRY COHEN','ROQUE ROCKY DE LA FUENTE','DAVID FORMHALS',"BRIAN O'NEILL w-in",'DONALD J_ TRUMP','TED CRUZ','JOHN R_ KASICH','MARCO RUBIO','BEN CARSON','JEB BUSH','RAND PAUL','CHRIS CHRISTIE','MIKE HUCKABEE','CARLY FIORINA','RICK SANTORUM','JOANN BREIVOGEL', 'Total']
for row in reader:
	if (len(row['PrecinctName'].split()) > 1 and (row['PrecinctName'].split()[len(row['PrecinctName'].split())-1].isdigit())):
		precinct_name = " ".join(row['PrecinctName'].split()[:len(row['PrecinctName'].split())-1] + [str(int(row['PrecinctName'].split()[len(row['PrecinctName'].split())-1]))])
		if precinct_name in precincts['dupage'].keys():
			precincts['dupage'][precinct_name]['2016PrimaryPresidential'] = {}
			for i in primary_candidates: precincts['dupage'][precinct_name]['2016PrimaryPresidential'][i] = (row[i])
	if row['PrecinctName'] in precincts['cook'].keys():
		precincts['cook'][row['PrecinctName']]['2016PrimaryPresidential'] = {}
		for i in primary_candidates: precincts['cook'][row['PrecinctName']]['2016PrimaryPresidential'][i] = (row[i]) 
	if row['PrecinctName'] in precincts['lake'].keys():
		precincts['lake'][row['PrecinctName']]['2016PrimaryPresidential'] = {}
		for i in primary_candidates: precincts['lake'][row['PrecinctName']]['2016PrimaryPresidential'][i] = (row[i])
	if "alg" in row['PrecinctName'].lower():
		if "Algonquin " + row['PrecinctName'].split()[1] in precincts['mchenry'].keys():
			precincts['mchenry']["Algonquin " + row['PrecinctName'].split()[1]]['2016PrimaryPresidential'] = {}
			for i in primary_candidates: precincts['mchenry']["Algonquin " + row['PrecinctName'].split()[1]]['2016PrimaryPresidential'][i] = str(row[i]) 
	if row['PrecinctName'] in precincts['kane'].keys():
		precincts['kane'][row['PrecinctName']]['2016PrimaryPresidential'] = {}
		for i in primary_candidates: precincts['kane'][row['PrecinctName']]['2016PrimaryPresidential'][i] = (row[i])
f.close()
filename = 'electiondata/2012GeneralCongressional/2012GeneralCongressional.csv'
f = open(filename)
reader = csv.DictReader(f)
for row in reader:
	total = int(row['Leslie Coolidge']) + int(row['Peter J. Roskam'])
	precinct_name = row['Precinct']
	if row['County'] == 'dupage': 
		words = precinct_name.split()
		if len(words) > 2: precinct_name = " ".join(words[:len(words)-1] + [str(int(words[len(words)-1]))])
		else:  precinct_name = words[0] + " " + str(int(words[1]))
	if precinct_name in precincts[row['County']].keys():
		precincts[row['County']][precinct_name]['2012GeneralCongressional'] = {'Democrat': float(row['Leslie Coolidge']) / total * 100, 'Republican': float(row['Peter J. Roskam']) / total * 100}
	else:
		precincts[row['County']][precinct_name] = {'2012GeneralCongressional': {'Democrat': float(row['Leslie Coolidge']) / total * 100, 'Republican': float(row['Peter J. Roskam']) / total * 100}}
f.close()
filename = 'electiondata/2012GeneralPresidential/2012GeneralPresidential.csv'
f = open(filename)
reader = csv.DictReader(f)
for row in reader:
	total = int(row['Obama'].translate(None, string.punctuation)) + int(row['Romney'].translate(None, string.punctuation))
	precinct_name = row['Precinct']
	if row['County'] == 'dupage': 
		words = precinct_name.split()
		if len(words) > 2: precinct_name = " ".join(words[:len(words)-1] + [str(int(words[len(words)-1]))])
		else: precinct_name = words[0] + " " + str(int(words[1]))
	if precinct_name in precincts[row['County']].keys():
		precincts[row['County']][precinct_name]['2012GeneralPresidential'] = {'Democrat': float(row['Obama'].translate(None, string.punctuation)) / total * 100, 'Republican': float(row['Romney'].translate(None, string.punctuation)) / total * 100}
	else:
		precincts[row['County']][precinct_name] = {'2012GeneralPresidential': {'Democrat': float(row['Obama'].translate(None, string.punctuation)) / total * 100, 'Republican': float(row['Romney'].translate(None, string.punctuation)) / total * 100}}
f.close()
filename = 'electiondata/2012PrimaryCongressional/2012PrimaryCongressional.csv'
f = open(filename)
reader = csv.DictReader(f)
primary_candidates = ['Leslie Coolidge','Geoffrey Petzel','Maureen E. Yates','Peter J. Roskam']
for row in reader: precincts[row['County']][row['Precinct']]['2012PrimaryCongressional'] = {cand: row[cand] for cand in primary_candidates}
f.close()
filename = 'electiondata/2014PrimaryCongressional/2014PrimaryCongressional.csv'
f = open(filename)
reader = csv.DictReader(f)
primary_candidates = ['Michael Mason', 'Peter J. Roskam']
for row in reader: precincts[row['County']][row['Precinct']]['2014PrimaryCongressional'] = {cand: row[cand] for cand in primary_candidates}
f.close()
filename = 'electiondata/2016PrimaryCongressional/2016PrimaryCongressional.csv'
f = open(filename)
reader = csv.DictReader(f)
primary_candidates = ['Peter J. Roskam', 'Gordon (Jay) Kinzler','Robert Marshall','Amanda Howland']
for row in reader: precincts[row['County']][row['Precinct']]['2016PrimaryCongressional'] = {cand: row[cand] for cand in primary_candidates}
f.close()
filename = 'electiondata/2018PrimaryCongressional/2018PrimaryCongressional.csv'
f = open(filename)
reader = csv.DictReader(f)
primary_candidates = ['Kelly Mazeski','Amanda Howland','Sean Casten','Jennifer Zordani','Becky Anderson Wilkins','Ryan Huffman','Carole Cheney','Peter J. Roskam']
for row in reader: 
	if row['Precinct'] in precincts[row['County']].keys():
		precincts[row['County']][row['Precinct']]['2018PrimaryCongressional'] = {cand: row[cand] for cand in primary_candidates}
	else:
		precincts[row['County']][row['Precinct']] = {'2018PrimaryCongressional': {cand: row[cand] for cand in primary_candidates}}
f.close()


print precincts['dupage'].keys() + precincts['cook'].keys() + precincts['lake'].keys() + precincts['mchenry'].keys() + precincts['kane'].keys()

filename = 'electiondata.js'
f = open(filename, "w")
f.write("var electiondata = " + json.dumps(precincts) + ";")
f.close()
filename = 'electiondata.json'
f = open(filename, 'w')
f.write(json.dumps(precincts))
f.close()