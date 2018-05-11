import json, csv

output_filename = "all_census_data.json"
output_f = open(output_filename, 'w')
to_output = {'2012': {}, '2014': {}, '2016': {}}

years = ['2012','2014','2016']
file_types = ['Dem', 'Econ', 'Social']

precinct_to_ct_filename = '../../precinct_to_ct.json'
precinct_to_ct_f = open(precinct_to_ct_filename)
precinct_to_ct_dict = json.loads(precinct_to_ct_f.readline())
relevant_cts = list(set([precinct_to_ct_dict[x] for x in precinct_to_ct_dict.keys()]))

dem_questions = ['Percent; SEX AND AGE - 20 to 24 years', 'Percent; SEX AND AGE - 25 to 34 years', 'Percent; SEX AND AGE - 35 to 44 years', 'Percent; SEX AND AGE - 45 to 54 years', 'Percent; SEX AND AGE - 55 to 59 years', 'Percent; SEX AND AGE - 60 to 64 years', 'Percent; SEX AND AGE - 65 to 74 years', 'Percent; SEX AND AGE - 75 to 84 years', 'Percent; SEX AND AGE - 85 years and over', 'Percent; RACE - White','Percent; HISPANIC OR LATINO AND RACE - Hispanic or Latino (of any race)']
soc_questions = ['Percent; EDUCATIONAL ATTAINMENT - Less than 9th grade','Percent; EDUCATIONAL ATTAINMENT - 9th to 12th grade, no diploma','Percent; EDUCATIONAL ATTAINMENT - High school graduate (includes equivalency)','Percent; EDUCATIONAL ATTAINMENT - Some college, no degree',"Percent; EDUCATIONAL ATTAINMENT - Associate's degree","Percent; EDUCATIONAL ATTAINMENT - Bachelor's degree",'Percent; EDUCATIONAL ATTAINMENT - Graduate or professional degree', 'Percent; LANGUAGE SPOKEN AT HOME - Language other than English - Spanish - Speak English less than "very well"']
ec_questions = ['Percent; INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS) - Less than $10,000', 'Percent; INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS) - $10,000 to $14,999', 'Percent; INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS) - $15,000 to $24,999', 'Percent; INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS) - $25,000 to $34,999', 'Percent; INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS) - $35,000 to $49,999', 'Percent; INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS) - $50,000 to $74,999', 'Percent; INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS) - $75,000 to $99,999', 'Percent; INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS) - $100,000 to $149,999', 'Percent; INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS) - $150,000 to $199,999', 'Percent; INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS) - $200,000 or more']

type_to_question_dict = {'Dem': dem_questions, 'Econ': ec_questions, 'Social': soc_questions}

for year in years:
	print year
	for t in file_types:
		print t 
		filename = year + "/" + t + year + ".csv"
		f = open(filename)
		r = csv.DictReader(f)
		relevant_questions = type_to_question_dict[t]
		for row in r:
			if row['Id2'][5:] in relevant_cts:
				if row['Id2'][5:] not in to_output[year].keys():
					to_output[year][row['Id2'][5:]] = {}
				for question in relevant_questions:
					new_question = question 
					if ("Percent; SEX AND AGE - " in question) and ("ale" in question) and int(year)>2012:
						question_words = question.split()
						gender = question_words[len(question_words)-1]
						new_question = "Percent; SEX AND AGE - Total population - " + gender
					if ("Percent; RACE - " in question) and int(year)>2012:
						question_words = question.split()
						new_question = " ".join(question_words[:3]) + " Race alone or in combination with one or more other races - Total population - " + " ".join(question_words[3:])
					if ("Percent; HISPANIC OR LATINO AND RACE - " in question) and int(year)>2012:
						question_words = question.split()
						new_question = " ".join(question_words[:7]) + " Total population - " + " ".join(question_words[7:])
					if ("Percent; EDUCATIONAL ATTAINMENT" in question) and int(year)>2012:
						question_words = question.split()
						new_question = " ".join(question_words[:4]) + " Population 25 years and over - " + " ".join(question_words[4:])
					if "Percent; INCOME AND BENEFITS" in question:
						new_question = new_question[:36] + year[3] + new_question[37:]
						if int(year)>2012:
							question_words = new_question.split()
							new_question = " ".join(question_words[:9]) + " Total households - " + " ".join(question_words[9:])
					if 'LANGUAGE SPOKEN' in question and int(year)>2012:
						new_question = 'Percent; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Spanish - Speak English less than "very well"'
					txt = row[new_question]
					to_output[year][row['Id2'][5:]][question] = txt

output_f.write(json.dumps(to_output))