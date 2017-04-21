import sys
from lxml import html
from bs4 import BeautifulSoup
import urllib.request

def northwesternUpdate():
	dates = tourSchedules()
	restaurants = restaurantsNearby()
	hotels = hotelsNearby()
	college = {
			'id': 6,
			'name': 'Northwestern University',
			'visits': dates,
			'address': '633 Clark St, Evanston, IL 60208',
			'zipcode': '60208',
			'restaurants': restaurants,
			'hotels': hotels,
			'picture':'https://s-media-cache-ak0.pinimg.com/originals/bc/96/72/bc9672a93d498dc851ac65c9b0f526d4.jpg'		
			}
	return college

def tourSchedules():
	dates = ["2017-03-28","2017-03-29","2017-04-09","2017-04-10","2017-04-12"]
	sched = {}
	for date in dates:
		partTwo = date[:4]
		partOne = date[5:]
		newDate = partOne+"-"+partTwo
		sched[newDate] = "Campus Tours"
	return sched

def restaurantsNearby():
	restaurants = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/RestaurantsNear-g35972-d144239-Northwestern_University-Evanston_Illinois.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("div", { "class" : "location_name" })
	for div in mydivs:
			restaurants.append(''.join(div.findAll(text=True)))
			if len(restaurants)>6: return restaurants
	return restaurants

def hotelsNearby():
	hotels = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/HotelsNear-g35972-d144239-Northwestern_University-Evanston_Illinois.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("a", { "class" : "property_title" })
	for div in mydivs:
		hotels.append(''.join(div.findAll(text=True)))
		if len(hotels)>4: return hotels
	return hotels