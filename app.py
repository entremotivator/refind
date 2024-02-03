import streamlit as st
import http.client
import pandas as pd
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
            return data
        else:
            st.error(f"Unexpected response content: {res.read().decode('utf-8')}")
            return None

    except Exception as e:
        st.error(f"Error making API request: {e}")
        return None

    finally:
        conn.close()

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
                # Parse JSON response
                property_data = pd.json_normalize(properties)
                
                # Display organized property information
                st.write("### Property Information:")
                st.write(property_data)

                # Export to CSV
                if st.button("Export to CSV"):
                    property_data.to_csv("property_info.csv", index=False)
                    st.success("Data exported successfully to property_info.csv.")
            else:
                st.warning("No data available for the provided address.")
        else:
            st.warning("Please provide both API key and address.")

if __name__ == "__main__":
    main()
