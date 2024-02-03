import streamlit as st
import requests

# Function to get property information from the API
def get_property_info(api_key, address):
    api_url = 'https://realty-mole-property-api.p.rapidapi.com/properties'
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'realty-mole-property-api.p.rapidapi.com'
    }

    params = {'address': address}

    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error making API request: {e}")
        return None

# Function to display property information
def display_property_info(property_info):
    st.write("### Property Information:")
    st.write(f"**Address Line 1:** {property_info.get('addressLine1', 'N/A')}")
    st.write(f"**City:** {property_info.get('city', 'N/A')}")
    st.write(f"**State:** {property_info.get('state', 'N/A')}")
    st.write(f"**Zip Code:** {property_info.get('zipCode', 'N/A')}")
    st.write(f"**Formatted Address:** {property_info.get('formattedAddress', 'N/A')}")
    st.write(f"**Assessor ID:** {property_info.get('assessorID', 'N/A')}")
    st.write(f"**Bedrooms:** {property_info.get('bedrooms', 'N/A')}")
    # Add more fields similarly

# Main Streamlit app
def main():
    st.title("Realtor Property Information App")

    # Sidebar for user input
    st.sidebar.header("User Input:")
    api_key = st.sidebar.text_input("Enter your API key:")
    address = st.sidebar.text_input("Enter the address:")

    if st.sidebar.button("Get Property Info"):
        if api_key and address:
            properties = get_property_info(api_key, address)
            if properties:
                display_property_info(properties)
            else:
                st.warning("No data available for the provided address.")

    # ... (rest of the code remains the same)

if __name__ == "__main__":
    main()
