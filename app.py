import streamlit as st
import requests

# Function to get property information from the API
def get_property_info(api_key, address):
    api_url = f'https://api.propertymole.com/v1/property?address={address}&apikey={api_key}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error making API request: {e}")
        return None

# Function to edit property information via the API
def edit_property_info(api_key, property_id, new_data):
    api_url = f'https://api.propertymole.com/v1/property/{property_id}?apikey={api_key}'

    try:
        response = requests.put(api_url, json=new_data)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        updated_data = response.json()
        return updated_data
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

    # Edit Property Info
    st.sidebar.header("Edit Property Info:")
    property_id = st.sidebar.text_input("Enter Property ID for Editing:")
    new_data = {}

    new_data['bedrooms'] = st.sidebar.number_input("Edit Bedrooms", min_value=0)
    # Add more fields for editing similarly

    if st.sidebar.button("Update Property Info") and property_id:
        if api_key:
            updated_property = edit_property_info(api_key, property_id, new_data)
            if updated_property:
                st.success("Property information updated successfully.")
                display_property_info(updated_property)
            else:
                st.warning("Failed to update property information.")

if __name__ == "__main__":
    main()

