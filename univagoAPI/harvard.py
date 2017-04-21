import sys
from lxml import html
from bs4 import BeautifulSoup
import urllib.request

def harvardUpdate():
	dates = tourSchedules()
	restaurants = restaurantsNearby()
	hotels = hotelsNearby()
	college = {
			'id': 4,
			'name': 'Harvard University',
			'visits': dates,
			'address': 'Cambridge, MA 02138',
			'zipcode': '02138',
			'restaurants': restaurants,
			'hotels': hotels,
			'picture':'http://curitibainenglish.com.br/wp-content/uploads/2013/01/Harvard-University-campus.jpg'		
			}
	return college

def tourSchedules():
	dates = ["2017-03-27","2017-03-29","2017-04-06","2017-04-07","2017-04-22"]
	sched = {}
	for date in dates:
		partTwo = date[:4]
		partOne = date[5:]
		newDate = partOne+"-"+partTwo
		sched[newDate] = "Campus Visits & Info Sessions"
	return sched

def restaurantsNearby():
	restaurants = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/RestaurantsNear-g60890-d102687-Harvard_University-Cambridge_Massachusetts.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("div", { "class" : "location_name" })
	for div in mydivs:
			restaurants.append(''.join(div.findAll(text=True)))
			if len(restaurants)>6: return restaurants
	return restaurants

def hotelsNearby():
	hotels = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/HotelsNear-g60890-d102687-Harvard_University-Cambridge_Massachusetts.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("a", { "class" : "property_title" })
	for div in mydivs:
		hotels.append(''.join(div.findAll(text=True)))
		if len(hotels)>4: return hotels
	return hotels