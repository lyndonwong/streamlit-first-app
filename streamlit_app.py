import streamlit as st
import pandas as pd
import numpy as np

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

dataframe = np.random.randn(5,7)
st.dataframe(dataframe)

# interactive table that highlights minimum values in each column

st.subheader("Interactive Table that highlights minimum values in each column") 

dataframe = pd.DataFrame(
    np.random.randn(11, 17),
    columns=('col %d' % i for i in range(17)),
    index=('row %d' % i for i in range(11))      
)   

st.dataframe(dataframe.style.highlight_min(axis=0)) 

# generate static table with st.table function
st.subheader("Static Table Example")    

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe) 

# Draw a line chart

st.subheader("Line Chart Example")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['apha', 'beta', 'gamma']
)   

st.line_chart(chart_data)

# display table for above chart
st.text("Data table for above chart")
st.dataframe(chart_data)

# Plot a map
st.subheader("Map Plot")
map_data = pd.DataFrame(
    np.random.randn(80, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)    

st.caption("Map data is generated randomly, so it will change every time you refresh the page.")
st.subheader("Lat Lon data table for above map")
st.dataframe(map_data)


