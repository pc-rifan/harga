# IMPORT LIBRARY
import pandas as pd
import streamlit as st
import scrapBerita as sb

st.subheader("SCRAPPING BERITA ONLINE")

form = st.form(key='Scrapping Berita')
query = form.text_input('Masukan kata kunci')
startDate = form.text_input('Periode awal berita (format: DD-MM-YYYY)')
endDate = form.text_input('Periode akhir berita (format: DD-MM-YYYY)')
submit = form.form_submit_button('Scrape Now!')

maxPage = 10
df = pd.DataFrame()

if submit:

	df = antaraNewsJatim(query, startDate, endDate)
    
	st.write('RESULT')
	st.write(df)
