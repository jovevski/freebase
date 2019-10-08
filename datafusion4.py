import json
import urllib
#your api key
api_key = 'AIzaSyAGjVS9JMid1ItJcql-flIHasfEmsAG7Ag'
service_url = 'https://www.googleapis.com/freebase/v1/mqlread' 
query =[{
  "type": "/military/battle",
  "id": None,
  "name": None,
  "/time/event/start_date": None,
  "/time/event/start_date>": "1000",
  "sort": "-/time/event/start_date",
  "count": None,
  "limit":1000
}]
params = {
        'query': json.dumps(query),
        'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
response['result'].sort()


lista=[]

count = 0
br=0
while (count< 900):
	
  #print 'Battle: '+response['result'][count]['name']+', year : '+str(response['result'][count]['/time/event/start_date'][:4])
  current_year=response['result'][count]['/time/event/start_date'][:4]
  count = count + 1
  br+=1
  
  if current_year != response['result'][count+1]['/time/event/start_date'][:4]:
  	current_year=response['result'][count+1]['/time/event/start_date'][:4]
  	lista.append([br,response['result'][count+1]['/time/event/start_date'][:4]])
  	#print 'vkupno bitki vo '+str(response['result'][count]['/time/event/start_date'][:4])+' se '+str(br)
  	br=0

top=0
lista.sort(reverse=True)	
for x in lista:
	top+=1
	print 'Godina '+str(x[1])+'  Vkupno bitki ='+str(x[0])
	if top==5:
		exit()