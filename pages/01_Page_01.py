import streamlit as st
import requests



isbn = st.text_input('Please enter ISBN', value="0-7475-3269-9")
key = f'ISBN:{isbn}'

if st.button('SUBMIT'):
    st.balloons()
    response = requests.get(
    'https://openlibrary.org/api/books',
    params={'bibkeys': key, 'format':'json', 'jscmd':'data'},
    ).json()
    st.write('The book is...')
    st.write(response[key]['title'])
