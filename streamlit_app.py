import streamlit as st
import pandas as pd

st.title("🎈 Lyndon's first streamlit app in the cloud!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

## Create a sample DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060]
})
 
## Create a map with the data
st.map(data, zoom=1)

"""
### Continue with streamlit get-started guide Basic Concepts
Create a table with data:    
"""

df=pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

# write table manually as well
st.write(df)

# writing an interactive table
import numpy as np

dataframe = np.random.randn(5,7)
st.dataframe(dataframe)

# interactive table that highlights minimum values in each column
dataframe = pd.DataFrame(
    np.random.randn(11, 17),
    columns=('col %d' % i for i in range(17)),
    index=('row %d' % i for i in range(11))      
)   

st.dataframe(dataframe.style.highlight_min(axis=0)) 

# generate static table with st.table function

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe) 

