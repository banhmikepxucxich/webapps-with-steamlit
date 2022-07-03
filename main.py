import streamlit as st
import pandas

data = {
  'series_1': [1, 3, 4, 5, 7],
  'series_2': [10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)

st.title('toast')
st.subheader('steamlit + toast = the steam lit the toast')
st.write('nice toast bro')
st.write(df)
st.line_chart(df)
