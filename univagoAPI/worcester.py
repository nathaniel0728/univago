import sys
from lxml import html
from bs4 import BeautifulSoup
import urllib.request

def worcesterUpdate():
	dates = tourSchedules()
	restaurants = restaurantsNearby()
	hotels = hotelsNearby()
	michigan = {
			'id': 3,
			'name': 'Worcester Polytechnic Institute',
			'visits': dates,
			'address': '100 Institute Rd, Worcester, MA 01609',
			'zipcode': '01609',
			'restaurants': restaurants,
			'hotels': hotels,
			'picture': 'https://campusencounters.files.wordpress.com/2014/11/wpi-campus-center.jpg'
		}
	return michigan

def tourSchedules():
	html = urllib.request.urlopen('https://www.wpi.edu/news/calendar').read()
	monthAbbreviations = {"Jan": 1, "Feb":2, "Mar":3, "Apr":4, "May":5, "June":6, "July":7, "Aug":8, "Sept":9, "Oct":10, "Nov":11, "Dec":12}
	monthList, dayList = [], []
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("span", { "class" : "event-date-day" })
	dates = {}
	days = []
	for div in mydivs:
		day = ''.join(div.findAll(text=True))
		for i in range(int(day[:2]),int(day[len(day)-2:])+1):
			date = "03"+"-"+str(i)+"-"+"2017"
			if date not in dates:
				dates[date] = "Campus Tour and Information Session"
	
	new_dates = {}
	counter = 0;
	for date in dates:
		if counter < 5:
			new_dates[date] = dates[date]
			counter+=1
		else:
			return new_dates

	return dates

def restaurantsNearby():
	restaurants = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/RestaurantsNear-g41952-d5790223-Worcester_Polytechnic_Institute-Worcester_Massachusetts.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("div", { "class" : "location_name" })
	for div in mydivs:
			restaurants.append(''.join(div.findAll(text=True)))
			if len(restaurants)>6: return restaurants
	return restaurants

def hotelsNearby():
	hotels = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/HotelsNear-g41952-d5790223-Worcester_Polytechnic_Institute-Worcester_Massachusetts.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("a", { "class" : "property_title" })
	for div in mydivs:
		hotels.append(''.join(div.findAll(text=True)))
		if len(hotels)>4: return hotels
	return hotels