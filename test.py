import time
import datetime
import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup


st.subheader("SCRAPPING BERITA ONLINE")

today = datetime.datetime.now()

form = st.form(key='Scrapping Berita')
query = form.text_input('Masukan kata kunci')
startDate = form.date_input('Periode awal berita', datetime.date(today.year, today.month, 1), format="DD-MM-YYYY").strftime("%DD-%MM%-%YYYY")
endDate = form.date_input('sampai dengan', today, format="DD-MM-YYYY").strftime("%DD-%MM%-%YYYY")
submit = form.form_submit_button('Scrape Now!')

df = pd.DataFrame()

page = 1
maxPage = 10

if submit:

	st.write(startDate)
	st.write(endDate)

	startDate = str(startDate).replace("-", "/")
	endDate = str(endDate).replace("-", "/")
	judul = []; tanggal = []; link = []

	st.write(startDate)
	st.write(endDate)
	
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
	
	st.write(df)
