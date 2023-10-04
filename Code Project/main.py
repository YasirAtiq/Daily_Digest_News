## Importing...
import streamlit as st
import requests

## Adding the API url in url variable
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

## Getting the API
response = requests.get(url)
content = response.json()

## Adding title
title = content["title"].split(": ")[1].title()
st.write("""
<style>
h1 {text-align: center;}
</style>
<h1 'style: text-align = center';>%s</h1>
"""% title, unsafe_allow_html=True)

## Adding 2 columns to make the website better.
col1, col2 = st.columns(2)

## Adding the image
st.image(content["hdurl"])

## Adding the description
st.write(f"<p><b>{content['explanation']}</b></p>", unsafe_allow_html=True)
