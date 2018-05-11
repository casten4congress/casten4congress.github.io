import json

input_filename = 'illinois_census_tracts.json'
input_f = open(input_filename)
input_json = json.loads(input_f.readline())
input_tracts = input_json['features']
output_tracts = []

in_district_census_tracts = ['842709', '842708', '850105', '841504', '842702', '871305', '871304', '871307', '871306', '804201', '804202', '845810', '844502', '844501', '850600', '846404', '846405', '841902', '842300', '871301', '846413', '841206', '841205', '864409', '842603', '841209', '841208', '841501', '845807', '845802', '845602', '845601', '841503', '864408', '846412', '844701', '803610', '864403', '843400', '852001', '852003', '852002', '864305', '820000', '851801', '845200', '842602', '841606', '871202', '842601', '841603', '871205', '842604', '842605', '871208', '852101', '852102', '842703', '844402', '844401', '803702', '850701', '864411', '864410', '864407', '846208', '846209', '842200', '845401', '845402', '841703', '803800', '864402', '804109', '804108', '871600', '841901', '804102', '804106', '804105', '804104', '845702', '841308', '845701', '845704', '842500', '803901', '841307', '841314', '843500', '804507', '804506', '804505', '846102', '846105', '846104', '846106', '845508', '845300', '851910', '871201', '846202', '841318', '846205', '841706', '841310', '841704', '841705', '842100', '841316', '864307', '864306', '845502', '864303', '845505', '845506', '845507', '844305', '845509', '871207', '844301', '864308', '871209', '851905', '841325', '841326', '841327', '820101', '844902', '844901', '841323', '851909', '841313', '842400', '841404', '841401', '841403', '803603', '803605', '803604', '803607', '843602', '846002', '846004', '845000', '845510', '844702', '846103', '864412', '841324', '850101', '850106', '850702', '851904', '851907', '871206', '843301', '843302', '842000', '842706', '841321', '852601', '850500', '841801', '846504', '841802', '850103', '871310', '871311', '842710', '842711', '803701', '871404', '871402', '842704', '844802', '844801', '845100', '803608', '841312']


for tract in input_tracts:
	if tract['properties']['TRACTCE'] in in_district_census_tracts: output_tracts.append(tract)

input_json['features'] = output_tracts
output_filename = 'relevant_census_tracts.json'
output_f = open(output_filename, 'w')
output_f.write(json.dumps(input_json))