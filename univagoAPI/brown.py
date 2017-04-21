import sys
from lxml import html
from bs4 import BeautifulSoup
import urllib.request

def brownUpdate():
	dates = tourSchedules()
	restaurants = restaurantsNearby()
	hotels = hotelsNearby()
	brown = {
			'id': 2,
			'name': 'Brown University',
			'visits': dates,
			'address': 'Providence, RI 02912',
			'zipcode': '02912',
			'restaurants': restaurants,
			'hotels': hotels,
			'picture':'https://i.ytimg.com/vi/H6XP70wHa6I/maxresdefault.jpg'
		}
	return brown

def tourSchedules():
	html = urllib.request.urlopen('https://collegeadmission.brown.edu/Datatel.ERecruiting.Web.External/Pages/Events.aspx').read()
	monthAbbreviations = {"January": 1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
	dateList, descriptionList = [], []
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("div", { "class" : "searchResult" })
	for div in mydivs:
		dates = div.findAll("div", { "class" : "event-date"})
		for date in dates:
			dateList.append(''.join(date.findAll(text=True)))
		descriptions = div.findAll("div", {"class" : "event-description"})
		for description in descriptions:
			descriptionList.append(''.join(description.findAll(text=True)))
	duplicateChecker = []
	prevDate = ""
	for date in dateList:
		if date==prevDate:
			duplicateChecker.append(1)
		else:
			duplicateChecker.append(0)
		prevDate = date
	for i in range(len(duplicateChecker)-1,0,-1):
		if duplicateChecker[i]==1:
			del dateList[i]
			del descriptionList[i]
	tourDates = {}
	count = 0
	for date in dateList:
		firstIndex = date.index(' ')
		date = date[firstIndex+1:]
		secondIndex = date.index(' ')
		month = date[:secondIndex]
		date = date[secondIndex+1:]
		thirdIndex = date.index(' ')
		day = date[:thirdIndex-1]
		date = str(monthAbbreviations[month])+"-"+str(day)+"-"+"2017"
		tourDates[date] = descriptionList[count]
		count+=1
	
	new_dates = {}
	counter = 0;
	for date in tourDates:
		if counter < 5:
			new_dates[date] = tourDates[date]
			counter+=1
		else:
			return new_dates

	return tourDates

def restaurantsNearby():
	restaurants = []
	html = urllib.request.urlopen('https://www.opentable.com/landmark/restaurants-near-brown-university?lang=es&page=1').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("a", { "class" : "rest-row-name" })
	for div in mydivs:
		names = div.findAll("span", { "class" : "rest-row-index"})
		for name in names:
			restaurants.append((''.join(name.next_sibling)))
			if len(restaurants)>6: return restaurants
	return restaurants

def hotelsNearby():
	hotels = []
	html = urllib.request.urlopen('https://www.tripadvisor.com/HotelsNear-g60946-d108524-Brown_University-Providence_Rhode_Island.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("a", { "class" : "property_title" })
	for div in mydivs:
		hotels.append(''.join(div.findAll(text=True)))
		if len(hotels)>4: return hotels
	return hotels