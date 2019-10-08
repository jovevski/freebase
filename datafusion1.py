import json
import urllib

api_key = 'AIzaSyAGjVS9JMid1ItJcql-flIHasfEmsAG7Ag'
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
query =[{
  "type": "/location/country",
  "name": None,
  "id": None,
  "/location/location/people_born_here": [{
    "/people/person/gender": "Female",
    "id": None,
    "/award/award_winner/awards_won": [{
      "/award/award_honor/award": [{

      }]
    }],
    "return": "count"
  }],
  "sort": "-/location/location/people_born_here.count",
  "limit": 5
}]
params = {
        'query': json.dumps(query),
        'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for country in response['result']:
  print 'Country: '+country['name']+' ,Female with Nobel price : '+str(country['/location/location/people_born_here'])
