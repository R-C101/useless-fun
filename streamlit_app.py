import streamlit as st
import requests

def sound_techy():
    # Fetch JSON data from the URL
    url = "https://techy-api.vercel.app/api/json"
    response = requests.get(url)
    data = response.json()

    # Check if the response contains the 'message' key
    if 'message' in data:
        # Display the message in bold and big text using Streamlit
        st.markdown(f"<h1 style='text-align: center;'><b>{data['message']}</b></h1>", unsafe_allow_html=True)
    else:
        st.write("No message found in the response. Try again")

def random_facts():
    # Define the base URL of the API
    base_url = "https://uselessfacts.jsph.pl/api/v2/facts"

    # Define the endpoint you want to access
    endpoint = "/random"

    # Define parameters for language and content type
    params = {
        "language": "en"  # Specify the language you want to receive the fact in (optional)
    }

    # Define headers for content type
    headers = {
        "Accept": "application/json"  # Specify the desired content type (optional)
    }

    # Make the request
    response = requests.get(base_url + endpoint, params=params, headers=headers)

    # Check if the request was successful (status code 200)
    if 'text' in response.json:
        # Display the message in bold and big text using Streamlit
        st.markdown(f"<h1 style='text-align: center;'><b>{response.json['text']}</b></h1>", unsafe_allow_html=True)
    else:
        st.write("No message found in the response. Try again")