import streamlit as st
import pandas as pd
import numpy as np
from SessionState import get
from login import get_data, planning


import streamlit as st


def is_authenticated(user, password):
    return user == "user" and password == "admin"


def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()

    return block1, block2


def clean_blocks(blocks):
    for block in blocks:
        block.empty()


def login(blocks):
    # blocks[0].markdown("""
    #         <style>
    #             input {
    #                 -webkit-text-security: disc;
    #             }
    #         </style>
    #     """, unsafe_allow_html=True)

    return blocks[0].text_input('Username'), blocks[1].text_input('Password',type='password')


def main():
    st.write("Laporan Kegiatan Dashboard Monev")
    df = get_data()
    planning(df)


login_blocks = generate_login_block()
user, password = login(login_blocks)

if is_authenticated(user, password):
    st.write("Login as User from IT Department")
    clean_blocks(login_blocks)
    main()
elif password:
    st.info("Incorrect username/password")
    


