import streamlit as st
from datetime import date

st.set_page_config(
        page_title="My Page Title",
)

today = str(date.today())

name = st.text_input('What is your name?')
bday = str(st.date_input('What is your birthday?'))
if st.button('Submit'):
    st.balloons()
    st.write(f'Why hello there {name}!')
    if bday[-5:] == today[-5:]:
        st.write('WOOOOOOO Happy birthday!')
    else:
        st.write('A very happy unbirthday to you!')
