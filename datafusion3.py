import json
import urllib
#your api key
api_key = 'AIzaSyAGjVS9JMid1ItJcql-flIHasfEmsAG7Ag'
service_url = 'https://www.googleapis.com/freebase/v1/mqlread' 
query =[{
  "type": "/film/film",
  "id": None,
  "name": None,
  "/film/film/starring": [{
    "actor": [{
      "name": None,
      "id": None,
      "/award/award_winner/awards_won": [{
        "/award/award_honor/ceremony~=": "Academy Awards"
      }]
    }],
    "return": "count"
  }],
  #"sort": "-/film/film/starring.count",
  
  #"limit":5
}]
params = {
        'query': json.dumps(query),
        'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
response['result'].sort(reverse=True)

br=0
for film in response['result']:
  br+=1
  print 'Film: '+film['name']+', total oscar actors starring : '+str(film['/film/film/starring'])
  if br==5: 
  	exit()
