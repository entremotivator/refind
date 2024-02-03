import streamlit as st
import http.client
import csv
import json
from urllib.parse import quote

# Function to get property information from the API using http.client
def get_property_info(api_key, address):
    try:
        conn = http.client.HTTPSConnection("realty-mole-property-api.p.rapidapi.com")
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
            data = res.read().decode("utf-8")
            return json.loads(data)
        else:
            return None  # No JSON data in the response

    except Exception as e:
        st.exception(f"An error occurred: {e}")
        return None

    finally:
        conn.close()

# Function to display property information
def display_property_info(property_data):
    st.write("### Property Information:")
    for key, value in property_data.items():
        st.write(f"**{key}:** {value}")

# Function to export data to CSV
def export_to_csv(property_data, filename="property_info.csv"):
    try:
        with open(filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(property_data.keys())
            csv_writer.writerow(property_data.values())
        st.success(f"Data exported successfully to {filename}.")
    except Exception as e:
        st.warning(f"Failed to export data to CSV. Error: {e}")

# Main Streamlit app
def main():
    st.title("Realtor Property Information App")

    # Sidebar for user input
    st.sidebar.header("User Input:")
    api_key = st.sidebar.text_input("Enter your API key", help="Get it from Realty Mole API")
    address = st.sidebar.text_input("Enter the address", help="E.g., 5500 Grand Lake Dr, San Antonio, TX, 78244")

    if st.sidebar.button("Get Property Info"):
        if api_key and address:
            with st.spinner("Fetching property information..."):
                properties = get_property_info(api_key, address)
            if properties:
                display_property_info(properties[0])

                # Export to CSV
                if st.button("Export to CSV"):
                    export_to_csv(properties[0])
            else:
                st.warning("No data available for the provided address.")
        else:
            st.warning("Please provide both API key and address.")

if __name__ == "__main__":
    main()
