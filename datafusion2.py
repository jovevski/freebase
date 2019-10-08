import json
import urllib
#your api key
api_key = 'AIzaSyAGjVS9JMid1ItJcql-flIHasfEmsAG7Ag'
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
industry='Software' #Insert specific industry name
year='2009' #Insert year  
query =[{
  "type": "/business/business_operation",
  "id": None,
  "/business/business_operation/industry": [{
    "name": industry
  }],
  "name": None,
  "/business/business_operation/revenue": [{
    "/measurement_unit/dated_money_value/amount": None,
    "/measurement_unit/dated_money_value/currency": {
      "/finance/currency/currency_code": "USD"
    },
    "/measurement_unit/dated_money_value/valid_date>": year,
    "/measurement_unit/dated_money_value/valid_date": None,
    "limit":1,
  }],
  "sort": "-/business/business_operation/revenue./measurement_unit/dated_money_value/amount",
  "limit": 5
  }]
params = {
        'query': json.dumps(query),
        'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for company in response['result']:
  print 'Company: '+company['name']+' total revenue for year '+year+'  :'
  for a in company['/business/business_operation/revenue']:
      print str(a['/measurement_unit/dated_money_value/amount']) +' '+str(a['/measurement_unit/dated_money_value/currency']['/finance/currency/currency_code'])

