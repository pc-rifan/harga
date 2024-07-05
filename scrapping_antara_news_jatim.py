# IMPORT LIBRARY
import io
import requests
import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

# buffer to use for excel writer
buffer = io.BytesIO()


form = st.form(key='Scrapping Antara News Jatim')
query = form.text_input('Masukan kata kunci')
startDate = form.text_input('Isikan tanggal Mulai')
endDate = form.text_input('Isikan tanggal akhir')
submit = form.form_submit_button('Sr')

maxPage = 10

if submit:

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
	st.write('RESULT')
	st.write(df)

# DOWNLOAD TO CSV
df.to_csv(index=False).encode('utf-8')
csv = convert_df(df)

st.download_button(
   "Unduh Hasil",
   csv,
   "scrapping " + query + " " + startDate + " sd " + endDate + ".csv",
   "text/csv",
   key='download-csv'
)
