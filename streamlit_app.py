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