import streamlit as st
import http.client
import csv
import json
from urllib.parse import quote

# Function to make the API request
def make_api_request(api_key, address):
    try:
        conn = http.client.HTTPSConnection("realty-mole-property-api.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': api_key,
            'X-RapidAPI-Host': 'realty-mole-property-api.p.rapidapi.com'
        }

        encoded_address = quote(address)
        conn.request("GET", f"/properties?address={encoded_address}", headers=headers)
        res = conn.getresponse()

        if 'application/json' in res.getheader('Content-Type', ''):
            data = res.read().decode("utf-8")
            return json.loads(data)
        else:
            return None

    except Exception as e:
        return None

    finally:
        conn.close()

# Function to handle API response
def handle_api_response(api_key, address):
    properties = make_api_request(api_key, address)
    
    if properties:
        return properties
    else:
        st.warning("Failed to fetch property information. Please check your API key and address.")
        return None

# Function to display property information with improved formatting
def display_property_info(property_data):
    st.write("### Property Information:")
    st.write(f"**Address:** {property_data['formattedAddress']}")
    st.write(f"**Assessor ID:** {property_data['assessorID']}")
    st.write(f"**Bedrooms:** {property_data['bedrooms']}")
    st.write(f"**Bathrooms:** {property_data['bathrooms']}")
    st.write(f"**Square Footage:** {property_data['squareFootage']}")
    st.write(f"**Year Built:** {property_data['yearBuilt']}")
    st.write(f"**Lot Size:** {property_data['lotSize']}")
    st.write(f"**Property Type:** {property_data['propertyType']}")
    st.write(f"**Last Sale Date:** {property_data['lastSaleDate']}")
    st.write(f"**Last Sale Price:** {property_data['lastSalePrice']}")
    st.write(f"**Owner Occupied:** {'Yes' if property_data['ownerOccupied'] else 'No'}")
    
    st.write("#### Features:")
    for key, value in property_data['features'].items():
        st.write(f"**{key}:** {value}")

    st.write("#### Tax Assessment:")
    for year, data in property_data['taxAssessment'].items():
        st.write(f"**Year {year}:** {data['value']} (Land: {data['land']}, Improvements: {data['improvements']})")

    st.write("#### Owner:")
    st.write(f"**Name(s):** {', '.join(property_data['owner']['names'])}")
    st.write(f"**Mailing Address:** {property_data['owner']['mailingAddress']['addressLine1']}, {property_data['owner']['mailingAddress']['city']}, {property_data['owner']['mailingAddress']['state']} {property_data['owner']['mailingAddress']['zipCode']}")

    st.write("#### Property Taxes:")
    for year, data in property_data['propertyTaxes'].items():
        st.write(f"**Year {year}:** {data['total']}")

    st.write(f"**ID:** {property_data['id']}")
    st.write(f"**Longitude:** {property_data['longitude']}")
    st.write(f"**Latitude:** {property_data['latitude']}")

# Function to export data to CSV
def export_to_csv(property_data, filename="property_info.csv"):
    try:
        with open(filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(property_data[0].keys())

            for property_info in property_data:
                csv_writer.writerow(property_info.values())

        st.success(f"Data exported successfully to {filename}.")
    except Exception as e:
        st.warning(f"Failed to export data to CSV. Error: {e}")

# Main Streamlit app
def main():
    st.title("Realtor Property Information App")
    st.sidebar.header("User Input:")
    
    api_key = st.sidebar.text_input("Enter your API key", help="Get it from Realty Mole API")
    address = st.sidebar.text_input("Enter the address", help="E.g., 5500 Grand Lake Dr, San Antonio, TX, 78244")

    if st.sidebar.button("Get Property Info"):
        if api_key and address:
            with st.spinner("Fetching property information..."):
                properties = handle_api_response(api_key, address)
            
            if properties:
                display_property_info(properties[0])

                # Export to CSV
                if st.button("Export to CSV"):
                    export_to_csv(properties)
        else:
            st.warning("Please provide both API key and address.")

if __name__ == "__main__":
    main()
