#Import the necessary methods from tweepy library

print 'hi'

from bs4 import BeautifulSoup
import requests
import json
import geocoder



page = 'https://www.bandsintown.com/?came_from=257&page='
urlBucket = []
for i in range (0,3):
    uniqueUrl = page + str(i)
    urlBucket.append(uniqueUrl)

#print urlBucket

responseBucket = []

for i in urlBucket:
    uniqueResponse = requests.get(i)
    responseBucket.append(uniqueResponse)


#print responseBucket

soupBucket = []
for i in responseBucket:
    individualSoup = BeautifulSoup(i.text, 'html.parser')
    soupBucket.append(individualSoup)


#print soupBucket

uniqueDatesBucket = []
for i in soupBucket:
   uniqueDate = i.find_all('div', {'class': 'event-b58f7990'})
   uniqueDatesBucket.append(uniqueDate)
   #print (uniqueDate)

#print uniqueDatesBucket
#print (len(uniqueDatesBucket))
uniqueMonth = []
uniqueDates = []

uniqueMonthDayBucket = []

uniqueBandNameBucket = []
for i in soupBucket:
   uniqueBandName = i.find_all('div', {'class': 'event-38a9a08e'})
   uniqueBandNameBucket.append(uniqueBandName)
   #print (uniqueDate)

#print uniqueBandNameBucket

bandNames = []
for entry in uniqueBandNameBucket:
    for band in entry:
        uniqueBand = band.find_all('h2')[0].get_text()
        #print uniqueBand
        #text = uniqueBand.next_element
        #print text
        #uniqueBand.append(bandNames)

#print bandNames

for udb in uniqueDatesBucket:
    for i in udb:
        uniqueMonthDay = i.find_all('div')

        uniqueMonth.append('Month' + uniqueMonthDay[0].text)
        uniqueDates.append('Month: ' + uniqueMonthDay[0].text + ' ' + 'Day: ' + uniqueMonthDay[1].text)

#print uniqueDates
array = [
'https://www.bandsintown.com/?came_from=257&sort_by_filter=Number+of+RSVPs&page=',
'https://www.bandsintown.com/?came_from=257&sort_by_filter=Number+of+RSVPs&page=2',
'https://www.bandsintown.com/?came_from=257&sort_by_filter=Number+of+RSVPs&page=3',
'https://www.bandsintown.com/?came_from=257&sort_by_filter=Number+of+RSVPs&page=4'
]
#print array
url = 'https://www.bandsintown.com/?came_from=257&sort_by_filter=Number+of+RSVPs&page=1'
response = requests.get(url)

for thing in array:
    response2 = requests.get(thing)
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    #print soup2
    dates = soup2.find_all('div', {'class': 'event-b58f7990'})


soup = BeautifulSoup(response.text, 'html.parser')
#print soup
for i in soup.find('div', {'class': 'event-b58f7990'}).find_all('div'):

    #print (i.text)
    x=1


dates = soup.find_all('div', {'class': 'event-b58f7990'})
#print(len(dates))
#print (dates)
month=[]
day=[]
for i in dates:
    md = i.find_all('div')
    month.append(md[0].text)
    day.append(md[1].text)
    #print(md)


entries = []
for i in soupBucket:
   item = {}
   uniqueEntry = i.find_all('div', {'class': 'event-0fe45b3b'})
   #print uniqueEntry
   #uniqueEntry.append(entries)
   for i in uniqueEntry:
       bandEntry = i.find_all('div', {'class': 'event-38a9a08e'})
       dateEntry = i.find_all('div', {'class': 'event-b58f7990'})
       #print dateEntry
       #print bandEntry
      # entries.append('Artist: ' + bandEntry)



       for i in bandEntry:
           name = i.find_all('h2')[0].get_text()
           #print name
           venueInfo = i.find_all('div', {'class': 'event-a7d492f7'})
           venueText = venueInfo[0].text
           #print venueText
           for i in venueInfo:
               venueDiv = i.find_all('div', {'class': 'event-6891d84c'})
               locationDiv = i.find_all('div', {'class': 'event-c5863c62'})
               venue = venueDiv[0].text
               location = locationDiv[0].text
               #entries.append('Artist: ' + name + 'Venue: ' + venue + ' ' + 'location: ' + location)
               item['Artist'] = name
               item['Venue'] = venue
               item['Location'] = location
               #entries.append(item)
               print("Artist: " + item['Artist'])
               print("Venue: " + item['Venue'])
               print("Location: " + item['Location'])
               uniqueLocation = (venue + "," + location)
               geocodedLocation = geocoder.google(uniqueLocation)
               latLong = 'https://maps.googleapis.com/maps/api/geocode/json?address=' +[uniqueLocation] + '&sensor=true'
               print latLong
               #print venue
               #print location
               #location = venueInfo[1].text
           #venue = venueText[1]
           #print venue
           #location = venueInfo[1].text

           for i in venueInfo:
              venue = i.find_all('div', {'class': 'event-6891d84c'})
              location = i.find_all('div', {'class': 'event-c5863c62'})

              #uniqueVenue = venue.text


           #print name

       for i in dateEntry:
           date = i.find_all('div')
           month = date[0].text
           day = date[1].text
           #print day
           #print month
           #entries.append('Artist: ' + name + 'Month: ' + month + 'Day: ' + day)
           item['Day'] = day
           item['Month'] = month
           print("Day: " + item['Day'])
           print("Month: " + item['Month'])



print entries

with open("textbooks5.json", "w") as writeJSON:
   json.dump(item, writeJSON, ensure_ascii=False)
    #for uniqueDate = i.find_all('div', {'class': 'event-b58f7990'})
    #print (uniqueDate)



print ('end')
#event-b58f7990
#eventList-5e5f25ca
# in unique date bucket --- class="event-ad736269"
# event-38a9a08e  - container
# event-5daafce9 - band name
# event-a7d492f7  1st element in child - venue, 2nd element in child - city,State

