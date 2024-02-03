import streamlit as st
import csv
import json
from urllib.parse import quote

# Function to get property information from the API
def get_property_info(api_key, address):
    # Your existing code for making API requests

# Display basic property details
def display_basic_details(property_data):
    # Your existing code for displaying basic details

# Display property features
def display_features(features):
    # Your existing code for displaying features

# Display tax assessment details
def display_tax_assessment(tax_assessment):
    # Your existing code for displaying tax assessment details

# Display property taxes
def display_property_taxes(property_taxes):
    # Your existing code for displaying property taxes

# Display owner information
def display_owner_info(owner):
    # Your existing code for displaying owner information

# Display geographical information
def display_geographical_info(property_data):
    # Your existing code for displaying geographical information

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

                # Display different sections of property information
                display_basic_details(property_data)
                display_features(property_data['features'])
                display_tax_assessment(property_data['taxAssessment'])
                display_property_taxes(property_data['propertyTaxes'])
                display_owner_info(property_data['owner'])
                display_geographical_info(property_data)

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
