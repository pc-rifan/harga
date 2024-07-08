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
		tanggal.append(element.find("span").text)
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
