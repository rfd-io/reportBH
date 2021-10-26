import streamlit as st
# import sqlite3 
# import hashlib
import pandas as pd

@st.cache(suppress_st_warning=True)
def get_data(sheets):
	# st.write("Laporan Kegiatan Dashboard Monev")
	SPREADSHEET_ID = '1rkln3HOcmNM79hxNPxX6BPev4yc_ywlHm-LAe6a4j0M' # dashboard monev
	FORMAT = 'xlsx'
	if sheets == 'form':
		SHEET_ID = '1865598876' # form
	elif sheets == 'admin':
		SHEET_ID = '356714709' # admin
	url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format={FORMAT}&gid={SHEET_ID}"
	return pd.read_excel(url)

def content(df):
	st.sidebar.text('Logging in as admin')
	st.sidebar.text('Department: IT')

	users = df['USER'].drop_duplicates()
	users_choice = st.sidebar.selectbox("Pilih Pelapor:",users)
	kelas = df['KELAS'].loc[df['USER'] == users_choice]
	kelas_choice = st.sidebar.selectbox('Pilih Kelas:', kelas) 

	df = df.loc[df['KELAS'] == kelas_choice]
	idx = df.index[0]

	planning = df.loc[idx,'PLANNING']
	doing = df.loc[idx,'DOING']
	checking = df.loc[idx,'CHECKING']
	follow_up = df.loc[idx,'ACTUATING-FOLLOW UP']
	hasil = df.loc[idx,'ACTUATING-HASIL']
	date = df.loc[idx,'Timestamp'].date()

	return users_choice, kelas_choice, planning, doing, checking, follow_up, hasil, date

