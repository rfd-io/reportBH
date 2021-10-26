import streamlit as st
import sqlite3 
import hashlib
import pandas as pd

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management

conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	# c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	# data = c.fetchall()
	data = df.query(f'email == "{username}" & password == "{password}"').values.tolist()
	return data

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def clean_blocks(blocks):
	for block in blocks:
		block.empty()

def login():
	menu = ["Login", "Dashboard"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Login":
		st.subheader("Log In")

		username = st.text_input("Username")
		password = st.text_input("Password",type='password')
		st.button("Login")
		result = login_user(username,password)

		if result:
			st.success(f"Logged In as Fida from IT Department")
		else:
			st.warning("Incorrect Username/Password")
	elif choice == "Dashboard":
		st.write("Laporan Kegiatan Dashboard Monev")

	
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

def planning(df):
	users = df['USER'].drop_duplicates()
	users_choice = st.sidebar.selectbox("Pilih Pelapor:",users)
	kelas = df['KELAS'].loc[df['USER'] == users_choice]
	kelas_choice = st.sidebar.selectbox('Pilih Kelas:', kelas) 

	planning = df.loc[0,'PLANNING']
	return st.markdown(planning)


