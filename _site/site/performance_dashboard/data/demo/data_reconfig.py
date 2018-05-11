import json 
filename = 'data.json'
f = open(filename)
d = json.loads(f.readline())

relevant_data_titles = ['Percent; SEX AND AGE - Male','Percent; SEX AND AGE - Female','Percent; SEX AND AGE - 20 to 24 years','Percent; SEX AND AGE - 25 to 34 years','Percent; SEX AND AGE - 35 to 44 years','Percent; SEX AND AGE - 45 to 54 years','Percent; SEX AND AGE - 55 to 59 years','Percent; SEX AND AGE - 60 to 64 years','Percent; SEX AND AGE - 65 to 74 years','Percent; SEX AND AGE - 75 to 84 years','Percent; SEX AND AGE - 85 years and over']
relevant_data_sums = {t:0 for t in relevant_data_titles}
total_total_pop = 0
for place in d.keys():
	if place in relevant_data_titles or place=="Estimate; SEX AND AGE - Total population": continue
	total_pop = d[place]["Estimate; SEX AND AGE - Total population"]
	for data_title in d[place].keys():
		d[place][data_title] = float(d[place][data_title]/d[data_title])
		# if data_title in relevant_data_titles: d[place][data_title] = (d[place][data_title]/100)*total_pop
		# else: del d[place][data_title]
	# d[place]["Estimate; SEX AND AGE - Total population"] = total_pop
		# if data_title in relevant_data_titles: relevant_data_sums[data_title] = relevant_data_sums[data_title] + d[place][data_title]
# for t in relevant_data_titles: d[t] = relevant_data_sums[t]

f = open(filename, 'w')
f.write(json.dumps(d))