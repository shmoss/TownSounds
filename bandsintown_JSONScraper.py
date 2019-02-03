#import the necessary methods from tweepy library

print 'JSON scraper initializing'

from bs4 import BeautifulSoup
import json
import requests
import geocoder


# Set page variable
page = 'https://www.bandsintown.com/?came_from=257&page='
urlBucket = []
for i in range (1,3):
    uniqueUrl = page + str(i)
    urlBucket.append(uniqueUrl)

# Build response container
responseBucket = []

for i in urlBucket:
    uniqueResponse = requests.get(i)
    responseBucket.append(uniqueResponse)


# Build soup container
soupBucket = []
for i in responseBucket:
    individualSoup = BeautifulSoup(i.text, 'html.parser')
    soupBucket.append(individualSoup)


# Build events container
allSanFranciscoEvents = []
for i in soupBucket:
    script = i.find_all("script")[4]
    #print script
    eventsJSON = json.loads(script.text)
    #print eventsJSON
    allSanFranciscoEvents.append(eventsJSON)
    #jsonD = json.dumps(i.text)
    #allScript.append(jsonD)
    #thing = json.loads(jsonD)
    # thing.find_all("eventsJsonLd")
    #print jsonD[8]


print allSanFranciscoEvents

with open("allSanFranciscoEvents3.json", "w") as writeJSON:
   json.dump(allSanFranciscoEvents, writeJSON, ensure_ascii=False)
print ('end')


#Unnecessary Items
#event-b58f7990
#eventList-5e5f25ca
# in unique date bucket --- class="event-ad736269"
# event-38a9a08e  - container
# event-5daafce9 - band name
# event-a7d492f7  1st element in child - venue, 2nd element in child - city,State
