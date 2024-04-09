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
        
def memes():

    # Fetch memes from the API
    url = "https://api.imgflip.com/get_memes"
    response = requests.get(url)
    data = response.json()

    # Check if the response is successful
    if data['success']:
        memes = data['data']['memes']
        
        st.header("Random Memes")
        
        # Display each meme
        for meme in memes:
            st.subheader(meme['name'])
            st.image(meme['url'], caption=f"ID: {meme['id']}, Width: {meme['width']}, Height: {meme['height']}")
    else:
        st.write("Failed to fetch memes.")

def game_giveaways():

# Function to fetch giveaways from the GamerPower API
    def fetch_giveaways(platform=None, giveaway_type=None, sort_by=None):
        base_url = "https://www.gamerpower.com/api/giveaways"
        params = {}
        
        if platform:
            params['platform'] = platform
        if giveaway_type:
            params['type'] = giveaway_type
        if sort_by:
            params['sort-by'] = sort_by
        
        response = requests.get(base_url, params=params)
        return response.json()



    st.title("Free Game Giveaway Informer")
    
    # Sidebar for filtering options
    st.sidebar.title("Filter Options")
    platform = st.sidebar.selectbox("Platform", ["All", "PC", "Steam", "Epic Games Store", "Ubisoft", "GOG", "Itch.io", "PS4", "PS5", "Xbox One", "Xbox Series X/S", "Switch", "Android", "iOS", "VR", "Battle.net", "Origin", "DRM-Free", "Xbox 360"])
    giveaway_type = st.sidebar.selectbox("Type", ["All", "Game", "Loot", "Beta"])
    sort_by = st.sidebar.selectbox("Sort By", ["Date", "Value", "Popularity"])
    
    # Fetch giveaways based on selected filters
    if platform != "All":
        platform = platform.lower().replace(" ", "-")
    if giveaway_type != "All":
        giveaway_type = giveaway_type.lower()
    if sort_by == "Date":
        sort_by = "date"
    elif sort_by == "Value":
        sort_by = "value"
    elif sort_by == "Popularity":
        sort_by = "popularity"
    
    giveaways = fetch_giveaways(platform, giveaway_type, sort_by)
    
    # Display giveaways
    st.subheader("Current Giveaways:")
    for giveaway in giveaways:
        st.markdown(f"**{giveaway['title']}**")
        st.write(f"Platform: {giveaway['platform']}")
        st.write(f"Type: {giveaway['type']}")
        st.write(f"Ends: {giveaway['endDate']}")
        st.write(f"Link: {giveaway['open_giveaway_url']}")
        st.write("---")


