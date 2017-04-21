import sys
from lxml import html
from bs4 import BeautifulSoup
import urllib.request

def cornellUpdate():
	dates = tourSchedules()
	restaurants = restaurantsNearby()
	hotels = hotelsNearby()
	college = {
			'id': 7,
			'name': 'Cornell University',
			'visits': dates,
			'address': 'Ithaca, NY 14850',
			'zipcode': '14850',
			'restaurants': restaurants,
			'hotels': hotels,
			'picture':'http://www.ivyleaguelifestyle.com/wp-content/uploads/2015/02/cornellarts.jpg'		
			}
	return college

def tourSchedules():
	dates = ["2017-03-27","2017-04-05","2017-04-14","2017-04-19","2017-04-20"]
	sched = {}
	for date in dates:
		partTwo = date[:4]
		partOne = date[5:]
		newDate = partOne+"-"+partTwo
		sched[newDate] = "Info Session and Campus Tours"
	return sched

def restaurantsNearby():
	restaurants = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/RestaurantsNear-g47958-d534362-Cornell_University-Ithaca_Finger_Lakes_New_York.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("div", { "class" : "location_name" })
	for div in mydivs:
			restaurants.append(''.join(div.findAll(text=True)))
			if len(restaurants)>6: return restaurants
	return restaurants

def hotelsNearby():
	hotels = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/HotelsNear-g47958-d534362-Cornell_University-Ithaca_Finger_Lakes_New_York.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("a", { "class" : "property_title" })
	for div in mydivs:
		hotels.append(''.join(div.findAll(text=True)))
		if len(hotels)>4: return hotels
	return hotels