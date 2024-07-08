# IMPORT LIBRARY
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

	container = st.warning('This is a warning', icon="⚠️")

	df = sb.antaraNewsJatim(query, str(startDate), str(endDate))

	container = st.success('This is a success')
	
	st.write('RESULT')
	st.write(df)