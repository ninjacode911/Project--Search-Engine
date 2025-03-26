import streamlit as st
from exa_py import Exa

# Initialize Exa API
exa = Exa("YOUR_KEY_HERE")  # Replace with your actual API key

st.set_page_config(page_title="Custom Search Engine", page_icon="🔍")

st.title("🔍 AI-Powered Search Engine")

query = st.text_input("Enter your search query:")

if query:
    st.write(f"🔎 Searching for: **{query}**...")
    response = exa.search(query, num_results=5)

    if response.results:
        for result in response.results:
            st.markdown(f"### [{result.title}]({result.url})")
    else:
        st.error("No results found. Try a different query.")
