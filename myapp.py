import streamlit as st
import pandas as pd
import numpy as np
from dashboard import get_data, content

def is_authenticated(user, password):
    return user == "admin" and password == "admin"


def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()

    return block1, block2


def clean_blocks(blocks):
    for block in blocks:
        block.empty()


def login(blocks):
    return blocks[0].text_input('Username'), blocks[1].text_input('Password',type='password')


def main():
    df = get_data("form")
    result = content(df)
    st.title("Laporan Kegiatan Dashboard Monev")
    st.write("Pelapor:", result[0])
    st.write("Kelas Pelapor:", result[1])
    st.write("Tanggal Lapor:", result[7])
    st.subheader("PLANNING")
    st.markdown(result[2])
    st.subheader("DOING")
    st.markdown(result[3])
    st.subheader("CHECKING")
    st.markdown(result[4])
    st.subheader("ACTUATING-FOLLOW UP")
    st.markdown(result[5])
    st.subheader("ACTUATING-HASIL")
    st.markdown(result[6])

login_blocks = generate_login_block()
user, password = login(login_blocks)

if is_authenticated(user, password):
    clean_blocks(login_blocks)
    main()
elif password:
    st.info("Incorrect username/password")
    


