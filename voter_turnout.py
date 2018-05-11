import csv, json 
# Non-numeric input key: 
# Midterm: 0 / Presidential: 1
# dem_cand_gender: Male: 0 / Female: 1 

OUTPUT_FILENAME = "voter_turnout.js"
OUTPUT_F = open(OUTPUT_FILENAME, "w")

# read in demographic info: 
voter_turout_filename = 'voter_turnout.csv'
voter_turnout_f = open(voter_turout_filename)
voter_turnout_r = csv.DictReader(voter_turnout_f)

to_output = {}
for row in voter_turnout_r:
	if row['PartyName']=='Democrat':
		if to_output.get(row['PrecinctName'],0) < float(row['VoteCount'])/float(row['Registration']): to_output[row['PrecinctName']] = float(row['VoteCount'])/float(row['Registration'])

OUTPUT_F.write('var vt = ' + json.dumps(to_output) + ';')
