import streamlit as st
import requests



isbn = st.text_input('Please enter ISBN', value="978-1473619791")
key = f'ISBN:{isbn}'

if st.button('SUBMIT'):
    st.snow()
    response = requests.get(
    'https://openlibrary.org/api/books',
    params={'bibkeys': key, 'format':'json', 'jscmd':'data'},
    ).json()
    st.write('The book is...')
    st.write(response[key]['title'])
