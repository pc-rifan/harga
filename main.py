# IMPORT LIBRARY
import time
import datetime
import pandas as pd
import streamlit as st
import scrapBerita as sb

st.subheader("SCRAPPING BERITA ONLINE")

today = datetime.datetime.now()

form = st.form(key='Scrapping Berita')
query = form.text_input('Masukan kata kunci')
startDate = form.date_input('Periode awal berita', datetime.date(today.year, today.month, 1), format="DD-MM-YYYY")
endDate = form.date_input('sampai dengan', today, format="DD-MM-YYYY")
submit = form.form_submit_button('Scrape Now!')

df = pd.DataFrame()

if submit:

	alert = st.warning('Scraping in progress...', icon="⚠️")

	df = sb.antaraNewsJatim(query, str(startDate), str(endDate))

	alert.empty()
	success = st.success("Success")
	st.write('RESULT')
	st.write(df)

	time.sleep(3)
	success.empty()
