import sys
from lxml import html
from bs4 import BeautifulSoup
import urllib.request

def michiganUpdate():
	dates = tourSchedules()
	restaurants = restaurantsNearby()
	hotels = hotelsNearby()
	michigan = {
			'id': 1,
			'name': 'University of Michigan',
			'visits': dates,
			'address': '515 East Jefferson Street, 1220 Student Activities Building Ann Arbor, MI 48109-1316',
			'zipcode': '48109',
			'restaurants': restaurants,
			'hotels': hotels,
			'picture':'https://dalefisherphoto.com/wp-content/uploads/2016/03/062415UMStadiumCityBkgComp9527crop17x38.jpg'		
			}
	return michigan

def tourSchedules():
	html = urllib.request.urlopen('https://admissions.umich.edu/info-session-calendar').read()
	monthAbbreviations = {"Jan": 1, "Feb":2, "Mar":3, "Apr":4, "May":5, "June":6, "July":7, "Aug":8, "Sept":9, "Oct":10, "Nov":11, "Dec":12}
	monthList, dayList = [], []
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("div", { "class" : "date" })
	for div in mydivs:
		link = div.findAll("a")
		if len(link)>0:
			months = div.findAll("span", { "class" : "month"})
			for month in months:
				monthList.append(''.join(month.findAll(text=True)))
				dayList.append(''.join(month.next_sibling.split()))
	dates = {}
	for i in range(0,len(monthList)):
		date = str(monthAbbreviations[monthList[i]])+"-"+str(dayList[i])+"-"+"2017"
		dates[date]="Information Session and Walking Tour"
	
	new_dates = {}
	counter = 0;
	for date in dates:
		if counter < 5:
			new_dates[date] = dates[date];
			counter+=1
		else:
			return new_dates

	return dates

def restaurantsNearby():
	restaurants = []
	html = urllib.request.urlopen('https://www.opentable.com/landmark/restaurants-near-university-of-michigan?page=1').read()
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
	html = urllib.request.urlopen('https://www.tripadvisor.com/HotelsNear-g29556-d107760-University_of_Michigan-Ann_Arbor_Michigan.html').read()
	soup = BeautifulSoup(html, "lxml")
	mydivs = soup.findAll("a", { "class" : "property_title" })
	for div in mydivs:
		hotels.append(''.join(div.findAll(text=True)))
		if len(hotels)>4: return hotels
	return hotels