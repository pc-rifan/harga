import requests
import pandas as pd
from bs4 import BeautifulSoup

maxPage = 10

def antaraNewsJatim(query, startDate, endDate):

	# SCRAPPING PAGE #1
	url = "https://jatim.antaranews.com/search?q=" + query + "&startDate=" + startDate + "&endDate=" + endDate
	webpage = requests.get(url)

	soup = BeautifulSoup(webpage.content, "html.parser")
	elements = soup.find_all("article", class_="simple-post simple-big clearfix")

	judul = []; tanggal = []; link = []

	for element in elements:
		judul.append(element.find("a")["title"])
		tanggal.append(element.find("div", class_="media__date").text)
		link.append(element.find("a")["href"])
	  
	# SCRAPPING OTHER PAGES
	page = 2

	while True:
		url = "https://jatim.antaranews.com/search/" + query + "/" + startDate + "/" + endDate + "/" + str(page)
		webpage = requests.get(url)
		soup = BeautifulSoup(webpage.content, "html.parser")
		elements = soup.find_all("article", class_="simple-post simple-big clearfix")
		
		for element in elements:
			judul.append(element.find("a")["title"])
			tanggal.append(element.find("span").text)
			link.append(element.find("a")["href"])
		
		if len(judul) < 10 or page == maxPage:
			break
		
		page = page + 1
		
	data = {'judul': judul, 'tanggal': tanggal, 'link': link}
	df = pd.DataFrame(data)
	
	return(df)

def detikJatim(query, startDate, endDate):

	page = 1
	startDate = startDate.replace("-", "/")
	endDate = endDate.replace("-", "/")
	judul = []; tanggal = []; link = []

	while True:
		url = "https://www.detik.com/search/searchnews?query=" + query + "&page=" + str(page) + "&result_type=latest&siteid=119&fromdatex=" + startDate + "&todatex=" + endDate
		webpage = requests.get(url)
		soup = BeautifulSoup(webpage.content, "html.parser")
		elements = soup.find_all("article", class_="list-content__item")
		
		for element in elements:
			judul.append(element.find("a")["dtr-ttl"])
			tanggal.append(element.find("div", class_="media__date").text.replace("\n", ""))
			link.append(element.find("a")["href"])
		
		if len(judul) < 10 or page == maxPage:
			break
		
		page = page + 1
		
	data = {'judul': judul, 'tanggal': tanggal, 'link': link}
	df = pd.DataFrame(data)
	
	return(df)
