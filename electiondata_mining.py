import json

filename = "electiondata.json"
f = open(filename)
electiondata = json.loads(f.readline())

precincts = {}
counties = ['cook', 'dupage', 'lake']

for county in counties:
	for precinct in electiondata[county].keys():
		if ('2014GeneralCongressional' in electiondata[county][precinct]) and ('2016GeneralCongressional' in electiondata[county][precinct]) and ('2016GeneralPresidential' in electiondata[county][precinct]):
			precincts[precinct] = {'2014GC2016GC': float(electiondata[county][precinct]['2014GeneralCongressional']['Democrat'])-float(electiondata[county][precinct]['2016GeneralCongressional']['Democrat']), '2016GC2016GP': float(electiondata[county][precinct]['2016GeneralCongressional']['Democrat'])-float(electiondata[county][precinct]['2016GeneralPresidential']['Democrat']), '2016PP2016GPHH': float(electiondata[county][precinct]['2016PrimaryPresidential']['HILLARY CLINTON'])/float(electiondata[county][precinct]['2016PrimaryPresidential']['Total'])*100 - float(electiondata[county][precinct]['2016GeneralPresidential']['Democrat']), '2016PP2016GPBH': float(electiondata[county][precinct]['2016PrimaryPresidential']['BERNIE SANDERS'])/float(electiondata[county][precinct]['2016PrimaryPresidential']['Total'])*100 - float(electiondata[county][precinct]['2016GeneralPresidential']['Democrat']), '2016PP2016GPBD': (float(int(electiondata[county][precinct]['2016PrimaryPresidential']['BERNIE SANDERS'])+int(electiondata[county][precinct]['2016PrimaryPresidential']['HILLARY CLINTON']))/float(electiondata[county][precinct]['2016PrimaryPresidential']['Total'])*100) - float(electiondata[county][precinct]['2016GeneralPresidential']['Democrat'])}

print "2016 Congressional to Presidential: "
l = sorted(precincts.keys(), key=lambda x:precincts[x]['2016GC2016GP'])
for i in l[:20]:
	print i + ": " + str(precincts[i]['2016GC2016GP'])
print "---"
for i in l[len(l)-20:]:
	print i + ": " + str(precincts[i]['2016GC2016GP'])
print ""
l = sorted(precincts.keys(), key=lambda x: precincts[x]['2014GC2016GC'])
print "2014 Congressional to 2016 Congressional"
for i in l[:20]:
	print i + ": " + str(precincts[i]['2014GC2016GC'])
print "---"
for i in l[len(l)-20:]:
	print i + ": " + str(precincts[i]['2014GC2016GC'])
print ""
print "2016 Presidential Primary to General -- Hillary to Hillary"
l = sorted(precincts.keys(), key=lambda x:precincts[x]['2016PP2016GPHH'])
for i in l[:20]:
	print i + ": " + str(precincts[i]['2016PP2016GPHH'])
print "---"
for i in l[len(l)-20:]:
	print i + ": " + str(precincts[i]['2016PP2016GPHH'])
print ""
l = sorted(precincts.keys(), key=lambda x:precincts[x]['2016PP2016GPBH'])
print "2016 Presidential Primary to General -- Bernie to Hillary"
for i in l[:20]:
	print i + ": " + str(precincts[i]['2016PP2016GPBH'])
print "---"
for i in l[len(l)-20:]:
	print i + ": " + str(precincts[i]['2016PP2016GPBH'])
print ""
l = sorted(precincts.keys(), key=lambda x:precincts[x]['2016PP2016GPBD'])
print "2016 Presidential Primary to General -- Bernie to Donald"
for i in l[:20]:
	print i + ": " + str(precincts[i]['2016PP2016GPBD'])
print "---"
for i in l[len(l)-20:]:
	print i + ": " + str(precincts[i]['2016PP2016GPBD'])
