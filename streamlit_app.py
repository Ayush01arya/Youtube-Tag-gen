import streamlit as st
import requests

st.title("Youtube Tag Genrator")
a=st.text_input("Enter You Querry","Type here here..")
if st.button("Search"):
   

    query = a
    parms = {"client": "firefox", "q": query, "hl": "en", }
    url = 'http://suggestqueries.google.com/complete/search'
    r = requests.get(url, params=parms)
    r.status_code
    # print(r.status)

    res = r.json()[1]
    for data in res:

        st.write(f"{data}",end='')


#st.markdown("'<h1 style='text-align:center;color:red;'>some</h1>",unsafe_allow_html=True)
