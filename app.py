import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Earthquake Data Explorer')
st.text('This is a web app to explore earthquake data.')
st.markdown('## This is **Markdown**')

uploaded_file = st.file_uploader('Upload your file here')
if uploaded_file:
    st.header('Data statistics')
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())

    st.header('Data Header')
    st.write(df.head())

    fig, ax = plt.subplots(1,1)
    ax.scatter(x = df['Depth'], y = df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    st.pyplot(fig)
