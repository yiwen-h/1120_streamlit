import streamlit as st

import numpy as np
import pandas as pd
import random

st.markdown("""# This is a header
## This is a sub header
This is text""")

def get_ran_num():
    ran_num = random.randint(0,100)
    return ran_num
st.write(get_ran_num())

@st.cache_data
def get_ran_num():
    ran_num = random.randint(0,100)
    return ran_num
st.write(get_ran_num())

st.write('I love cats')

st.image('data/best_cat.png')

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df
