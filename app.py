import streamlit as st
import http.client
import json
from urllib.parse import quote
from typing import Any, Dict, Optional

# Function to get property information from the API with caching
@st.cache(show_spinner=False)
def get_property_info(api_key: str, address: str) -> Optional[Dict[str, Any]]:
    try:
        with http.client.HTTPSConnection("realty-mole-property-api.p.rapidapi.com") as conn:
            headers = {
                'X-RapidAPI-Key': api_key,
                'X-RapidAPI-Host': 'realty-mole-property-api.p.rapidapi.com'
            }

            # Encode the address for the URL
            encoded_address = quote(address)

            # Make the API request
            conn.request("GET", f"/properties?address={encoded_address}", headers=headers)
            res = conn.getresponse()

            # Check if the response contains JSON data
            if 'application/json' in res.getheader('Content-Type', ''):
                return json.load(res)

    except Exception as e:
        st.exception(f"An error occurred: {e}")

    return None

# Function to display property information
def display_property_info(property_data: Dict[str, Any]) -> None:
    st.markdown("### Property Information")
    for key, value in property_data.items():
        st.write(f"**{key}:** {value}")

# Main Streamlit app
def main() -> None:
    st.title("Realtor Property Information App")

    # Sidebar for user input
    st.sidebar.header("User Input:")
    api_key = st.sidebar.text_input("Enter your API key", help="Obtain it from Realty Mole API")
    address = st.sidebar.text_input("Enter the address", help="E.g., 5500 Grand Lake Dr, San Antonio, TX, 78244")

    if st.sidebar.button("Get Property Info"):
        if api_key and address:
            with st.spinner("Fetching property information..."):
                properties = get_property_info(api_key, address)

            if properties:
                # Display property information
                display_property_info(properties[0])
            else:
                st.warning("No data available for the provided address.")
        else:
            st.warning("Please provide both API key and address.")

if __name__ == "__main__":
    main()
