import streamlit as st
import sqlite3 
import hashlib
import pandas as pd

# Security
#passlib,hashlib,bcrypt,scrypt

SPREADSHEET_ID = '1rkln3HOcmNM79hxNPxX6BPev4yc_ywlHm-LAe6a4j0M' # dashboard monev
FORMAT = 'xlsx'
SHEET_ID = '356714709' # form
url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format={FORMAT}&gid={SHEET_ID}"

df = pd.read_excel(url)

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

	
def get_data():
	# st.write("Laporan Kegiatan Dashboard Monev")
	SPREADSHEET_ID = '1rkln3HOcmNM79hxNPxX6BPev4yc_ywlHm-LAe6a4j0M' # dashboard monev
	FORMAT = 'xlsx'
	SHEET_ID = '1865598876' # form
	url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format={FORMAT}&gid={SHEET_ID}"
	return pd.read_excel(url)

def planning(df):
	planning = df.loc[0,'PLANNING']
	return st.markdown(planning)



	# elif choice == "SignUp":
	# 	st.subheader("Create New Account")
	# 	new_user = st.text_input("Username")
	# 	new_password = st.text_input("Password",type='password')

	# 	if st.button("Signup"):
	# 		create_usertable()
	# 		add_userdata(new_user,make_hashes(new_password))
	# 		st.success("You have successfully created a valid Account")
	# 		st.info("Go to Login Menu to login")



# if __name__ == '__main__':
# 	main()



