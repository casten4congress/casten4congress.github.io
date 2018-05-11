import json 
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

municipalities_list = ['Bartlett', 'Palatine', 'Lisle', 'Lakewood', 'Winfield', 'Carol Stream', 'Downers Grove', 'Westmont', 'Kildeer', 'Glen Ellyn', 'Burr Ridge', 'Long Grove', 'Barrington Hills', 'Wayne', 'Naperville', 'Forest Lake', 'Trout Valley', 'Rolling Meadows', 'Inverness', 'Clarendon Hills', 'St. Charles', 'South Barrington', 'Deer Park', 'Algonquin', 'Hoffman Estates', 'Wheaton', 'Lombard', 'Lake Zurich', 'Port Barrington', 'Hawthorn Woods', 'East Dundee', 'Fox River Grove', 'Lake in the Hills', 'Crystal Lake', 'Darien', 'Oakwood Hills', 'West Dundee', 'Oakbrook Terrace', 'Sleepy Hollow', 'Hinsdale', 'South Elgin', 'Lake Barrington', 'Gilberts', 'Tower Lakes', 'Cary', 'Willowbrook', 'North Barrington', 'Carpentersville', 'Oak Brook', 'Warrenville', 'Elgin', 'Willowbrook', 'West Chicago', 'Barrington']
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
SERVICE_ACCOUNT_EMAIL = 'ejerzyk@phonic-server-203118.iam.gserviceaccount.com'
KEY_FILE_LOCATION = 'client_secrets.json'
VIEW_ID = '154261248'

def initialize_analyticsreporting():
  """Initializes an Analytics Reporting API V4 service object.

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics


def get_report(analytics, dims, dateranges):
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': dateranges,
          'metrics': [{'expression': 'ga:sessions'}],
          'dimensions': [dims]
        }]
      }
  ).execute()

def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response.

  Args:
    response: An Analytics Reporting API V4 response.
  """
  printP = False 
  mun = ''
  age = ''
  gen = ''
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    to_return = {}
    for row in report.get('data', {}).get('rows', []):
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      for header, dimension in zip(dimensionHeaders, dimensions):
        print header + ": " + dimension
        if header=='ga:city' and dimension in municipalities_list: 
          mun = dimension
          printP = True
        elif header=='ga:userGender': gen = dimension
        elif header=='ga:userAgeBracket': age = dimension

      for i, values in enumerate(dateRangeValues):
        for metricHeader, value in zip(metricHeaders, values.get('values')):
            value = int(value)
            if printP: 
              if gen!='' and age!='': 
                if mun in to_return.keys():
                  if age in to_return[mun].keys(): to_return[mun][age][gen] = value
                  else: to_return[mun] = {age: {gen: value}}
                else: to_return[mun] = {age: {gen: value}}
              elif gen!='': 
                if mun in to_return.keys(): to_return[mun][gen] = value 
                else: to_return[mun] = {gen: value}
              elif age!='': 
                if mun in to_return.keys(): to_return[mun][age] = value 
                else: to_return[mun] = {age: value}
              else: to_return[mun] = value

  return to_return

def LA(dateranges):
  analytics = initialize_analyticsreporting()
  response = get_report(analytics, [{'name': 'ga:city'}, {'name':'ga:userAgeBracket'}], dateranges)
  d = print_response(response)
  total_18_24 = 0
  total_25_34 = 0
  total_35_44 = 0
  total_45_54 = 0
  total_55_64 = 0
  total_65 = 0
  for city in d.keys(): 
    print city
    total_18_24 += int(d[city].get('18-24',0))
    total_25_34 += int(d[city].get('25-34',0))
    total_35_44 += int(d[city].get('35-44',0))
    total_45_54 += int(d[city].get('45-54',0))
    total_55_64 += int(d[city].get('55-64',0))
    total_65 += int(d[city].get('65+',0))
  for city in d.keys(): 
    d[city]['18-24'] = float(d[city].get('18-24',0))/total_18_24
    d[city]['25-34'] = float(d[city].get('25-34',0))/total_25_34
    d[city]['35-44'] = float(d[city].get('35-44',0))/total_35_44
    d[city]['45-54'] = float(d[city].get('45-54',0))/total_45_54
    d[city]['55-64'] = float(d[city].get('55-64',0))/total_55_64
    d[city]['65+'] = float(d[city].get('65+',0))/total_65
  for city in municipalities_list: 
    if city not in d.keys(): 
      d[city] = {}
      d[city]['18-24'] = 0
      d[city]['25-34'] = 0
      d[city]['35-44'] = 0
      d[city]['45-54'] = 0
      d[city]['55-64'] = 0
      d[city]['65+'] = 0
  return d 

def LG(dateranges):
  analytics = initialize_analyticsreporting()
  response = get_report(analytics, [{'name': 'ga:city'}, {'name':'ga:userGender'}], dateranges)
  d = print_response(response)
  total_female = 0
  total_male = 0
  for city in d.keys(): 
    total_female = total_female + d[city].get('female',0)
    total_male = total_male + d[city].get('male',0)
  for city in d.keys(): 
    d[city]['female'] = float(d[city].get('female',0))/total_female
    d[city]['male'] = float(d[city].get('male',0))/total_male
  for city in municipalities_list: 
    if city not in d.keys(): 
      d[city] = {}
      d[city]['female'] = 0
      d[city]['male'] = 0
  return d 

def L(dateranges):
  analytics = initialize_analyticsreporting()
  response = get_report(analytics, [{'name': 'ga:city'}],dateranges)
  d = print_response(response)
  total = 0
  for city in d.keys(): total = total + d[city]
  for city in d.keys(): d[city] = float(d[city])/total
  for city in municipalities_list: 
    if city not in d.keys(): d[city] = 0
  return d 

def main():
  # LA
  output_filename = 'LA.js'
  d = {'1mo': LA([{'startDate': '2018-04-08', 'endDate': 'today'}]), '3mo': LA([{'startDate': '2018-02-08', 'endDate': 'today'}]), '1yr': LA([{'startDate': '2017-05-08', 'endDate': 'today'}])}
  output_f = open(output_filename, 'w')
  output_f.write("var la = " + json.dumps(d) + ";")
  output_f = open(output_filename + 'on', 'w')
  output_f.write(json.dumps(d))
  # LG
  output_filename = 'LG.js'
  d = {'1mo': LG([{'startDate': '2018-04-08', 'endDate': 'today'}]), '3mo': LG([{'startDate': '2018-02-08', 'endDate': 'today'}]), '1yr': LG([{'startDate': '2017-05-08', 'endDate': 'today'}])}
  output_f = open(output_filename, 'w')
  output_f.write("var lg = " + json.dumps(d) + ";")
  output_f = open(output_filename + 'on', 'w')
  output_f.write(json.dumps(d))
  # L
  output_filename = 'L.js'
  d = {'1mo': L([{'startDate': '2018-04-08', 'endDate': 'today'}]), '3mo': L([{'startDate': '2018-02-08', 'endDate': 'today'}]), '1yr': L([{'startDate': '2017-05-08', 'endDate': 'today'}])}
  output_f = open(output_filename, 'w')
  output_f.write("var l = " + json.dumps(d) + ";")
  output_f = open(output_filename + 'on', 'w')
  output_f.write(json.dumps(d))

if __name__ == '__main__':
  main()
