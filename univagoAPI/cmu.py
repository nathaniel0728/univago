import sys
from lxml import html
from bs4 import BeautifulSoup
import urllib.request

def cmuUpdate():
	dates = tourSchedules()
	restaurants = restaurantsNearby()
	hotels = hotelsNearby()
	college = {
			'id': 8,
			'name': 'Carnegie Mellon University',
			'visits': dates,
			'address': 'Pittsburgh, PA 15213',
			'zipcode': '15213',
			'restaurants': restaurants,
			'hotels': hotels,
			'picture':'https://img.offcampuspartners.com/img.php?src=users/0/0/0/1/1/723606/original.0.jpeg&w=600&h=388'		
			}
	return college

def tourSchedules():
	dates = ["2017-04-02","2017-04-08","2017-04-10","2017-04-14","2017-04-20"]
	sched = {}
	for date in dates:
		partTwo = date[:4]
		partOne = date[5:]
		newDate = partOne+"-"+partTwo
		sched[newDate] = "Information Sessions"
	return sched

def restaurantsNearby():
	restaurants = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/RestaurantsNear-g53449-d4701662-Carnegie_Mellon_University-Pittsburgh_Pennsylvania.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("div", { "class" : "location_name" })
	for div in mydivs:
			restaurants.append(''.join(div.findAll(text=True)))
			if len(restaurants)>6: return restaurants
	return restaurants

def hotelsNearby():
	hotels = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/HotelsNear-g53449-d4701662-Carnegie_Mellon_University-Pittsburgh_Pennsylvania.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("a", { "class" : "property_title" })
	for div in mydivs:
		hotels.append(''.join(div.findAll(text=True)))
		if len(hotels)>4: return hotels
	return hotels