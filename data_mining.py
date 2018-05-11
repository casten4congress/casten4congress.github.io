import json 

filename = "data.json"
f = open(filename)
data = json.loads(f.readline())

most_govt_workers = {}
most_self_employed = {}
most_hispanic = {}
most_unemployed = {}
most_single_moms = {}
most_non_family_households = {}
most_income_below_50k = {} # FIGURE THIS OUT 
most_black = {}
most_age_below_25 = {} 
most_age_between_35_and_34 = {}
most_veterans = {}
least_white = {} # FIGURE THIS OUT

keys_and_lists = {"Percent; CLASS OF WORKER - Government workers": most_govt_workers, "Percent; CLASS OF WORKER - Self-employed in own not incorporated business workers": most_self_employed, "Percent; HISPANIC OR LATINO AND RACE - Hispanic or Latino (of any race)": most_hispanic, "Percent; EMPLOYMENT STATUS - Percent Unemployed": most_unemployed, "Percent; HOUSEHOLDS BY TYPE - Family households (families) - Female householder, no husband present, family - With own children under 18 years": most_single_moms, "Percent; HOUSEHOLDS BY TYPE - Nonfamily households - Householder living alone": most_non_family_households, "Percent; RACE - Black or African American": most_black, "Percent; VETERAN STATUS - Civilian veterans": most_veterans, "Percent; SEX AND AGE - 20 to 24 years": most_age_below_25, "Percent; SEX AND AGE - 25 to 34 years": most_age_between_35_and_34}

for neighborhood in data.keys():
	for key in keys_and_lists.keys():
		if (key in data[neighborhood]) and (len(filter(lambda x: x['year']==2016, data[neighborhood][key])) > 0):
			curr_val = filter(lambda x: x['year']==2016, data[neighborhood][key])[0]['val']
			if len(keys_and_lists[key]) < 10:
				keys_and_lists[key][neighborhood] = curr_val
			else:
				minimum = min(keys_and_lists[key], key=keys_and_lists[key].get)
				if curr_val > keys_and_lists[key][minimum]:
					del keys_and_lists[key][minimum]
					keys_and_lists[key][neighborhood] = curr_val

for key in keys_and_lists:
	print key 
	for i in sorted(keys_and_lists[key].keys(), key=lambda x: keys_and_lists[key][x], reverse=True):
		print i + ": " + str(keys_and_lists[key][i])
	print ""
	print ""
	print ""

overlapping_neighborhoods = {}
for key in keys_and_lists.keys():
	for neighborhood in keys_and_lists[key].keys():
		if neighborhood in overlapping_neighborhoods.keys(): overlapping_neighborhoods[neighborhood] = overlapping_neighborhoods[neighborhood]+1
		else: overlapping_neighborhoods[neighborhood] = 1
print "Overlapping Neighborhoods:"
for i in sorted(overlapping_neighborhoods.keys(), key=lambda x: overlapping_neighborhoods[x], reverse=True)[:10]:
	print i + ": " + str(overlapping_neighborhoods[i])



