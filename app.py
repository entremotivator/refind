import streamlit as st
import requests

# Function to get property information from the API
def get_property_info(api_key, address):
    url = "https://realty-mole-property-api.p.rapidapi.com/properties"
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'realty-mole-property-api.p.rapidapi.com'
    }

    params = {'address': address}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        response_headers = response.headers
        return data, response_headers
    except requests.exceptions.RequestException as e:
        st.error(f"Error making API request: {e}")
        return None, None

# Function to display property information
def display_property_info(property_info, response_headers):
    st.write("### Property Information:")
    st.write(f"**Address Line 1:** {property_info.get('addressLine1', 'N/A')}")
    st.write(f"**City:** {property_info.get('city', 'N/A')}")
    st.write(f"**State:** {property_info.get('state', 'N/A')}")
    st.write(f"**Zip Code:** {property_info.get('zipCode', 'N/A')}")
    st.write(f"**Formatted Address:** {property_info.get('formattedAddress', 'N/A')}")
    st.write(f"**Assessor ID:** {property_info.get('assessorID', 'N/A')}")
    st.write(f"**Bedrooms:** {property_info.get('bedrooms', 'N/A')}")

    # Check if the 'features' key exists before trying to access its properties
    features = property_info.get('features', {})
    st.write("#### Features:")
    st.write(f"**Architecture Type:** {features.get('architectureType', 'N/A')}")
    st.write(f"**Cooling:** {features.get('cooling', 'N/A')}")
    st.write(f"**Cooling Type:** {features.get('coolingType', 'N/A')}")
    # Add more feature fields similarly

    # Display response headers
    st.write("### Response Headers:")
    for key, value in response_headers.items():
        st.write(f"**{key}:** {value}")

# Main Streamlit app
def main():
    st.title("Realtor Property Information App")

    # Sidebar for user input
    st.sidebar.header("User Input:")
    api_key = st.sidebar.text_input("Enter your API key:")
    address = st.sidebar.text_input("Enter the address:")

    if st.sidebar.button("Get Property Info"):
        if api_key and address:
            properties, headers = get_property_info(api_key, address)
            if properties:
                display_property_info(properties, headers)
            else:
                st.warning("No data available for the provided address.")
        else:
            st.warning("Please provide both API key and address.")

if __name__ == "__main__":
    main()
