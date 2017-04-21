import sys
from lxml import html
from bs4 import BeautifulSoup
import urllib.request

def uvaUpdate():
	dates = tourSchedules()
	restaurants = restaurantsNearby()
	hotels = hotelsNearby()
	college = {
			'id': 5,
			'name': 'University of Virginia',
			'visits': dates,
			'address': 'Charlottesville, VA 22903',
			'zipcode': '22903',
			'restaurants': restaurants,
			'hotels': hotels,
			'picture':'http://www.campussafetymagazine.com/images/uploads/UVA_Claims_to_Be_the_Victim_of_a_Chinese_Cyberattack.jpg'		
			}
	return college

def tourSchedules():
	dates = ["2017-04-05","2017-04-13","2017-04-18","2017-04-20","2017-04-22"]
	sched = {}
	for date in dates:
		partTwo = date[:4]
		partOne = date[5:]
		newDate = partOne+"-"+partTwo
		sched[newDate] = "Campus Visits and Information Sessions"
	return sched

def restaurantsNearby():
	restaurants = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/RestaurantsNear-g57592-d263627-University_of_Virginia-Charlottesville_Virginia.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("div", { "class" : "location_name" })
	for div in mydivs:
			restaurants.append(''.join(div.findAll(text=True)))
			if len(restaurants)>6: return restaurants
	return restaurants

def hotelsNearby():
	hotels = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/HotelsNear-g57592-d263627-University_of_Virginia-Charlottesville_Virginia.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("a", { "class" : "property_title" })
	for div in mydivs:
		hotels.append(''.join(div.findAll(text=True)))
		if len(hotels)>4: return hotels
	return hotels