import streamlit as st
import http.client
import csv
import json
from urllib.parse import quote

# Function to get property information from the API using http.client
def get_property_info(api_key, address):
    conn = http.client.HTTPSConnection("realty-mole-property-api.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'realty-mole-property-api.p.rapidapi.com'
    }

    try:
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
        return None  # Error making the API request

    finally:
        conn.close()

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
                # Display organized property information
                st.write("### Property Information:")
                property_data = properties[0]
                for key, value in property_data.items():
                    st.write(f"**{key}:** {value}")

                # Export to CSV
                if st.button("Export to CSV"):
                    with open("property_info.csv", "w", newline="") as csvfile:
                        csv_writer = csv.writer(csvfile)
                        csv_writer.writerow(property_data.keys())
                        csv_writer.writerow(property_data.values())
                    st.success("Data exported successfully to property_info.csv.")
            else:
                st.warning("No data available for the provided address.")
        else:
            st.warning("Please provide both API key and address.")

if __name__ == "__main__":
    main()
